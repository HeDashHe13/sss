import numpy as np
import pandas as pd
import ccxt
from VaderSentiment.vader Sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os
import transformers
API_KEY="e052d64e474240026e6e8f338e948c46868e5780f78f9cd23fb97646cbf341bf"
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env into the environment

api_key = os.getenv("API_KEY")
print(f"My API Key is: {API_KEY}")
