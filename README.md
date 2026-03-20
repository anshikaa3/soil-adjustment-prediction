# 🌱 Soil Adjustment Prediction System

A smart machine learning-based web application that predicts soil nutrient adjustments, recommends fertilizers, and suggests alternative crops using real-time weather data.

---

## 📌 Features

- 🌾 **Crop Selection**: User selects crop and location (city)
- 🌐 **Weather API Integration**: Automatically fetches real-time environmental data
- 🧪 **Reduced Manual Input**: Minimal input required (City + Crop)
- 📊 **Adjustment Predictions**:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall

- 💊 **Fertilizer Recommendations**:
  - Urea (Nitrogen)
  - DAP (Phosphorus)
  - MOP (Potassium)

- 🌱 **Smart Crop Recommendation**:
  - Suggests alternative crops **only when conditions are unsuitable**

---

## 💡 What's New (Latest Update)

- ✅ Integrated **Weather API (OpenWeather)**
- ✅ Reduced dependency on manual inputs
- ✅ Added **intelligent crop recommendation system**
- ✅ Improved decision logic (only suggests crops when needed)

---

## 🧠 Technologies Used

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- Joblib
- Requests (API integration)
- HTML, CSS

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
├── README.md
```

---

## ⚙️ How It Works

1. User inputs:
   - City
   - Crop

2. System:
   - Fetches weather data using API
   - Processes input
   - Runs ML model

3. Output:
   - Soil adjustments
   - Fertilizer recommendations
   - Crop recommendations (if required)

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

Visit: http://127.0.0.1:5000

---

## 🌐 Live Deployment

https://soil-adjustment-prediction-production.up.railway.app/

---

## 📊 Dataset

The dataset contains:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall
- Crop label

---

## 📷 Screenshots

![Dashboard](https://github.com/user-attachments/assets/ea9822bf-c03e-44aa-9f3d-783af1851ab8)

![Input](https://github.com/user-attachments/assets/9a00d793-3ed9-4140-b2b7-9cb7b81ea4b5)

---

## 📊 Output

![Output1](https://github.com/user-attachments/assets/40fc31da-6b3d-42fa-909a-5849d55739c7)

![Output2](https://github.com/user-attachments/assets/8b1b577d-92e2-4edd-8a54-a87bf9fc7baf)

---

## 🚀 Future Scope

- IoT sensor integration
- Advanced ML-based crop recommendation
- Mobile application support

---

## 🤝 Contributing

Pull requests are welcome.

---

## 👩‍💻 Author

- Anshika Srivastava
- 📧 [anshikasrivastava0304@gmail.com](mailto:anshikasrivastava0304@gmail.com)
- 🔗 https://github.com/anshikaa3
