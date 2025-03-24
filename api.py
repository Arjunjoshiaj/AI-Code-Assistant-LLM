from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

# Load Model
model_path = "./code_assistant_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Code Assistant API!"}

@app.post("/generate_code/")
def generate_code(prompt: str):
    """Generates code based on a given prompt."""
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_code": generated_code}

# Run Server: uvicorn api:app --reload
