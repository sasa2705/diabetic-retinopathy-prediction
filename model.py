import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data(file_path):
    """Load and preprocess the dataset."""
    df = pd.read_csv(file_path)
    # Convert prognosis to binary (0 or 1)
    df['prognosis'] = df['prognosis'].map({'no_retinopathy': 0, 'retinopathy': 1})
    return df

def preprocess_data(df):
    """Preprocess the data for model training."""
    # Select features and target
    X = df[['age', 'systolic_bp', 'diastolic_bp', 'cholesterol']]
    y = df['prognosis']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def train_model(X_train, y_train):
    """Train the Random Forest model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def save_model(model, scaler, model_path='model.joblib', scaler_path='scaler.joblib'):
    """Save the trained model and scaler."""
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

def main():
    # Load and preprocess data
    df = load_data('pronostico_dataset (1).csv')
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy, report = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(report)
    
    # Save model and scaler
    save_model(model, scaler)

if __name__ == "__main__":
    main() 