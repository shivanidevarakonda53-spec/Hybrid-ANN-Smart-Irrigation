# Hybrid ANN-Based Smart Irrigation System

## Project Overview

The **Hybrid ANN-Based Smart Irrigation System** is an AI-powered application designed to support efficient water management in agriculture.

It uses a Hybrid Artificial Neural Network (ANN) model to predict irrigation requirements based on environmental conditions, crop information, field area, and previous irrigation data.

The system aims to reduce unnecessary water usage and support smarter irrigation decisions.

## Objectives

- Predict the irrigation requirement of crops.
- Reduce unnecessary water consumption.
- Use weather and crop-related information for prediction.
- Support data-driven irrigation decisions.
- Provide an easy-to-use web-based interface.

## Key Features

- AI-based irrigation requirement prediction.
- Hybrid ANN machine learning model.
- Python-based AI prediction service.
- Spring Boot web application.
- MySQL database integration.
- Irrigation knowledge support through a chatbot.

## Technologies Used

| Component | Technology |
|---|---|
| Programming Languages | Python, Java |
| Machine Learning | Artificial Neural Network (ANN) |
| AI Service | FastAPI |
| Backend | Spring Boot |
| Database | MySQL |
| Build Tool | Maven |
| Version Control | Git and GitHub |

## System Architecture

The project consists of two main components:

1. **AI Service:** Processes input data and uses the trained ANN model to predict irrigation requirements.
2. **Web Application:** Provides the application interface and connects with the AI service.

## Input Parameters

The prediction model uses information such as:

- Temperature
- Humidity
- Rainfall
- Wind speed
- Crop type
- Crop growth stage
- Field area
- Previous irrigation amount

## Prediction Output

The model classifies irrigation requirements into three categories:

- Low
- Medium
- High

## Project Structure

```text
Hybrid-ANN-Smart-Irrigation/
│
├── ai-service/
│   ├── api.py
│   ├── train_hybrid_ann.py
│   ├── prediction_service.py
│   ├── hybrid_ann_model.pkl
│   ├── requirements.txt
│   └── documents/
│
├── src/
│   └── main/
│       ├── java/
│       └── resources/
│
├── pom.xml
├── .gitignore
└── README.md
```

## Future Enhancements

- Real-time soil moisture monitoring.
- Weather forecast integration.
- IoT-based irrigation automation.
- Crop-specific irrigation recommendations.
- Multilingual voice-based assistance.

## Project Goal

To develop an intelligent irrigation support system that helps farmers make better irrigation decisions while conserving water.

---

**Project Name:** Hybrid ANN-Based Smart Irrigation System

**Domain:** Artificial Intelligence and Machine Learning

**Repository:** [GitHub – Hybrid ANN Smart Irrigation](https://github.com/shivanidevarakonda53-spec/Hybrid-ANN-Smart-Irrigation)