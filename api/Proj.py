import numpy as np
import pandas as pd
import ccxt
from VaderSentiment.vader Sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os
import transformers
API_KEY="6e14d133-9595-4b9f-85f4-9b67304163e3"
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env into the environment

api_key = os.getenv("API_KEY")
print(f"My API Key is: {API_KEY}")
