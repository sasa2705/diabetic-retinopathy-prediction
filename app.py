import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Diabetic Retinopathy Prediction",
    page_icon="👁️",
    layout="wide"
)

# Load the trained model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')
    return model, scaler

def main():
    st.title("👁️ Diabetic Retinopathy Prediction System")
    st.write("Predict the likelihood of diabetic retinopathy based on patient health parameters.")
    
    # Load model and scaler
    try:
        model, scaler = load_model()
    except:
        st.error("Please train the model first by running model.py")
        return
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Patient Information")
        age = st.number_input("Age", min_value=0, max_value=120, value=50)
        systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=60, max_value=200, value=120)
        diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=40, max_value=120, value=80)
        cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=300, value=200)
    
    with col2:
        st.subheader("Reference Ranges")
        st.write("""
        - Systolic BP: Normal < 120 mmHg
        - Diastolic BP: Normal < 80 mmHg
        - Cholesterol: Normal 125-200 mg/dl
        """)
        
        # Add some visual elements
        st.write("### Health Status Indicators")
        fig, ax = plt.subplots(figsize=(6, 4))
        data = {
            'Parameter': ['Systolic BP', 'Diastolic BP', 'Cholesterol'],
            'Value': [systolic_bp, diastolic_bp, cholesterol],
            'Normal Range': [120, 80, 200]
        }
        df = pd.DataFrame(data)
        sns.barplot(data=df, x='Parameter', y='Value', ax=ax)
        ax.axhline(y=120, color='r', linestyle='--', alpha=0.3)
        st.pyplot(fig)
    
    # Make prediction
    if st.button("Predict Retinopathy Risk"):
        # Prepare input data
        input_data = np.array([[age, systolic_bp, diastolic_bp, cholesterol]])
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        
        # Display results
        st.subheader("Prediction Results")
        if prediction == 1:
            st.error("High Risk of Diabetic Retinopathy")
        else:
            st.success("Low Risk of Diabetic Retinopathy")
        
        st.write(f"Probability of Retinopathy: {probability:.2%}")
        
        # Display feature importance
        st.subheader("Feature Importance")
        feature_importance = pd.DataFrame({
            'Feature': ['Age', 'Systolic BP', 'Diastolic BP', 'Cholesterol'],
            'Importance': model.feature_importances_
        })
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(data=feature_importance, x='Feature', y='Importance')
        st.pyplot(fig)

if __name__ == "__main__":
    main() 