import gradio as gr
import pandas as pd
import joblib
import json

# Load the saved model
model = joblib.load("fraud_model.pkl")

# Load the saved feature column order
with open("feature_columns.json", "r") as f:
    feature_columns = json.load(f)

# Prediction function
def predict_fraud(*args):
    try:
        input_df = pd.DataFrame([args], columns=feature_columns)
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]
        return f"🔍 Prediction: {'FRAUD ⚠️' if prediction == 1 else 'Not Fraud ✅'}\nProbability of fraud: {prob:.4f}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create input fields for each feature
inputs = [gr.Number(label=col) for col in feature_columns]

# Build Gradio interface
demo = gr.Interface(
    fn=predict_fraud,
    inputs=inputs,
    outputs="text",
    title="💳 Credit Card Fraud Detection",
    description="Enter transaction data below to predict whether it is fraudulent."
)

if __name__ == "__main__":
    # Launch on all interfaces so Docker can expose it
    demo.launch(server_name="0.0.0.0", server_port=7860)
