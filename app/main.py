from fastapi import FastAPI
from llama_runner import run_llama

app = FastAPI()

@app.post('/generate')
def generate(prompt):
    output = run_llama(prompt)
    return {'response': output.strip()}