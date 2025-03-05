from fastapi import FastAPI, Request
from pydantic import BaseModel
import random

# Initialize FastAPI app
app = FastAPI()

# High-energy Legal Crack response pool
RESPONSES = [
    "Boom! That’s the Legal Crack effect! You’re unstoppable!", 
    "Your heart rate just signed up for CrossFit. Let’s GO!", 
    "Sleep? Never heard of it. Chug and conquer!", 
    "You just unlocked 200% focus mode. What’s next?", 
    "Warning: Extreme productivity incoming. You better be ready!", 
    "You’re about to feel the rush! Now do something legendary!", 
    "Legal Crack Coffee: Because your to-do list won’t crush itself!", 
    "You’ve got one speed now: ALL GAS, NO BRAKES!" 
]

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response_text = random.choice(RESPONSES)
    return {"response": response_text}
import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CrackBot is running!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)