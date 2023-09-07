import requests
import time

STOCK_KEY = 'K4UXKCTF5POS6YBS'

bank_symbols = [ "C","JPM", "BAC", "WFC", "GS",]
base_url = 'https://www.alphavantage.co/query'



while True:
    for symbol in bank_symbols:
        # Build the URL for each bank's stock price
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': STOCK_KEY }
        
        try:
            # Send a GET request to the API
            response = requests.get(base_url, params=params)
            data = response.json()
            
            # Extract the stock price from the response
            if 'Global Quote' in data:
                stock_price = data['Global Quote']['05. price']
                print(f"{symbol}: {stock_price}")
            else:
                print(f"Failed to fetch data for {symbol}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        params = {
            'function': 'NEWS_SENTIMENT',
            'symbol': symbol,
            'apikey': STOCK_KEY}
             # Send a GET request to the API
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            
            # Extract the stock price from the response
            if 'feed' in data:
                for item in data['feed']:

                
                    print(f"{item['title']} url : {item['url']} sentiment score : {item['overall_sentiment_score']}")
            else:
                print(f"Failed to fetch data for {symbol}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        params = {
            'function': 'CASH_FLOW',
            'symbol': symbol,
            'apikey': STOCK_KEY}
             # Send a GET request to the API
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            
            # Extract the stock price from the response
            if "quarterlyReports" in data:
                
                print(f"Operating Cash Flow : {data['quarterlyReports'][0]['operatingCashflow']} Cash Flow From Invesment : {data['quarterlyReports'][0]['cashflowFromInvestment']} ")
            else:
                print(f"Failed to fetch data for {symbol}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Sleep for 20 minutes before polling again
    time.sleep(1200)  # 1200 seconds = 20 minutes



