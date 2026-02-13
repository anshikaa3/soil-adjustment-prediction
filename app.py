from flask import Flask, request, render_template
import pandas as pd
import joblib

# Load the model, scaler, and label encoder
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__, static_folder='static', template_folder='templates')


# Input feature order expected by model
feature_order = [
    'soil_moisture', 'soil_type', 'sunlight_exposure', 'wind_speed',
    'co2_concentration', 'organic_matter', 'irrigation_frequency',
    'crop_density', 'pest_pressure', 'fertilizer_usage', 'growth_stage',
    'urban_area_proximity', 'water_source_type', 'frost_risk',
    'water_usage_efficiency', 'crop_label'
]

# Categorical feature mappings
soil_type_mapping = {"Clay": 0, "Sandy": 1, "Loamy": 2, "Silty": 3, "Peaty": 4, "Chalky": 5}
water_source_mapping = {"Canal": 0, "River": 1, "Rain": 2, "Groundwater": 3, "Tank": 4}

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_output = None
    user_input = None
    fertilizer_recommendations = None

    if request.method == "POST":
        try:
            user_input = {}
            for key in feature_order[:-1]:  # exclude 'crop_label'
                if key == "soil_type":
                    user_input["soil_type"] = soil_type_mapping.get(request.form["soil_type"])
                elif key == "water_source_type":
                    user_input["water_source_type"] = water_source_mapping.get(request.form["water_source_type"])
                else:
                    user_input[key] = float(request.form[key])

            # Encode crop label
            crop_name = request.form.get("crop")
            user_input["crop_label"] = int(label_encoder.transform([crop_name])[0])

            # Prepare DataFrame
            input_data = pd.DataFrame([user_input])[feature_order]
            input_data_scaled = scaler.transform(input_data)

            # Predict
            predicted_adjustments = model.predict(input_data_scaled)[0]

            # Build output
            predicted_output = {
                "Nitrogen (N)": f"{predicted_adjustments[0]:.2f}",
                "Phosphorus (P)": f"{predicted_adjustments[1]:.2f}",
                "Potassium (K)": f"{predicted_adjustments[2]:.2f}",
                "Temperature (°C)": f"{predicted_adjustments[3]:.2f}",
                "Humidity (%)": f"{predicted_adjustments[4]:.2f}",
                "pH": f"{predicted_adjustments[5]:.2f}",
                "Rainfall (mm)": f"{predicted_adjustments[6]:.2f}"
            }

            # Fertilizer Recommendations
            n, p, k = predicted_adjustments[:3]
            fertilizer_recommendations = []
            if n > 0: fertilizer_recommendations.append(f"Add {n * 2:.2f} kg Urea (Nitrogen)")
            if p > 0: fertilizer_recommendations.append(f"Add {p * 1.5:.2f} kg DAP (Phosphorus)")
            if k > 0: fertilizer_recommendations.append(f"Add {k * 2:.2f} kg MOP (Potassium)")

        except Exception as e:
            print("❌ Error:", e)

    return render_template("index.html",
                           user_input=user_input,
                           predicted_output=predicted_output,
                           fertilizer_recommendations=fertilizer_recommendations,
                           crops=label_encoder.classes_)
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

