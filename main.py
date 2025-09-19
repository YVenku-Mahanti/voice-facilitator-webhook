from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

# FastAPI app
app = FastAPI()

# Load Twilio credentials from environment
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.post("/twilio/voice")
async def twilio_voice(request: Request):
    """Endpoint to handle inbound calls from Twilio"""
    form = await request.form()
    from_number = form.get("From", "")
    
    # Basic Twilio greeting
    resp = VoiceResponse()
    resp.say("Hello! You've reached Dr. Rupin's Medical Centre. This is the virtual assistant.", voice="alice")
    resp.say("Please tell me your name and phone number.", voice="alice")
    
    return PlainTextResponse(str(resp), media_type="application/xml")
