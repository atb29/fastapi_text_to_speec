from fastapi import FastAPI
from .routes import auth, text_to_speech

app = FastAPI()

# Register routes
app.include_router(auth.router)
app.include_router(text_to_speech.router)

@app.get("/", response_model=str)
async def root():
    return "Welcome to the FastAPI Text-to-Speech API!"