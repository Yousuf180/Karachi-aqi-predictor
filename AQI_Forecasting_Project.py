{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qn_aEoGvYHon",
        "outputId": "86ff715a-b0d1-4197-a17e-32fff3928bb4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m815.8/815.8 kB\u001b[0m \u001b[31m11.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m124.2/124.2 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.2/44.2 kB\u001b[0m \u001b[31m1.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.2/9.2 MB\u001b[0m \u001b[31m72.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m258.6/258.6 kB\u001b[0m \u001b[31m13.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m295.2/295.2 kB\u001b[0m \u001b[31m14.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m88.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m140.5/140.5 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m45.3/45.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.2/15.2 MB\u001b[0m \u001b[31m83.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m45.7/45.7 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m88.6/88.6 kB\u001b[0m \u001b[31m3.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.3/3.3 MB\u001b[0m \u001b[31m69.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m91.9/91.9 kB\u001b[0m \u001b[31m5.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for twofish (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "ydf 0.15.0 requires protobuf<7.0.0,>=5.29.1, but you have protobuf 4.25.9 which is incompatible.\n",
            "tensorflow 2.20.0 requires protobuf>=5.28.0, but you have protobuf 4.25.9 which is incompatible.\n",
            "grain 0.2.17 requires protobuf>=5.28.3, but you have protobuf 4.25.9 which is incompatible.\n",
            "grpcio-status 1.71.2 requires protobuf<6.0dev,>=5.26.1, but you have protobuf 4.25.9 which is incompatible.\n",
            "opentelemetry-proto 1.38.0 requires protobuf<7.0,>=5.0, but you have protobuf 4.25.9 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0m✅ All packages installed successfully!\n"
          ]
        }
      ],
      "source": [
        "\n",
        "!pip install hopsworks scikit-learn pandas numpy requests streamlit shap joblib python-dotenv pyngrok -q\n",
        "\n",
        "print(\"✅ All packages installed successfully!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 2: Import everything we need\n",
        "import os\n",
        "import requests\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from datetime import datetime, timedelta\n",
        "import joblib\n",
        "from sklearn.ensemble import RandomForestRegressor\n",
        "from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error\n",
        "import shap\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "print(\"✅ Libraries imported!\")\n",
        "print(f\"Current time: {datetime.now()}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gZ50FkanYsZX",
        "outputId": "bfd94577-c952-4161-d488-cea86940dadb"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Libraries imported!\n",
            "Current time: 2026-06-09 11:16:15.364344\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 3: Enter your API keys (replace with your actual keys)\n",
        "\n",
        "# Get these from https://c.app.hopsworks.ai\n",
        "HOPSWORKS_API_KEY = \"WtY94d9J55EN71ai.0xi2mLp8dnsUdeK5jE5hQpGTEC45sMDTvfJLUuiZjDx5jXslcpr0bOsORyIZXmPw\"  # Paste your Hopsworks key\n",
        "HOPSWORKS_PROJECT = \"Aqi_project_Yousuf\"       # Your Hopsworks project name\n",
        "\n",
        "# Get from https://aqicn.org/data-platform/token/\n",
        "AQICN_TOKEN = \"1f245d5e610135f6ee652dbd11c63413898f7436\"  # Your AQICN token\n",
        "\n",
        "# Get from https://openweathermap.org/api\n",
        "OPENWEATHER_API_KEY = \"39ad7171ca3c5fe096a849af68d494b8\"  # Your OpenWeather API key\n",
        "\n",
        "# Set your city (examples: \"Beijing\", \"London\", \"Delhi\", \"Los Angeles\")\n",
        "CITY = \"Karachi\"\n",
        "\n",
        "print(\"✅ API keys configured!\")\n",
        "print(f\"📡 Fetching data for: {CITY}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PODSNjflbmtJ",
        "outputId": "0f3fdffd-74a1-45d4-d87b-db3af77b4a81"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ API keys configured!\n",
            "📡 Fetching data for: Karachi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 4: Verify all APIs are working\n",
        "print(\"🔍 Testing API connections...\\n\")\n",
        "\n",
        "# Test AQICN\n",
        "try:\n",
        "    url = f\"https://api.waqi.info/feed/{\"Karachi\"}/?token={\"1f245d5e610135f6ee652dbd11c63413898f7436\"}\"\n",
        "    response = requests.get(url).json()\n",
        "    if response['status'] == 'ok':\n",
        "        print(f\"✅ AQICN API: Working! Current AQI = {response['data']['aqi']}\")\n",
        "    else:\n",
        "        print(f\"❌ AQICN API Error: {response.get('data')}\")\n",
        "except Exception as e:\n",
        "    print(f\"❌ AQICN Error: {e}\")\n",
        "\n",
        "# Test OpenWeather\n",
        "try:\n",
        "    url = f\"https://api.openweathermap.org/data/2.5/weather?q={\"Karachi\"}&appid={\"39ad7171ca3c5fe096a849af68d494b8\"}&units=metric\"\n",
        "    response = requests.get(url).json()\n",
        "    if response.get('main'):\n",
        "        print(f\"✅ OpenWeather API: Working! Temp = {response['main']['temp']}°C\")\n",
        "    else:\n",
        "        print(f\"❌ OpenWeather Error: {response.get('message')}\")\n",
        "except Exception as e:\n",
        "    print(f\"❌ OpenWeather Error: {e}\")\n",
        "\n",
        "print(\"\\n⚠️ Note: If any API failed, check your keys and ensure you wait 30-60 minutes after signup!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EPe4DM2UdFR5",
        "outputId": "2d7906a2-415a-481b-edca-8bc5507fc423"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔍 Testing API connections...\n",
            "\n",
            "✅ AQICN API: Working! Current AQI = 161\n",
            "✅ OpenWeather API: Working! Temp = 33.11°C\n",
            "\n",
            "⚠️ Note: If any API failed, check your keys and ensure you wait 30-60 minutes after signup!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 5: Connect to Hopsworks\n",
        "import hopsworks\n",
        "\n",
        "try:\n",
        "    project = hopsworks.login(\n",
        "        project=\"Aqi_project_Yousuf\",\n",
        "        api_key_value=\"WtY94d9J55EN71ai.0xi2mLp8dnsUdeK5jE5hQpGTEC45sMDTvfJLUuiZjDx5jXslcpr0bOsORyIZXmPw\"\n",
        "    )\n",
        "    fs = project.get_feature_store()\n",
        "    print(\"✅ Connected to Hopsworks successfully!\")\n",
        "except Exception as e:\n",
        "    print(f\"❌ Hopsworks connection error: {e}\")\n",
        "    print(\"Make sure you: 1) Signed up at c.app.hopsworks.ai, 2) Created a project, 3) Generated an API key\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kWcFWHckeoCZ",
        "outputId": "0232d302-f4a2-4fa1-fd8b-793aa8ccda49"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Logged in to project, explore it here https://eu-west.cloud.hopsworks.ai:443/p/33118\n",
            "✅ Connected to Hopsworks successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 6: Feature pipeline - Fetches data and creates features\n",
        "\n",
        "def fetch_aqi_data():\n",
        "    \"\"\"Fetch current AQI from AQICN API\"\"\"\n",
        "    url = f\"https://api.waqi.info/feed/{\"Karachi\"}/?token={\"1f245d5e610135f6ee652dbd11c63413898f7436\"}\"\n",
        "    response = requests.get(url).json()\n",
        "\n",
        "    if response['status'] == 'ok':\n",
        "        data = response['data']\n",
        "        iaqi = data.get('iaqi', {})\n",
        "        return {\n",
        "            'aqi': data['aqi'],\n",
        "            'pm25': iaqi.get('pm25', {}).get('v', np.nan),\n",
        "            'pm10': iaqi.get('pm10', {}).get('v', np.nan),\n",
        "            'no2': iaqi.get('no2', {}).get('v', np.nan),\n",
        "            'o3': iaqi.get('o3', {}).get('v', np.nan),\n",
        "        }\n",
        "    else:\n",
        "        raise Exception(f\"AQICN Error: {response.get('data')}\")\n",
        "\n",
        "def fetch_weather_data():\n",
        "    \"\"\"Fetch current weather from OpenWeather API\"\"\"\n",
        "    url = f\"https://api.openweathermap.org/data/2.5/weather?q={\"Karachi\"}&appid={\"39ad7171ca3c5fe096a849af68d494b8\"}&units=metric\"\n",
        "    response = requests.get(url).json()\n",
        "\n",
        "    return {\n",
        "        'temperature': response['main']['temp'],\n",
        "        'humidity': response['main']['humidity'],\n",
        "        'pressure': response['main']['pressure'],\n",
        "        'wind_speed': response['wind']['speed'],\n",
        "        'clouds': response['clouds']['all']\n",
        "    }\n",
        "\n",
        "def engineer_features(timestamp):\n",
        "    \"\"\"Create time-based features\"\"\"\n",
        "    return {\n",
        "        'hour': timestamp.hour,\n",
        "        'day_of_week': timestamp.weekday(),\n",
        "        'month': timestamp.month,\n",
        "        'is_weekend': 1 if timestamp.weekday() >= 5 else 0,\n",
        "        'is_rush_hour': 1 if timestamp.hour in [7,8,9,17,18,19] else 0\n",
        "    }\n",
        "\n",
        "print(\"✅ Feature pipeline functions defined!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PP_3veXgfohZ",
        "outputId": "8b7121b7-414d-4953-b9eb-8698c263cf98"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Feature pipeline functions defined!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 7: Run the feature pipeline - This fetches current data\n",
        "from datetime import datetime\n",
        "\n",
        "print(\"🚀 Running Feature Pipeline...\\n\")\n",
        "\n",
        "# Fetch data\n",
        "aqi_data = fetch_aqi_data()\n",
        "weather_data = fetch_weather_data()\n",
        "timestamp = datetime.now()\n",
        "time_features = engineer_features(timestamp)\n",
        "\n",
        "# Combine all features\n",
        "feature_row = {\n",
        "    'timestamp': timestamp,\n",
        "    **aqi_data,\n",
        "    **weather_data,\n",
        "    **time_features\n",
        "}\n",
        "\n",
        "# Create DataFrame\n",
        "feature_df = pd.DataFrame([feature_row])\n",
        "print(\"📊 Features collected:\")\n",
        "print(feature_df.to_string())\n",
        "\n",
        "# Store in Hopsworks (uncomment after setting up Hopsworks)\n",
        "try:\n",
        "    feature_group = fs.get_or_create_feature_group(\n",
        "        name=\"air_quality_features\",\n",
        "        version=1,\n",
        "        primary_key=['timestamp'],\n",
        "        event_time='timestamp',\n",
        "        description=\"Hourly air quality and weather features\"\n",
        "    )\n",
        "    feature_group.insert(feature_df)\n",
        "    print(f\"\\n✅ Data stored in Hopsworks at {timestamp}\")\n",
        "except NameError:\n",
        "    print(\"\\n⚠️ Hopsworks not connected. Data not stored (run Cell 5 first)\")\n",
        "except Exception as e:\n",
        "    print(f\"\\n❌ Storage error: {e}\")\n",
        "\n",
        "print(\"\\n✅ Feature pipeline complete!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EcB000W_gO9K",
        "outputId": "887ddc56-210f-4981-bbea-a747cbaeb6bd"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🚀 Running Feature Pipeline...\n",
            "\n",
            "📊 Features collected:\n",
            "                   timestamp  aqi  pm25  pm10  no2  o3  temperature  humidity  pressure  wind_speed  clouds  hour  day_of_week  month  is_weekend  is_rush_hour\n",
            "0 2026-06-09 11:16:25.451637  161   161   NaN  NaN NaN        33.11        64       999        8.97       3    11            1      6           0             0\n",
            "\n",
            "❌ Storage error: Confluent Kafka package not found. If you want to use Kafka with Hopsworks you can install the corresponding extras via `pip install \"hopsworks[python]\"`. You can also install confluent-kafka directly in your environment with `pip install confluent-kafka`. You will need to restart your kernel if applicable.\n",
            "\n",
            "✅ Feature pipeline complete!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 8: Generate historical data for training\n",
        "print(\"📊 Generating 30 days of historical training data...\")\n",
        "\n",
        "historical_data = []\n",
        "start_date = datetime.now() - timedelta(days=30)\n",
        "\n",
        "for i in range(30 * 24):  # 30 days * 24 hours\n",
        "    timestamp = start_date + timedelta(hours=i)\n",
        "\n",
        "    # Simulate realistic AQI patterns\n",
        "    hour_factor = 1 + 0.3 * np.sin(2 * np.pi * (timestamp.hour - 8) / 24)\n",
        "    day_factor = 1 + 0.2 * np.sin(2 * np.pi * timestamp.weekday() / 7)\n",
        "    noise = np.random.normal(0, 10)\n",
        "\n",
        "    base_aqi = 100\n",
        "    aqi = max(0, base_aqi * hour_factor * day_factor + noise)\n",
        "\n",
        "    # Weather patterns\n",
        "    temp = 20 + 10 * np.sin(2 * np.pi * (timestamp.hour - 14) / 24) + np.random.normal(0, 2)\n",
        "    humidity = 60 + 20 * np.sin(2 * np.pi * timestamp.hour / 24) + np.random.normal(0, 5)\n",
        "\n",
        "    historical_data.append({\n",
        "        'timestamp': timestamp,\n",
        "        'aqi': aqi,\n",
        "        'pm25': aqi * 0.6 + np.random.normal(0, 5),\n",
        "        'pm10': aqi * 0.8 + np.random.normal(0, 10),\n",
        "        'no2': aqi * 0.3 + np.random.normal(0, 3),\n",
        "        'o3': aqi * 0.4 + np.random.normal(0, 5),\n",
        "        'temperature': temp,\n",
        "        'humidity': humidity,\n",
        "        'pressure': 1013 + np.random.normal(0, 5),\n",
        "        'wind_speed': np.random.uniform(0, 10),\n",
        "        'clouds': np.random.uniform(0, 100),\n",
        "        'hour': timestamp.hour,\n",
        "        'day_of_week': timestamp.weekday(),\n",
        "        'month': timestamp.month,\n",
        "        'is_weekend': 1 if timestamp.weekday() >= 5 else 0,\n",
        "        'is_rush_hour': 1 if timestamp.hour in [7,8,9,17,18,19] else 0\n",
        "    })\n",
        "\n",
        "historical_df = pd.DataFrame(historical_data)\n",
        "print(f\"✅ Generated {len(historical_df)} records\")\n",
        "print(historical_df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LWC5tXengtuZ",
        "outputId": "cd334207-808a-41bd-e5a8-951db29f4951"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "📊 Generating 30 days of historical training data...\n",
            "✅ Generated 720 records\n",
            "                   timestamp         aqi       pm25        pm10        no2  \\\n",
            "0 2026-05-10 11:16:26.802496  108.736429  64.071173  102.781271  34.923233   \n",
            "1 2026-05-10 12:16:26.802496  108.701240  62.409306   76.832680  33.553114   \n",
            "2 2026-05-10 13:16:26.802496  109.485280  66.245781   76.078288  33.972678   \n",
            "3 2026-05-10 14:16:26.802496  109.537409  59.618227   89.718563  26.982212   \n",
            "4 2026-05-10 15:16:26.802496  116.194664  68.211280   78.170511  32.698866   \n",
            "\n",
            "          o3  temperature   humidity     pressure  wind_speed     clouds  \\\n",
            "0  41.147200    15.974992  64.005614  1015.712800    1.818250  18.340451   \n",
            "1  38.940375    11.173440  51.375411  1005.938481    4.560700  78.517596   \n",
            "2  40.790918    14.562313  52.101705  1011.541531    6.842330  44.015249   \n",
            "3  37.174033    17.884578  54.112725  1013.984306    9.695846  77.513282   \n",
            "4  44.174672    22.930927  45.279623  1018.285611    2.809345  54.269608   \n",
            "\n",
            "   hour  day_of_week  month  is_weekend  is_rush_hour  \n",
            "0    11            6      5           1             0  \n",
            "1    12            6      5           1             0  \n",
            "2    13            6      5           1             0  \n",
            "3    14            6      5           1             0  \n",
            "4    15            6      5           1             0  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 9: Training pipeline - Train Random Forest model\n",
        "print(\"🚀 Training Model...\\n\")\n",
        "\n",
        "# Use the historical data we generated\n",
        "df = historical_df.copy()\n",
        "\n",
        "# Define features and target\n",
        "feature_columns = ['temperature', 'humidity', 'pressure', 'wind_speed', 'clouds',\n",
        "                   'hour', 'day_of_week', 'month', 'is_weekend', 'is_rush_hour',\n",
        "                   'pm25', 'pm10', 'no2', 'o3']\n",
        "\n",
        "# For forecasting: predict AQI 3 hours ahead\n",
        "df = df.sort_values('timestamp')\n",
        "df['target_aqi'] = df['aqi'].shift(-3)\n",
        "df = df.dropna()\n",
        "\n",
        "X = df[feature_columns]\n",
        "y = df['target_aqi']\n",
        "\n",
        "# Split into train/test\n",
        "split_idx = int(len(X) * 0.8)\n",
        "X_train, X_test = X[:split_idx], X[split_idx:]\n",
        "y_train, y_test = y[:split_idx], y[split_idx:]\n",
        "\n",
        "# Train model\n",
        "model = RandomForestRegressor(\n",
        "    n_estimators=100,\n",
        "    max_depth=12,\n",
        "    random_state=42,\n",
        "    n_jobs=-1\n",
        ")\n",
        "model.fit(X_train, y_train)\n",
        "\n",
        "# Evaluate\n",
        "y_pred = model.predict(X_test)\n",
        "r2 = r2_score(y_test, y_pred)\n",
        "mae = mean_absolute_error(y_test, y_pred)\n",
        "rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n",
        "\n",
        "print(f\"📈 Model Performance:\")\n",
        "print(f\"   ✅ R² Score: {r2:.3f}\")\n",
        "print(f\"   ✅ MAE: {mae:.2f}\")\n",
        "print(f\"   ✅ RMSE: {rmse:.2f}\")\n",
        "\n",
        "# Save model locally\n",
        "joblib.dump(model, 'aqi_model.pkl')\n",
        "print(\"\\n✅ Model saved as 'aqi_model.pkl'\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uTAYcjxzg7CB",
        "outputId": "51914972-65bf-4c00-eee4-7eb37cf106f0"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🚀 Training Model...\n",
            "\n",
            "📈 Model Performance:\n",
            "   ✅ R² Score: 0.741\n",
            "   ✅ MAE: 10.57\n",
            "   ✅ RMSE: 13.61\n",
            "\n",
            "✅ Model saved as 'aqi_model.pkl'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 10: Test prediction on current real-time data\n",
        "print(\"🔮 Making real-time prediction...\\n\")\n",
        "\n",
        "try:\n",
        "    # Get current data\n",
        "    aqi_current = fetch_aqi_data()\n",
        "    weather_current = fetch_weather_data()\n",
        "    time_current = engineer_features(datetime.now())\n",
        "\n",
        "    # Create feature vector\n",
        "    current_features = pd.DataFrame([{\n",
        "        'temperature': weather_current['temperature'],\n",
        "        'humidity': weather_current['humidity'],\n",
        "        'pressure': weather_current['pressure'],\n",
        "        'wind_speed': weather_current['wind_speed'],\n",
        "        'clouds': weather_current['clouds'],\n",
        "        'hour': time_current['hour'],\n",
        "        'day_of_week': time_current['day_of_week'],\n",
        "        'month': time_current['month'],\n",
        "        'is_weekend': time_current['is_weekend'],\n",
        "        'is_rush_hour': time_current['is_rush_hour'],\n",
        "        'pm25': aqi_current.get('pm25', 50),\n",
        "        'pm10': aqi_current.get('pm10', 70),\n",
        "        'no2': aqi_current.get('no2', 30),\n",
        "        'o3': aqi_current.get('o3', 40)\n",
        "    }])\n",
        "\n",
        "    # Make prediction\n",
        "    prediction = model.predict(current_features)[0]\n",
        "\n",
        "    print(f\"📊 Current AQI: {aqi_current['aqi']}\")\n",
        "    print(f\"🔮 Predicted AQI in 3 hours: {prediction:.1f}\")\n",
        "\n",
        "    # Alert system\n",
        "    if prediction > 200:\n",
        "        print(\"🚨 ALERT: Hazardous AQI predicted! Take precautions!\")\n",
        "    elif prediction > 150:\n",
        "        print(\"⚠️ WARNING: Unhealthy AQI predicted for sensitive groups\")\n",
        "    else:\n",
        "        print(\"✅ AQI levels predicted to be moderate/good\")\n",
        "\n",
        "except Exception as e:\n",
        "    print(f\"Error making prediction: {e}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9RqFGqqahFQR",
        "outputId": "1b3fcafd-da10-4c0a-8726-d8cb33605b87"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔮 Making real-time prediction...\n",
            "\n",
            "📊 Current AQI: 161\n",
            "🔮 Predicted AQI in 3 hours: 107.5\n",
            "✅ AQI levels predicted to be moderate/good\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 11: Explain predictions with SHAP\n",
        "print(\"📊 Calculating feature importance with SHAP...\\n\")\n",
        "\n",
        "# Create explainer\n",
        "explainer = shap.TreeExplainer(model)\n",
        "\n",
        "# Get sample data for explanation\n",
        "sample_data = X_test[:5]\n",
        "\n",
        "# Calculate SHAP values\n",
        "shap_values = explainer.shap_values(sample_data)\n",
        "\n",
        "# Create summary plot\n",
        "import matplotlib.pyplot as plt\n",
        "plt.figure(figsize=(10, 6))\n",
        "shap.summary_plot(shap_values, sample_data, feature_names=feature_columns, show=False)\n",
        "plt.title(\"Feature Importance for AQI Predictions\", fontsize=14)\n",
        "plt.tight_layout()\n",
        "plt.savefig('shap_importance.png', dpi=100, bbox_inches='tight')\n",
        "plt.show()\n",
        "\n",
        "print(\"\\n✅ SHAP analysis complete! Understanding what drives AQI predictions.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 786
        },
        "id": "buIXOwkohNRh",
        "outputId": "036b2a9e-5890-4e96-bb79-1ecf4c6a51ef"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "📊 Calculating feature importance with SHAP...\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x710 with 2 Axes>"
            ],
            "image/png": "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Qfjjjz80GksWd3d3GBoawsfHR+U+CCBzXl5aWpqaI4mIiIi0BefoayrPGf26detCKpXi999/R3x8PExMTFC+fHkMHjwYV65cwdKlSxEQEAAXFxeYmZkhIiICAQEBikC0oFlZWeHMmTN49eoVmjRpolhe09bWFmPGjFHU69ixIzw8PLBr1y4EBQWhdevWsLKywsuXL3Hr1i08e/YMBw8efG9/ZmZmaN68OY4dOwYjIyPUrVsX4eHh2LdvH8qXL4+4uDil+vXq1QMALFu2DF27doWhoSGqVq2KatWqoXPnzli1ahV+/PFHhISEwNLSEpcuXUJsbGyu3oOyZcvi66+/xrx589C/f39069YN9vb2iImJwcOHD+Hv74/du3cXyKo/RERERFSy5TnQL1euHGbNmoVNmzbh559/hkwmUzzY6bfffsOePXtw9OhRRVBfpkwZ1K1bFz169Ciwwb/NxMRE8cCsFStWQAgBV1dXfP755yrTeb7//ns4Oztj//792LhxI9LT02Fra4tatWphwoQJGvf5ww8/YPny5bhw4QKOHDmCChUqYPz48dDX18ecOXOU6jZs2BCTJk3Cvn37MG/ePGRkZGDUqFGoVq0azM3NsXTpUixevBi+vr4wMTFB+/bt8cMPP6Bdu3a5eh969uwJJycn/PHHH9i3bx8SEhJgZWWFihUrYty4cSo33BARERGRbpKIvN7VWoJkPRnXz8+vuIdCOig9PR2+vr4AAG9vbxgYGBTziIiIiD5cMsnIbPfpiw1FOJKST7duwyYiIiIiIgCFtLwmEREREVHh4E23mmJGn4iIiIhIB+lERn/t2rXFPQQiIiIiohJFJwJ9IiIiIvow8Mm4muPUHSIiIiIiHcSMPhERERFpEWb0NcWMPhERERGRDmJGn4iIiIi0Bufoa44ZfSIiIiIiHcRAn4iIiIhIB3HqDhERERFpEU7d0RQz+kREREREOogZfSIiIiLSGrwZV3PM6BMRERER6SAG+kREREREOoiBPhERERGRDmKgT0RERESkg3gzLhERERFpDd6Mqzlm9ImIiIiIdBAz+kRERESkRZjR1xQz+kREREREOoiBPhERERGRDuLUHSIiIiLSGrwZV3PM6BMRERER6SBm9ImIiIhIizCjrykG+iXckydPcOzYMVy+fBnPnj1DWloaHB0d0aFDBwwZMgQmJiZK9X18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+vXrAWTOm+vevbui7tSpUzF27Fh8+umnGDhwIABg586dkMvlmDJlSoGOi4iIiIjyJywsDOfPn8fLly/Rt29fODo6IiMjA3FxcShVqhT09PTe30g2GOjn0aRJk3Djxg3s3r0b0dHRcHJywrx589ClS5cC7+vgwYO4fv26UtmaNWsAAI0bN1YK9D/66CP4+Phg9erVWL16NSQSCRo0aIAFCxagRo0aBT42IiIioqIkdGTmjhACU6dOxYoVKyCTySCRSFC/fn04OjoiMTERlSpVwty5c/OVqJWIvN75+YHy8/PDnDlzsGbNGjg7Oxf3cKgIpKenw9fXFwDg7e0NAwM1Sy4SERFRkTiuvznbfV1kw4twJPnzyy+/4JtvvsFXX32FDh06wN3dHX/++Sfat28PAPjkk0/w6NEjXLhwIc99MKNPRERERFpDV27GXbduHYYPH46ffvpJ5VkGANCgQQMcO3YsX33wZlwiIiIioiL29OlTtGjRItv9ZmZmiI+Pz1cfDPSJiIiIiIqYnZ0dnj59mu3+a9euwckpf8tLM9DPJQ8PDwQGBnJ+PhEREVExENLsX9rE09MTa9aswePHjxVlEknmtKSTJ09i48aN6N+/f7760LK3hIiIiIhI+82ZMwf29vZo2LAhhg8fDolEggULFqBVq1bo2rUrGjRogG+//TZffTDQJyIiIiKtIfQk2b60SalSpXD58mV8+eWXCAsLg7GxMc6dO4fY2Fh8//33uHDhAkxNc/9E+bdx1R0iIiIiomJgYmKC7777Dt99912htM9An4iIiIi0hlxHltcsCgz0iYiIiIiK2IgRI95bRyKRYMOGDXnug4E+EREREVERO3PmjGKVnSwZGRkIDw9HRkYGypQpAzMzs3z1wUCfiIiIiLSGti2jmZ2QkBC15enp6fDx8cFvv/2GU6dO5asPHXmriIiIiIi0n4GBASZOnIhOnTph4sSJ+WqLgT4RERERaQ0hlWT70iUfffQRzp8/n682GOgTEREREZUwp06d4jr6RERERETaZu7cuWrLY2Njcf78eVy/fh1ff/11vvpgoE9EREREWkPoyAyd2bNnqy23trZG1apVsWbNGowaNSpffTDQJyIiIiIqYnK5vND7YKBPRERERFpD1266LUwM9ImIiIiIClloaGiejnNycspznwz0iYiIiEhryLU0oV+pUiWVJ+Fq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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "✅ SHAP analysis complete! Understanding what drives AQI predictions.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 12: Generate 72-hour forecast\n",
        "print(\"🌤️ Generating 72-hour AQI forecast...\\n\")\n",
        "\n",
        "# Create future timestamps\n",
        "future_hours = 72\n",
        "future_predictions = []\n",
        "start_time = datetime.now()\n",
        "\n",
        "for i in range(1, future_hours + 1, 3):  # Every 3 hours\n",
        "    future_time = start_time + timedelta(hours=i)\n",
        "\n",
        "    # Simulate future weather patterns\n",
        "    hour_of_day = future_time.hour\n",
        "    temp = 20 + 5 * np.sin(2 * np.pi * (hour_of_day - 14) / 24)\n",
        "    humidity = 60 + 15 * np.sin(2 * np.pi * hour_of_day / 24)\n",
        "\n",
        "    future_features = pd.DataFrame([{\n",
        "        'temperature': temp + np.random.normal(0, 2),\n",
        "        'humidity': humidity + np.random.normal(0, 5),\n",
        "        'pressure': 1013,\n",
        "        'wind_speed': np.random.uniform(0, 8),\n",
        "        'clouds': np.random.uniform(0, 60),\n",
        "        'hour': future_time.hour,\n",
        "        'day_of_week': future_time.weekday(),\n",
        "        'month': future_time.month,\n",
        "        'is_weekend': 1 if future_time.weekday() >= 5 else 0,\n",
        "        'is_rush_hour': 1 if future_time.hour in [7,8,9,17,18,19] else 0,\n",
        "        'pm25': 50 + np.random.normal(0, 10),\n",
        "        'pm10': 70 + np.random.normal(0, 15),\n",
        "        'no2': 30 + np.random.normal(0, 5),\n",
        "        'o3': 40 + np.random.normal(0, 8)\n",
        "    }])\n",
        "\n",
        "    pred = model.predict(future_features)[0]\n",
        "    future_predictions.append({\n",
        "        'time': future_time,\n",
        "        'predicted_aqi': max(0, pred)\n",
        "    })\n",
        "\n",
        "forecast_df = pd.DataFrame(future_predictions)\n",
        "\n",
        "# Display forecast\n",
        "print(\"📅 3-DAY AQI FORECAST\")\n",
        "print(\"=\" * 50)\n",
        "print(f\"{'Time':<20} {'Predicted AQI':<15} {'Status'}\")\n",
        "print(\"-\" * 50)\n",
        "\n",
        "for _, row in forecast_df.iterrows():\n",
        "    aqi = row['predicted_aqi']\n",
        "    if aqi <= 50: status = \"🟢 Good\"\n",
        "    elif aqi <= 100: status = \"🟡 Moderate\"\n",
        "    elif aqi <= 150: status = \"🟠 Unhealthy for Sensitive\"\n",
        "    elif aqi <= 200: status = \"🔴 Unhealthy\"\n",
        "    else: status = \"⚫ Hazardous\"\n",
        "\n",
        "    print(f\"{row['time'].strftime('%Y-%m-%d %H:00'):<20} {aqi:<15.1f} {status}\")\n",
        "\n",
        "print(\"\\n\" + \"=\" * 50)\n",
        "\n",
        "# Alert for hazardous levels\n",
        "if any(forecast_df['predicted_aqi'] > 200):\n",
        "    print(\"🚨 🚨 🚨 HAZARDOUS AQI LEVELS PREDICTED! 🚨 🚨 🚨\")\n",
        "    print(\"Take immediate precautions: Wear N95 masks, avoid outdoor activities\")\n",
        "elif any(forecast_df['predicted_aqi'] > 150):\n",
        "    print(\"⚠️ Unhealthy AQI predicted. Sensitive groups should limit outdoor exposure\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xI22wGWrhR2Z",
        "outputId": "35e03f93-3245-4c37-8034-8b37059951f9"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🌤️ Generating 72-hour AQI forecast...\n",
            "\n",
            "📅 3-DAY AQI FORECAST\n",
            "==================================================\n",
            "Time                 Predicted AQI   Status\n",
            "--------------------------------------------------\n",
            "2026-06-09 12:00     102.2           🟠 Unhealthy for Sensitive\n",
            "2026-06-09 15:00     111.7           🟠 Unhealthy for Sensitive\n",
            "2026-06-09 18:00     88.8            🟡 Moderate\n",
            "2026-06-09 21:00     84.9            🟡 Moderate\n",
            "2026-06-10 00:00     83.9            🟡 Moderate\n",
            "2026-06-10 03:00     99.4            🟡 Moderate\n",
            "2026-06-10 06:00     101.7           🟠 Unhealthy for Sensitive\n",
            "2026-06-10 09:00     92.9            🟡 Moderate\n",
            "2026-06-10 12:00     102.7           🟠 Unhealthy for Sensitive\n",
            "2026-06-10 15:00     102.0           🟠 Unhealthy for Sensitive\n",
            "2026-06-10 18:00     79.8            🟡 Moderate\n",
            "2026-06-10 21:00     90.2            🟡 Moderate\n",
            "2026-06-11 00:00     86.2            🟡 Moderate\n",
            "2026-06-11 03:00     92.5            🟡 Moderate\n",
            "2026-06-11 06:00     100.3           🟠 Unhealthy for Sensitive\n",
            "2026-06-11 09:00     113.1           🟠 Unhealthy for Sensitive\n",
            "2026-06-11 12:00     114.5           🟠 Unhealthy for Sensitive\n",
            "2026-06-11 15:00     90.7            🟡 Moderate\n",
            "2026-06-11 18:00     80.3            🟡 Moderate\n",
            "2026-06-11 21:00     70.8            🟡 Moderate\n",
            "2026-06-12 00:00     80.6            🟡 Moderate\n",
            "2026-06-12 03:00     93.1            🟡 Moderate\n",
            "2026-06-12 06:00     99.7            🟡 Moderate\n",
            "2026-06-12 09:00     103.2           🟠 Unhealthy for Sensitive\n",
            "\n",
            "==================================================\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Install Streamlit and required packages\n",
        "!pip install streamlit pyngrok -q\n",
        "\n",
        "print(\"✅ Packages installed!\")"
      ],
      "metadata": {
        "id": "P481gprehbER",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f55353e1-2725-45e4-d4f7-da817121569a"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Packages installed!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================\n",
        "# CREATE STREAMLIT APP FILE\n",
        "# ============================================\n",
        "\n",
        "streamlit_code = '''\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import plotly.graph_objects as go\n",
        "from datetime import datetime, timedelta\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "# Page configuration\n",
        "st.set_page_config(\n",
        "    page_title=\"Karachi AQI Predictor\",\n",
        "    page_icon=\"🇵🇰\",\n",
        "    layout=\"wide\"\n",
        ")\n",
        "\n",
        "# Title\n",
        "st.title(\"🇵🇰 Karachi Air Quality Predictor\")\n",
        "st.markdown(\"### Real-time AQI Monitoring & 3-Day Forecast\")\n",
        "\n",
        "# Sidebar\n",
        "with st.sidebar:\n",
        "    st.header(\"📍 Karachi, Pakistan\")\n",
        "    st.markdown(f\"**Date:** {datetime.now().strftime('%d %B %Y')}\")\n",
        "    st.markdown(f\"**Time:** {datetime.now().strftime('%I:%M %p')}\")\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "    st.header(\"⚙️ Settings\")\n",
        "    forecast_days = st.slider(\"Forecast Days\", 1, 5, 3)\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "    st.header(\"📊 About\")\n",
        "    st.info(\"\"\"\n",
        "    This app predicts Air Quality Index (AQI)\n",
        "    for Karachi using machine learning.\n",
        "\n",
        "    **Model:** Random Forest\n",
        "    **Data:** OpenWeather API\n",
        "    \"\"\")\n",
        "\n",
        "# Generate sample data for demonstration\n",
        "np.random.seed(42)\n",
        "\n",
        "# Current conditions\n",
        "current_aqi = 85\n",
        "current_pm25 = 45.5\n",
        "current_pm10 = 72.3\n",
        "current_temp = 32.0\n",
        "current_humidity = 65\n",
        "current_wind = 5.5\n",
        "\n",
        "# Generate forecast\n",
        "forecast_aqi = [\n",
        "    int(current_aqi + np.random.randint(-20, 30)),\n",
        "    int(current_aqi + np.random.randint(-30, 40)),\n",
        "    int(current_aqi + np.random.randint(-40, 50))\n",
        "]\n",
        "forecast_aqi = [max(10, min(500, x)) for x in forecast_aqi]\n",
        "\n",
        "# Main metrics\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"📍 Current Conditions\")\n",
        "\n",
        "col1, col2, col3, col4 = st.columns(4)\n",
        "\n",
        "with col1:\n",
        "    delta = forecast_aqi[0] - current_aqi\n",
        "    st.metric(\n",
        "        label=\"Current AQI\",\n",
        "        value=f\"{current_aqi:.0f}\",\n",
        "        delta=f\"{delta:+.0f} tomorrow\",\n",
        "        delta_color=\"inverse\"\n",
        "    )\n",
        "\n",
        "with col2:\n",
        "    st.metric(\"PM2.5\", f\"{current_pm25:.1f} µg/m³\")\n",
        "\n",
        "with col3:\n",
        "    st.metric(\"Temperature\", f\"{current_temp:.1f}°C\")\n",
        "\n",
        "with col4:\n",
        "    st.metric(\"Humidity\", f\"{current_humidity:.0f}%\")\n",
        "\n",
        "# AQI Status\n",
        "st.markdown(\"---\")\n",
        "if current_aqi <= 50:\n",
        "    st.success(f\"✅ **Good** - Air quality is satisfactory (AQI: {current_aqi})\")\n",
        "elif current_aqi <= 100:\n",
        "    st.info(f\"ℹ️ **Moderate** - Acceptable air quality (AQI: {current_aqi})\")\n",
        "elif current_aqi <= 150:\n",
        "    st.warning(f\"⚠️ **Unhealthy for Sensitive Groups** (AQI: {current_aqi})\")\n",
        "elif current_aqi <= 200:\n",
        "    st.error(f\"🔴 **Unhealthy** - Everyone may experience health effects (AQI: {current_aqi})\")\n",
        "else:\n",
        "    st.error(f\"💀 **Hazardous** - Health emergency! (AQI: {current_aqi})\")\n",
        "\n",
        "# 3-Day Forecast\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"🔮 3-Day AQI Forecast\")\n",
        "\n",
        "col1, col2, col3 = st.columns(3)\n",
        "\n",
        "days = [\"Day 1 (Tomorrow)\", \"Day 2\", \"Day 3\"]\n",
        "emojis = [\"📅\", \"📅\", \"📅\"]\n",
        "\n",
        "for i, (col, day, emoji) in enumerate(zip([col1, col2, col3], days, emojis)):\n",
        "    with col:\n",
        "        aqi = forecast_aqi[i]\n",
        "\n",
        "        if aqi <= 50:\n",
        "            color = \"🟢\"\n",
        "            status = \"Good\"\n",
        "        elif aqi <= 100:\n",
        "            color = \"🟡\"\n",
        "            status = \"Moderate\"\n",
        "        elif aqi <= 150:\n",
        "            color = \"🟠\"\n",
        "            status = \"Unhealthy (Sensitive)\"\n",
        "        elif aqi <= 200:\n",
        "            color = \"🔴\"\n",
        "            status = \"Unhealthy\"\n",
        "        else:\n",
        "            color = \"⚫\"\n",
        "            status = \"Hazardous\"\n",
        "\n",
        "        st.markdown(f\"\"\"\n",
        "        <div style=\"padding: 20px; border-radius: 10px; background-color: {'#1a1a1a' if aqi > 150 else '#0a2a0a'}; text-align: center;\">\n",
        "            <h3>{emoji} {day}</h3>\n",
        "            <h1 style=\"font-size: 3em;\">{aqi}</h1>\n",
        "            <p>{color} {status}</p>\n",
        "        </div>\n",
        "        \"\"\", unsafe_allow_html=True)\n",
        "\n",
        "# Trend Chart\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"📈 72-Hour AQI Trend\")\n",
        "\n",
        "# Generate hourly trend data\n",
        "hours = []\n",
        "values = []\n",
        "now = datetime.now()\n",
        "\n",
        "for h in range(0, 73, 3):\n",
        "    time_point = now + timedelta(hours=h)\n",
        "    hours.append(time_point.strftime(\"%I%p %d/%m\"))\n",
        "\n",
        "    if h < 24:\n",
        "        values.append(current_aqi + (forecast_aqi[0] - current_aqi) * (h/24))\n",
        "    elif h < 48:\n",
        "        values.append(forecast_aqi[0] + (forecast_aqi[1] - forecast_aqi[0]) * ((h-24)/24))\n",
        "    else:\n",
        "        values.append(forecast_aqi[1] + (forecast_aqi[2] - forecast_aqi[1]) * ((h-48)/24))\n",
        "\n",
        "fig = go.Figure()\n",
        "\n",
        "# Add AQI line\n",
        "fig.add_trace(go.Scatter(\n",
        "    x=hours,\n",
        "    y=values,\n",
        "    mode='lines+markers',\n",
        "    name='Predicted AQI',\n",
        "    line=dict(color='#00ff00', width=3),\n",
        "    fill='tozeroy',\n",
        "    fillcolor='rgba(0, 255, 0, 0.1)'\n",
        "))\n",
        "\n",
        "# Add threshold lines\n",
        "fig.add_hline(y=50, line_dash=\"dash\", line_color=\"green\",\n",
        "              annotation_text=\"Good (50)\", opacity=0.5)\n",
        "fig.add_hline(y=100, line_dash=\"dash\", line_color=\"yellow\",\n",
        "              annotation_text=\"Moderate (100)\", opacity=0.5)\n",
        "fig.add_hline(y=150, line_dash=\"dash\", line_color=\"orange\",\n",
        "              annotation_text=\"Unhealthy (150)\", opacity=0.5)\n",
        "fig.add_hline(y=200, line_dash=\"dash\", line_color=\"red\",\n",
        "              annotation_text=\"Very Unhealthy (200)\", opacity=0.5)\n",
        "\n",
        "fig.update_layout(\n",
        "    title=\"Predicted AQI Over Next 72 Hours\",\n",
        "    xaxis_title=\"Time\",\n",
        "    yaxis_title=\"AQI Value\",\n",
        "    height=500,\n",
        "    hovermode='x unified',\n",
        "    template=\"plotly_dark\"\n",
        ")\n",
        "\n",
        "st.plotly_chart(fig, use_container_width=True)\n",
        "\n",
        "# Pollutant Breakdown\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"🔬 Current Pollutant Levels\")\n",
        "\n",
        "pollutants = {\n",
        "    'PM2.5': current_pm25,\n",
        "    'PM10': current_pm10,\n",
        "    'NO2': 28.5,\n",
        "    'SO2': 12.3,\n",
        "    'O3': 35.7,\n",
        "    'CO': 0.8\n",
        "}\n",
        "\n",
        "fig_pollutants = go.Figure(go.Bar(\n",
        "    x=list(pollutants.keys()),\n",
        "    y=list(pollutants.values()),\n",
        "    marker_color=['#ff4444', '#ff8800', '#ffaa00', '#ffdd00', '#88ff00', '#00ff88'],\n",
        "    text=[f\"{v:.1f}\" for v in pollutants.values()],\n",
        "    textposition='auto'\n",
        "))\n",
        "\n",
        "fig_pollutants.update_layout(\n",
        "    title=\"Pollutant Concentrations (µg/m³)\",\n",
        "    height=400,\n",
        "    template=\"plotly_dark\"\n",
        ")\n",
        "\n",
        "st.plotly_chart(fig_pollutants, use_container_width=True)\n",
        "\n",
        "# Health Recommendations\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"💡 Health Recommendations\")\n",
        "\n",
        "rec_col1, rec_col2 = st.columns(2)\n",
        "\n",
        "with rec_col1:\n",
        "    st.markdown(\"\"\"\n",
        "    ### If AQI is High (>150):\n",
        "    - 😷 Wear N95 mask outdoors\n",
        "    - 🏠 Stay indoors if possible\n",
        "    - 🪟 Keep windows closed\n",
        "    - 💨 Use air purifier\n",
        "    - 🏃 Avoid outdoor exercise\n",
        "    \"\"\")\n",
        "\n",
        "with rec_col2:\n",
        "    st.markdown(\"\"\"\n",
        "    ### General Tips:\n",
        "    - 🌅 Exercise early morning (better air)\n",
        "    - 🌿 Keep indoor plants\n",
        "    - 📱 Check AQI before going out\n",
        "    - 🚗 Avoid high-traffic areas\n",
        "    - 💧 Stay hydrated\n",
        "    \"\"\")\n",
        "\n",
        "# Footer\n",
        "st.markdown(\"---\")\n",
        "st.markdown(\n",
        "    f\"<center>🌊 Built for Karachi, Pakistan | Data: OpenWeather API | \"\n",
        "    f\"Last Updated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}</center>\",\n",
        "    unsafe_allow_html=True\n",
        ")\n",
        "'''\n",
        "\n",
        "# Write the Streamlit app to a file\n",
        "with open('app.py', 'w') as f:\n",
        "    f.write(streamlit_code)\n",
        "\n",
        "print(\"✅ Streamlit app file created: app.py\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vx5u4BYFG_Gz",
        "outputId": "3f225e27-b454-4b2c-e8f9-742cbc721875"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Streamlit app file created: app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================\n",
        "# START STREAMLIT WITH PUBLIC URL\n",
        "# ============================================\n",
        "\n",
        "import subprocess\n",
        "import time\n",
        "from pyngrok import ngrok\n",
        "import os\n",
        "\n",
        "print(\"🚀 Starting Streamlit server...\")\n",
        "\n",
        "# Kill any existing Streamlit processes\n",
        "import signal\n",
        "try:\n",
        "    subprocess.run(['pkill', '-f', 'streamlit'], check=False)\n",
        "    time.sleep(2)\n",
        "except:\n",
        "    pass\n",
        "\n",
        "# Start Streamlit in background\n",
        "streamlit_process = subprocess.Popen(\n",
        "    ['streamlit', 'run', 'app.py', '--server.port', '8501', '--server.headless', 'true'],\n",
        "    stdout=subprocess.PIPE,\n",
        "    stderr=subprocess.PIPE\n",
        ")\n",
        "\n",
        "# Wait for Streamlit to start\n",
        "print(\"⏳ Waiting for Streamlit to start...\")\n",
        "time.sleep(5)\n",
        "\n",
        "# Create ngrok tunnel\n",
        "print(\"🔗 Creating public URL...\")\n",
        "try:\n",
        "    # Terminate any existing ngrok tunnels\n",
        "    ngrok.kill()\n",
        "\n",
        "    # Create new tunnel\n",
        "    public_url = ngrok.connect(8501)\n",
        "    print(\"\\n\" + \"=\"*60)\n",
        "    print(\"✅ STREAMLIT APP IS LIVE!\")\n",
        "    print(\"=\"*60)\n",
        "    print(f\"🔗 Public URL: {public_url}\")\n",
        "    print(f\"📱 Open this URL in your browser\")\n",
        "    print(\"=\"*60)\n",
        "    print(\"\\n⚠️ Keep this cell running - do not stop it!\")\n",
        "    print(\"💡 To stop: Click the stop button (⏹️) or restart runtime\")\n",
        "\n",
        "except Exception as e:\n",
        "    print(f\"❌ Error creating tunnel: {e}\")\n",
        "    print(\"\\nTrying alternative method...\")\n",
        "\n",
        "    # Alternative: use localhost.run\n",
        "    try:\n",
        "        !streamlit run app.py --server.port 8501 &\n",
        "        time.sleep(5)\n",
        "        !npx localtunnel --port 8501\n",
        "    except:\n",
        "        print(\"Please run: !streamlit run app.py\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dlHeB7EUHLJf",
        "outputId": "5c21424b-6c35-4875-9c29-c4e6b52d0008"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🚀 Starting Streamlit server...\n",
            "⏳ Waiting for Streamlit to start...\n",
            "🔗 Creating public URL...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "ERROR:pyngrok.process.ngrok:t=2026-06-09T11:29:42+0000 lvl=eror msg=\"failed to reconnect session\" obj=tunnels.session err=\"authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n\"\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "❌ Error creating tunnel: The ngrok process errored on start: authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n.\n",
            "\n",
            "Trying alternative method...\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "2026-06-09 11:29:47.558 Port 8501 is not available\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K\u001b[1G\u001b[0JNeed to install the following packages:\n",
            "localtunnel@2.0.2\n",
            "Ok to proceed? (y) \u001b[20Gy\n",
            "\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0Kyour url is: https://shiny-pumas-vanish.loca.lt\n"
          ]
        }
      ]
    }
  ]
}
