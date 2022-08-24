import os
import requests

class NotificationManager:
    __TWILIO_API_SID = "AC53d4f0b291e74ae5aa6a37e0c294ca1d"
    __TWILIO_AUTH_KEY = os.environ.get("TWILIO_AUTH_TOKEN")
    def __init__(self) -> None:

    #This class is responsible for sending notifications with the deal flight details.
