import streamlit as st
import numpy as np
from redwine.pipeline.prediction import PredictionPipeline

# Define the Streamlit app
def main():
    st.title("Red Wine Quality Prediction")

    # Create input widgets for user to enter data
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=15.0, step=0.1)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, step=0.01)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, step=0.01)
    residual_sugar =st.number_input('residual_sugar',min_value=0.0, max_value=20.0, step=0.01)
    chlorides =st.number_input('chlorides',min_value=0.0, max_value=20.0, step=0.01)
    free_sulfur_dioxide =st.number_input('free_sulfur_dioxide',min_value=0.0, max_value=100.0, step=0.01)
    total_sulfur_dioxide =st.number_input('total_sulfur_dioxide',min_value=0.0, max_value=150.0, step=0.01)
    density =st.number_input('density',min_value=0.0, max_value=20.0, step=0.01)
    pH =st.number_input('pH',min_value=0.0, max_value=20.0, step=0.01)
    sulphates =st.number_input('sulphates',min_value=0.0, max_value=20.0, step=0.01)
    alcohol =st.number_input('alcohol',min_value=0.0, max_value=20.0, step=0.01)
       
    # Add more input fields for other features...

    if st.button("Predict"):
        try:
            # Organize user input into a NumPy array
            data = np.array([fixed_acidity, volatile_acidity, citric_acid,
                             residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,
                             density,pH,sulphates,alcohol])  # Add more features as needed

            # Make a prediction using your PredictionPipeline
            obj = PredictionPipeline()
            prediction = obj.predict(data.reshape(1, -1))

            st.success(f"Predicted Quality: {prediction[0]}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
