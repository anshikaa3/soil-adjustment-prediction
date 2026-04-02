# 🌱 Soil Adjustment Prediction System

A smart **Machine Learning + Web-based application** that predicts soil nutrient adjustments, recommends fertilizers, and suggests suitable crops using **real-time weather data (API integration)**.

---

## 🚀 Live Demo

🔗 https://soil-adjustment-prediction-production-6595.up.railway.app/

---

## 📌 Key Features

* 🌾 **Crop Selection**: User selects crop and city
* 🌐 **Weather API Integration**:

  * Automatically fetches:

    * Temperature
    * Humidity
    * Wind Speed
* ⚡ **Auto Input System**:

  * Minimal manual input required
  * Uses **default agronomic values** for missing fields

---

## 📊 ML Predictions

The model predicts:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

---

## 💊 Fertilizer Recommendations

Based on predicted values:

* Urea → Nitrogen
* DAP → Phosphorus
* MOP → Potassium

---

## 🌱 Smart Crop Recommendation

* Suggests alternative crops
* Only triggers when environmental conditions are not suitable

---

## 📈 Data Visualization

* 📊 Interactive **NPK Bar Chart** (Chart.js)
* Helps users easily understand nutrient requirements

---

## 🧠 Technologies Used

* **Backend**: Flask (Python)
* **Machine Learning**: Scikit-learn
* **Data Processing**: Pandas, NumPy
* **Model Handling**: Joblib
* **API Integration**: OpenWeather API
* **Frontend**: HTML, CSS, Chart.js

---

## 📁 Project Structure

```
├── app.py
├── model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── Crop_recommendationV2.csv
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── weeding.jpeg
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ How It Works

1. User inputs:

   * City
   * Crop

2. System:

   * Fetches weather data via API
   * Auto-fills missing parameters using default values
   * Processes data through ML model

3. Output:

   * Soil adjustment recommendations
   * Fertilizer suggestions
   * Crop recommendations (if required)
   * NPK visualization graph

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/anshikaa3/soil-adjustment-prediction.git
cd soil-adjustment-prediction

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python app.py
```



---

## 📊 Dataset

The dataset includes:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall
* Crop label

---

## 📷 Screenshots

### Dashboard

![Dashboard](https://github.com/user-attachments/assets/ea9822bf-c03e-44aa-9f3d-783af1851ab8)

### Input

![Input](https://github.com/user-attachments/assets/9a00d793-3ed9-4140-b2b7-9cb7b81ea4b5)

### Output

![Output1](https://github.com/user-attachments/assets/40fc31da-6b3d-42fa-909a-5849d55739c7)
![Output2](https://github.com/user-attachments/assets/8b1b577d-92e2-4edd-8a54-a87bf9fc7baf)

---

## 🚀 Future Enhancements

* 🌐 IoT sensor integration (real-time soil data)
* 🤖 Advanced ML-based crop recommendation
* 📱 Mobile app version
* 📊 More interactive dashboards

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

---

## 👩‍💻 Author

**Anshika Srivastava**

📧 [anshikasrivastava0304@gmail.com](mailto:anshikasrivastava0304@gmail.com)
🔗 https://github.com/anshikaa3

---

