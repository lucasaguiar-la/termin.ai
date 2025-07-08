from fastapi import FastAPI, Request
from pydantic import BaseModel
from .llama_runner import run_llama
import logging

logging.basicConfig(level=logging.INFO)

class Prompt(BaseModel):
    prompt: str

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    body = await request.body()
    logging.info(f"Request body: {body}")
    response = await call_next(request)
    return response

@app.post('/generate')
def generate(prompt: Prompt):
    output = run_llama(prompt.prompt)
    return {'response': output.strip()}