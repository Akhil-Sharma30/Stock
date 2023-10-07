"""
Copyright (c) 2023 Akhil Sharma. All rights reserved.

PyStoAnalyzer.
"""
import os
"""
API configuration for the stock and news APIs.

Environment variables:
    Stock_API_KEY: The API key for the stock API.
    news_API_KEY: The API key for the news API.
"""
#API Configeration
api_key = os.environ.get("Stock_API_KEY")

#News API Configeration
news_api = os.environ.get("news_API_KEY")