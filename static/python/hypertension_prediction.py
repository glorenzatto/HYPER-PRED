import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class HypertensionPredictionModel:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        df = pd.read_excel(self.file_path)
        return df

    def train_model(self, df):
        # Remove rows where the 'Percentage' column contains NaN
        df = df.dropna(subset=['Percentage'])

        # Separate the data into features (X) and target (y)
        X = df[['Filter', 'Filter Range']]
        y = df['Percentage']

        # OneHotEncode for categorical columns
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), ['Filter', 'Filter Range'])
            ])

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=48)

        # Create and train the model
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=48))
        ])

        model.fit(X_train, y_train)

        # Evaluate the model
        self.evaluate_model(model, X_test, y_test)

        return model

    # Function to evaluate the model
    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        # print(f"Mean Squared Error (MSE): {mse}")
        # print(f"R² Score: {r2}")

    # Function to predict hypertension risk
    def predict_hypertension_risk(self, model, age, gender, race):

        patient_data = pd.DataFrame({
            'Filter': ['Age', 'Gender', 'Race'],
            'Filter Range': [age, gender, race]
        })

        # Prediction for each individual filter
        predictions = model.predict(patient_data)

        # Aggregate the predictions (mean)
        risk_percentage = np.mean(predictions)

        return risk_percentage

    # Function to determine the color based on the percentage
    def get_color(self, percentage):
        if percentage <= 5:
            return 'green'
        elif percentage <= 10:
            return '#66ff00'
        elif percentage <= 15:
            return '#ccff00'
        elif percentage <= 20:
            return '#ffff00'
        elif percentage <= 25:
            return '#ffcc00'
        elif percentage <= 30:
            return '#ff9900'
        elif percentage <= 35:
            return '#ff6600'
        elif percentage <= 40:
            return '#ff3300'
        elif percentage <= 45:
            return '#ff0000'
        else:
            return 'darkred'

    def get_risk_percentage_and_color(self, age, gender, race):
        df = self.load_data()
        model = self.train_model(df)

        risk = self.predict_hypertension_risk(model, age, gender, race)
        risk = round(risk, 2)

        color = self.get_color(risk)

        return risk, color
