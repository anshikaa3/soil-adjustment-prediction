# 🌱 Soil Adjustment Prediction System

A smart dashboard-enabled machine learning system for analyzing real-time and manual soil parameters and suggesting optimal nutrient adjustments, fertilizer recommendations, and crop-growing strategies.

---

## 📌 Features

- 🌾 **Crop Label Prediction**: Encodes crop labels from user input.
- 🧪 **Soil Parameter Input**: Allows manual input from farmers or automated input from IoT devices.
- 🌐 **Web Dashboard UI**: Interactive, dashboard-like structure with quick access to multiple tools.
- 📊 **Adjustment Predictions**: Outputs required corrections for N, P, K, pH, temperature, humidity, and rainfall.
- 💊 **Fertilizer Recommendations**: Calculates Urea, DAP, MOP doses based on predicted soil deficiencies.
- 📅 **Modular Dashboard Tabs**:
  - 📉 Soil Moisture Comparison (Graph)
  - 🌦️ Weather Forecasts for Sowing
  - 📈 Yield Analysis: Actual vs Predicted
  - 💰 Crop Revenue Timing Suggestion
  - 🔗 Task Management: Connects to nearby farmers

---

## 💡 What's Unique?

- ✅ **IoT-Compatible**: Built to fetch sensor data in future updates.
- ✅ **Manually Usable**: Works seamlessly with or without sensor devices.
- ✅ **Real-time Scaling**: Supports scrollable and modular UI for large data sets.
- ✅ **Enhanced UI**: Clean, dark-themed input + bright recommendation layout.
- ✅ **Fertilizer Logic**: Based on predicted adjustments from ML model.

---

## 🧠 Technologies Used

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- HTML, CSS
- Bootstrap/Grid for layout
- Jupyter Notebook (model training)

---

## 📁 Project Structure

```
├── app.py                        # Flask backend for UI
├── model.pkl                    # ML model for adjustment prediction
├── scaler.pkl                   # Trained standard scaler
├── label_encoder.pkl            # Crop label encoder
├── Crop_recommendationV2.csv   # Dataset used
├── templates/
│   └── index.html               # UI Dashboard Page
├── static/
│   ├── style.css
│   └── weeding.jpeg             # Background image
├── README.md
```

---

## 🔢 Features Supported

| Section             | Functionality                                                   |
| ------------------- | --------------------------------------------------------------- |
| Dashboard (Default) | Main form + predictions                                         |
| Weather             | Shows best growing season info                                  |
| Soil Moisture       | Shows line graph comparing moisture vs needed moisture          |
| Crop Yield          | Displays actual/predicted yield ratio                           |
| Farm Revenue        | Shows peak time for selling the crop                            |
| Task Management     | Shows nearby farmers & allows contact for best selling strategy |

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/ArjitaSahu123/Soil_prediction-Project.git
cd Soil_prediction-Project
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 🧪 Technologies Used

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- TensorFlow / Keras
- HTML/CSS (for frontend)
- Jupyter Notebook

## 📊 Dataset

The dataset `Crop_recommendationV2.csv` contains labeled samples with the following features:

- **N** – Nitrogen level in the soil
- **P** – Phosphorus level
- **K** – Potassium level
- **temperature** – Temperature in Celsius
- **humidity** – Relative humidity
- **ph** – Soil pH value
- **rainfall** – Rainfall in mm
- **label** – Suitable crop name

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ArjitaSahu123/soil-adjustment-prediction.git
cd soil-adjustment-prediction
```

### 2. Install Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

If requirements.txt is not present, manually install:

```bash
pip install flask pandas numpy scikit-learn tensorflow
```

### 3. Run the Application

```bash
python app.py
```

### The app will be available at http://127.0.0.1:5000/.

### Work flow

![Screenshot 2024-11-04 143649](https://github.com/user-attachments/assets/145764c3-9986-4d5e-b81b-805bc8c892bb)

### 📷 Screenshots

![Screenshot 2024-12-08 152300](https://github.com/user-attachments/assets/ea9822bf-c03e-44aa-9f3d-783af1851ab8)

![Screenshot 2024-12-08 152334](https://github.com/user-attachments/assets/9a00d793-3ed9-4140-b2b7-9cb7b81ea4b5)

### Output

![Screenshot 2024-12-08 152357](https://github.com/user-attachments/assets/40fc31da-6b3d-42fa-909a-5849d55739c7)

![Screenshot 2024-12-08 152415](https://github.com/user-attachments/assets/8b1b577d-92e2-4edd-8a54-a87bf9fc7baf)

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

👩‍💻 Author

- Anshika Srivastava
- 📧 Contact: [anshikasrivastava0304@gmail.com]
- 🔗 GitHub: anshikaa3
