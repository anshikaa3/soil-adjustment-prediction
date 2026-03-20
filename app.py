from flask import Flask, request, render_template
import pandas as pd
import joblib
import requests
import os

# Load model
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__, static_folder='static', template_folder='templates')

API_KEY = "35f8c662dee6aa7e7297d751a176ef1c"

# Weather API
def get_weather(city):
    try:
        if not city:
            return 5
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        if data.get("cod") != 200:
            return 5

        return data["wind"]["speed"]
    except:
        return 5


feature_order = [
    'soil_moisture', 'soil_type', 'sunlight_exposure', 'wind_speed', 
    'co2_concentration', 'organic_matter', 'irrigation_frequency',
    'crop_density', 'pest_pressure', 'fertilizer_usage', 'growth_stage',
    'urban_area_proximity', 'water_source_type', 'frost_risk',
    'water_usage_efficiency', 'crop_label'
]

soil_type_mapping = {"Clay": 0, "Sandy": 1, "Loamy": 2, "Silty": 3, "Peaty": 4, "Chalky": 5}
water_source_mapping = {"Canal": 0, "River": 1, "Rain": 2, "Groundwater": 3, "Tank": 4}


@app.route("/", methods=["GET", "POST"])
def index():
    predicted_output = None
    user_input = None
    fertilizer_recommendations = None
    recommended_crops = []   # ✅ NEW

    if request.method == "POST":
        try:
            user_input = {}

            city = request.form.get("city")
            wind_speed_api = get_weather(city)

            for key in feature_order[:-1]:

                if key == "soil_type":
                    user_input[key] = soil_type_mapping.get(request.form.get("soil_type"), 0)

                elif key == "water_source_type":
                    user_input[key] = water_source_mapping.get(request.form.get("water_source_type"), 0)

                elif key == "wind_speed":
                    user_input[key] = float(wind_speed_api)

                else:
                    value = request.form.get(key)
                    try:
                        user_input[key] = float(value)
                    except:
                        user_input[key] = 0

            # crop encoding
            crop_name = request.form.get("crop")
            if crop_name:
                user_input["crop_label"] = int(label_encoder.transform([crop_name])[0])
            else:
                user_input["crop_label"] = 0

            # DataFrame
            input_df = pd.DataFrame([user_input])[feature_order]
            input_scaled = scaler.transform(input_df)

            # Prediction
            predicted_adjustments = model.predict(input_scaled)[0]

            print("Prediction:", predicted_adjustments)

            predicted_output = {
                "Nitrogen (N)": f"{predicted_adjustments[0]:.2f}",
                "Phosphorus (P)": f"{predicted_adjustments[1]:.2f}",
                "Potassium (K)": f"{predicted_adjustments[2]:.2f}",
                "Temperature (°C)": f"{predicted_adjustments[3]:.2f}",
                "Humidity (%)": f"{predicted_adjustments[4]:.2f}",
                "pH": f"{predicted_adjustments[5]:.2f}",
                "Rainfall (mm)": f"{predicted_adjustments[6]:.2f}"
            }

            # Fertilizer
            n, p, k = predicted_adjustments[:3]
            fertilizer_recommendations = []

            if n > 0:
                fertilizer_recommendations.append(f"Add {n * 2:.2f} kg Urea (Nitrogen)")
            if p > 0:
                fertilizer_recommendations.append(f"Add {p * 1.5:.2f} kg DAP (Phosphorus)")
            if k > 0:
                fertilizer_recommendations.append(f"Add {k * 2:.2f} kg MOP (Potassium)")

            # 🌱 Crop Recommendation (NEW FEATURE)
            temp = predicted_adjustments[3]
            humidity = predicted_adjustments[4]
            ph = predicted_adjustments[5]
            rainfall = predicted_adjustments[6]

            # Always suggest based on conditions
            if temp <= 25:
              recommended_crops.append("Wheat")

            if rainfall >= 50:
               recommended_crops.append("Rice")

            if ph <= 6.5:
               recommended_crops.append("Potato")

            if humidity >= 40:
             recommended_crops.append("Sugarcane")

            if temp >= 25:
             recommended_crops.append("Maize")

            if not recommended_crops:
               recommended_crops = ["Wheat", "Rice"]
        except Exception as e:
            print("❌ ERROR:", e)

    return render_template(
        "index.html",
        user_input=user_input,
        predicted_output=predicted_output,
        fertilizer_recommendations=fertilizer_recommendations,
        recommended_crops=recommended_crops,   # ✅ PASS
        crops=label_encoder.classes_
    )


if __name__ == "__main__":
    app.run(debug=True)