# 🏠 House Price Prediction using Linear Regression

A Machine Learning project that predicts house prices based on various property features using the Linear Regression algorithm. This project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment with Streamlit.

## 🌐 Live Demo

🔗 **Application:** https://your-streamlit-app-url.streamlit.app


---

## 📌 Project Overview

The objective of this project is to build a regression model that estimates house prices based on features such as:

- Area
- Number of Bedrooms
- Number of Bathrooms
- Number of Stories
- Main Road Access
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

The model is built using **Scikit-learn's Linear Regression** algorithm.

---

## 🚀 Features

- Data preprocessing and cleaning
- Encoding categorical variables
- Exploratory Data Analysis (EDA)
- Correlation heatmap
- Linear Regression model training
- Model evaluation using MAE, MSE, RMSE, and R² Score
- Interactive house price prediction through Streamlit

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── app.py                      # Streamlit application
├── house_price_model.pkl       # Trained machine learning model
├── Housing.csv                 # Dataset
├── Notebook.ipynb              # Google Colab Notebook
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 📊 Dataset

The dataset contains **545 house records** with **13 input features** and one target variable.

### Input Features

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

### Target Variable

- House Price

---

## 🔄 Machine Learning Workflow

1. Load the dataset
2. Clean and preprocess the data
3. Encode categorical variables
4. Perform Exploratory Data Analysis (EDA)
5. Split the dataset into training and testing sets
6. Train the Linear Regression model
7. Evaluate the model
8. Save the trained model
9. Deploy using Streamlit

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Mean Absolute Error (MAE) | 970,043 |
| Mean Squared Error (MSE) | 1.754 × 10¹² |
| Root Mean Squared Error (RMSE) | 1,324,507 |
| R² Score | **0.653** |

The model explains approximately **65.3%** of the variance in house prices.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

Navigate to the project directory:

```bash
cd House-Price-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Application

The Streamlit application enables users to:

- Enter house details
- Predict house prices instantly
- Estimate property values based on selected features

---

## 📚 Learning Outcomes

This project demonstrates:

- Data preprocessing
- Feature engineering
- Exploratory Data Analysis
- Linear Regression
- Model evaluation
- Machine Learning deployment using Streamlit

---

## 🔮 Future Improvements

- Implement Random Forest Regression
- Use XGBoost for improved accuracy
- Perform hyperparameter tuning
- Add feature scaling and feature selection
- Train on larger datasets
- Deploy with Docker or cloud platforms
- Add interactive visualizations and analytics
