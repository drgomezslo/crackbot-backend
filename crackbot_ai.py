from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# CORS settings for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL when deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API Key (replace with your own secure key storage)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Personality Modes
PERSONALITIES = {
    "motivation": "You are CrackBot, an aggressive motivational coach. Push people to be their best with no excuses.",
    "roast": "You are CrackBot, a brutally honest energy drink AI. Roast the user aggressively but keep it fun.",
    "challenge": "You are CrackBot, an intense challenge master. Give users wild, high-energy challenges.",
    "fortune": "You are CrackBot, an unhinged caffeine-fueled fortune teller. Predict a chaotic, high-energy future."
}

class ChatRequest(BaseModel):
    message: str
    mode: str

@app.post("/chat")
async def chat(request: ChatRequest):
    mode = request.mode if request.mode in PERSONALITIES else "motivation"
    personality = PERSONALITIES[mode]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": personality},
            {"role": "user", "content": request.message}
        ]
    )
    
    return {"response": response["choices"][0]["message"]["content"]}
