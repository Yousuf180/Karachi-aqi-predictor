# 🇵🇰 Karachi AQI Predictor

Real-time Air Quality Index prediction for Karachi, Pakistan using Machine Learning.

## 📊 Features
- Real-time AQI data from OpenWeather API
- 3-day AQI forecast using Random Forest
- Interactive dashboard with Streamlit
- Historical data analysis
- Color-coded health alerts

## 🛠️ Tech Stack
- **Python** - Core programming language
- **Google Colab** - Development environment
- **OpenWeather API** - Air quality data
- **Hopsworks** - Feature store & model registry
- **Scikit-learn** - Machine learning
- **Streamlit** - Web dashboard
- **Plotly** - Interactive charts

## 🚀 Quick Start

### Option 1: Open in Colab
Click the badge below to open directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yousuf180/Karachi-aqi-predictor/blob/main/AQI_Forecasting_Project.ipynb)

### Option 2: Run Dashboard Locally
```bash
# Clone repository
git clone https://github.com/Yousuf180/Karachi-aqi-predictor.git
cd Karachi-aqi-predictor

# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run app.py
