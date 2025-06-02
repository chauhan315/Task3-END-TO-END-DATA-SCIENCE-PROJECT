*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: ANKUR SINGH CHAUHAN

*INTERN ID*: CT12WV42

*DOMAIN*: DATA SCIENCE

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH

*OUTPUT* : ![Image](https://github.com/user-attachments/assets/a0b80eaf-c292-48f4-b940-ed3159f801ee)

# Personality Classification Web App

Welcome to the **Personality Classification Web App** — a complete end-to-end data science project that predicts whether a person is an **Extrovert** or **Introvert** based on their social behavior and personal habits. This project combines data preprocessing, machine learning modeling, and a user-friendly FastAPI web interface, and is fully deployed and accessible online.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Dataset](#dataset)  
- [Data Preprocessing](#data-preprocessing)  
- [Modeling](#modeling)  
- [API & Web Interface](#api--web-interface)  
- [How to Run Locally](#how-to-run-locally)  
- [Deployment](#deployment)  
- [Technologies Used](#technologies-used)  
- [Future Work](#future-work)  
- [Contact](#contact)

---

## Project Overview

Personality traits can often be inferred by analyzing patterns in an individual's lifestyle, social habits, and preferences. This project focuses on classifying users into two personality types:

- **Extrovert**: Individuals who are outgoing, social, and energized by social interactions.  
- **Introvert**: Individuals who prefer solitude, smaller social circles, and find social events draining.

Using a labeled dataset containing features like time spent alone, fear of stages, social event attendance, and others, the project develops a robust machine learning model to classify personality types accurately.

The model is wrapped in a FastAPI backend with an interactive HTML form frontend, allowing users to input their data and receive instant personality classification.

---

## Dataset

The dataset used consists of the following features:

| Feature                    | Description                                      | Data Type    |
|----------------------------|------------------------------------------------|--------------|
| `Time_spent_Alone`         | Hours spent alone daily (scale 0-10)            | Numeric      |
| `Stage_fear`               | Fear of public speaking ('yes' or 'no')         | Categorical  |
| `Social_event_attendance`  | Frequency of attending social events (0-10)     | Numeric      |
| `Going_outside`            | Frequency of going outside (0-10)                | Numeric      |
| `Drained_after_socializing`| Whether the person feels drained after socializing ('yes' or 'no') | Categorical  |
| `Friends_circle_size`      | Number of close friends                            | Numeric      |
| `Post_frequency`           | Frequency of posting on social media (0-10)     | Numeric      |
| `Personality`              | Target variable: Extrovert or Introvert          | Categorical  |

The dataset contained some missing values and categorical data that required preprocessing before modeling.

---

## Data Preprocessing

To prepare the data for machine learning:

- **Handling Missing Values**:  
  Missing numeric values were imputed using median imputation, which is robust to outliers.  
  Missing categorical values were imputed with the most frequent category.

- **Encoding Categorical Variables**:  
  Categorical features like `Stage_fear` and `Drained_after_socializing` were encoded into numerical form using `OrdinalEncoder` to make them usable by ML algorithms.

- **Saving Preprocessors**:  
  All preprocessing objects (imputers, encoders) were saved as `.pkl` files to ensure consistent transformation both during training and inference.

---

## Modeling

Two popular machine learning models were trained and compared:

1. **Random Forest Classifier**  
2. **XGBoost Classifier**

Both models performed well, but the **Random Forest Classifier** achieved slightly better accuracy on the validation set, so it was chosen for deployment.

The model was trained on preprocessed data, saved using `joblib`, and loaded during API runtime for predictions.

---

## API & Web Interface

The backend is built with **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python.

- **Endpoints**:  
  - `/` : Serves the home page with the personality prediction form.  
  - `/predict` : Receives form data via POST, applies preprocessing, runs the model, and returns the predicted personality.

- **Frontend**:  
  A simple HTML form allows users to input their details such as time spent alone, stage fear, and more. Results are displayed on the same page.

- **Styling**:  
  The form includes embedded CSS to ensure a clean and user-friendly UI.

- **Input Validation**:  
  FastAPI's Pydantic models validate the input data formats before prediction to maintain robustness.

---

## How to Run Locally

If you want to run this project on your local machine, follow these steps:

### Prerequisites:

- Python 3.8+ installed
- Git installed (optional but recommended)

### Clone the repo:

```bash
git clone https://github.com/yourusername/personality-classification.git
cd personality-classification

### Deployment
- This app is deployed and publicly accessible at:
- https://task3-end-to-end-data-science-project.onrender.com

Feel free to try it out live! Enter your details and see your predicted personality type instantly.

- The deployment was done using Render, a free cloud platform for hosting web apps. The backend FastAPI app, along with all the saved models and preprocessors, was uploaded and configured on Render for easy access without needing to run locally.
