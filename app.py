from flask import Flask, request, render_template
import pandas as pd
import joblib
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

API_KEY = "35f8c662dee6aa7e7297d751a176ef1c"

# 💰 Crop economics
crop_economics = {
    "Rice": {"price": 20, "cost": 10000, "yield": 2000},
    "Wheat": {"price": 18, "cost": 8000, "yield": 1800},
    "Maize": {"price": 15, "cost": 7000, "yield": 1500},
    "Sugarcane": {"price": 30, "cost": 15000, "yield": 3000},
    "Potato": {"price": 12, "cost": 6000, "yield": 1400}
}

# 🌦️ UPDATED WEATHER API (FULL DATA)
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        return {
            "wind_speed": data["wind"]["speed"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
    except:
        return {
            "wind_speed": 5,
            "temperature": 25,
            "humidity": 60
        }


feature_order = [
    'soil_moisture', 'soil_type', 'sunlight_exposure', 'wind_speed',
    'co2_concentration', 'organic_matter', 'irrigation_frequency',
    'crop_density', 'pest_pressure', 'fertilizer_usage', 'growth_stage',
    'urban_area_proximity', 'water_source_type', 'frost_risk',
    'water_usage_efficiency', 'crop_label'
]

soil_type_mapping = {"Clay": 0, "Sandy": 1, "Loamy": 2}
water_source_mapping = {"Canal": 0, "Rain": 1, "Groundwater": 2}


@app.route("/", methods=["GET", "POST"])
def index():
    predicted_output = None
    fertilizer_recommendations = []
    recommended_crops = []
    profit_data = []
    comparison_result = []
    reasons = []
    user_input = {}

    if request.method == "POST":
        try:
            city = request.form.get("city")

            # 🌦️ Get API data
            weather = get_weather(city)

            # 🔥 DEFAULT VALUES (no more 0)
            defaults = {
                "soil_moisture": 50,
                "sunlight_exposure": 6,
                "co2_concentration": 400,
                "organic_matter": 5,
                "irrigation_frequency": 7,
                "crop_density": 10,
                "pest_pressure": 3,
                "fertilizer_usage": 20,
                "growth_stage": 2,
                "urban_area_proximity": 5,
                "frost_risk": 1,
                "water_usage_efficiency": 70
            }

            # Input handling
            for key in feature_order[:-1]:

                if key == "soil_type":
                    user_input[key] = soil_type_mapping.get(request.form.get("soil_type"), 0)

                elif key == "water_source_type":
                    user_input[key] = water_source_mapping.get(request.form.get("water_source_type"), 0)

                elif key == "wind_speed":
                    user_input[key] = weather["wind_speed"]

                else:
                    value = request.form.get(key)
                    user_input[key] = float(value) if value else defaults.get(key, 0)

            # Crop encoding
            crop_name = request.form.get("crop")
            user_input["crop_label"] = int(label_encoder.transform([crop_name])[0]) if crop_name else 0

            # Prediction
            input_df = pd.DataFrame([user_input])[feature_order]
            input_scaled = scaler.transform(input_df)
            predicted = model.predict(input_scaled)[0]

            # ✅ Predicted Output
            predicted_output = {
                "Nitrogen (N)": f"{predicted[0]:.2f}",
                "Phosphorus (P)": f"{predicted[1]:.2f}",
                "Potassium (K)": f"{predicted[2]:.2f}",
                "Temperature (°C)": f"{predicted[3]:.2f}",
                "Humidity (%)": f"{predicted[4]:.2f}",
                "pH": f"{predicted[5]:.2f}",
                "Rainfall (mm)": f"{predicted[6]:.2f}"
            }

            # 🌿 Fertilizer
            n, p, k = predicted[:3]
            if n > 0:
                fertilizer_recommendations.append(f"Add {n*2:.2f} kg Urea")
            if p > 0:
                fertilizer_recommendations.append(f"Add {p*1.5:.2f} kg DAP")
            if k > 0:
                fertilizer_recommendations.append(f"Add {k*2:.2f} kg MOP")

            # 🌱 Crop Recommendation
            temp = predicted[3]
            rainfall = predicted[6]
            humidity = predicted[4]

            if temp < 25:
                recommended_crops.append("wheat")
            if rainfall > 100:
                recommended_crops.append("rice")
            if humidity > 60:
                recommended_crops.append("sugarcane")
            if temp > 28:
                recommended_crops.append("maize")

            if len(recommended_crops) < 2:
                recommended_crops = ["wheat", "rice"]

            # 💰 Profit
            for crop in recommended_crops:
                data = crop_economics.get(crop.capitalize())
                if data:
                    profit = (data["yield"] * data["price"]) - data["cost"]
                    profit_data.append({
                        "crop": crop.capitalize(),
                        "profit": profit
                    })

            # 📊 Comparison
            if len(recommended_crops) >= 2:
                c1 = crop_economics.get(recommended_crops[0].capitalize())
                c2 = crop_economics.get(recommended_crops[1].capitalize())

                comparison_result = [
                    {"factor": "Profit", "crop1": c1["yield"] * c1["price"],
                     "crop2": c2["yield"] * c2["price"]},
                    {"factor": "Cost", "crop1": c1["cost"],
                     "crop2": c2["cost"]}
                ]

            # 🧠 Reasons
            reasons = ["Auto-filled using API", "Balanced environment", "Optimized conditions"]

        except Exception as e:
            print("ERROR:", e)

    return render_template(
        "index.html",
        user_input=user_input,
        predicted_output=predicted_output,
        fertilizer_recommendations=fertilizer_recommendations,
        recommended_crops=[c.capitalize() for c in recommended_crops],
        profit_data=profit_data,
        comparison_result=comparison_result,
        reasons=reasons,
        crops=label_encoder.classes_
    )


if __name__ == "__main__":
    app.run(debug=True)