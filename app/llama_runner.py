import subprocess

def run_llama(prompt):
    result = subprocess.run([
        './llama/main',
        '-m', 'models/mistral.gguf',
        '-p', prompt,
        '-n', '200'
    ], capture_output=True, text=True)

    return result.stdout