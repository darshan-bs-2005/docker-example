
import gradio as gr
import pandas as pd
import joblib
import json

# Load the saved model
model = joblib.load("fraud_model.pkl")

# Load the saved feature column order
with open("feature_columns.json", "r") as f:
    feature_columns = json.load(f)

def predict_fraud(**kwargs):
    try:
        input_df = pd.DataFrame([kwargs])
        input_df = input_df[feature_columns]
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]
        return f"🔍 Prediction: {'FRAUD ⚠️' if prediction == 1 else 'Not Fraud ✅'}\nProbability of fraud: {prob:.4f}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

inputs = [gr.Number(label=col) for col in feature_columns]

demo = gr.Interface(
    fn=predict_fraud,
    inputs=inputs,
    outputs="text",
    title="💳 Credit Card Fraud Detection",
    description="Enter transaction data below to predict whether it is fraudulent."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

