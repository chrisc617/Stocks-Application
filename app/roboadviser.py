import json
import os
import requests
import csv
import time

from IPython import embed

# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'." #could not get dotenv to work
print('API KEY HAS BEEN RECOGNIZED')

symbols=[] ##Empty list to take in multiple stocks
while True: #Method derived from class to do preliminary stock symbol check. Only checking for numeric symbols
    symbol = input("Please enter a stock symbol (e.g. MSFT). When you are done, please input 'Done' ")
    if symbol=='Done':
        break
    else:
        symbols.append(symbol)


#
for i in symbols:  #This for loop will run for each individual stock in the list
    symbol=i
    try:
        float(symbol)
        quit('Numeric symbol is not valid')
    except ValueError:
        pass
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}" #Format derived from starter app
    print(request_url)

    response = requests.get(request_url)
    if "Error Message" in response.text: #Method taken from class, used to identify if the stock symbol is recognized
        print(f'{symbol} is an Invalid Stock Symbol')
        continue #continue is used to move onto the next symbol in the list

# parse the JSON response
    response_body = json.loads(response.text)

    file_name = f"data/prices_{symbol}.csv"

    datas = response_body["Time Series (Daily)"]
    # except KeyError:
    #     print(f'{symbol} Not a valid symbol')
    #     continue
    dataslist=list(datas)
    print(type(response_body))


    # print(dataslist[i],stocklistdatas[dataslist[i]])
    # print(datas['open'])
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", file_name)
    with open(csv_file_path, "w") as csv_file: #leveraged from csv module
        writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open","high","low","close","volume"])
        writer.writeheader() # uses fieldnames set above
        for i in range(len(dataslist)):
            writer.writerow({"timestamp": dataslist[i],
            'open': datas[dataslist[i]]['1. open'],
            'high':datas[dataslist[i]]['2. high'],
            'low': datas[dataslist[i]]['3. low'],
            'close': datas[dataslist[i]]['4. close'],
            'volume':datas[dataslist[i]]['5. volume']
            })

#
# traverse the nested response data structure to find the latest closing price
#Following block was derived from the starter app
    metadata = response_body["Meta Data"]
    data = response_body["Time Series (Daily)"]
    dates = list(data)
    print(f'Stock Symbol is: {metadata["2. Symbol"]}')
    print(f'Runtime:{time.strftime("%c")}')
    print(f'Data last refreshed: {metadata["3. Last Refreshed"]}')
    latest_daily_data = data[dates[0]]


    latest_price = latest_daily_data["4. close"]
    latest_price = float(latest_price)
    latest_price_usd = "${0:,.2f}".format(latest_price)
    print(f"LATEST DAILY CLOSING PRICE FOR {symbol} IS: {latest_price_usd}")
    highlist=[]
    for i in range(100): #range of 100 which was output standard output size of APi, appends to highlist so that I can use the max function
        highlist.append(datas[dataslist[i]]['2. high'])
    print(f'The recent average high of {symbol} is: {"${0:,.2f}".format(float(max(highlist)))}')

    lowlist=[]
    for i in range(100): #range of 100 which was output standard output size of APi, appends to lowlist so that I can use the min function
        lowlist.append(datas[dataslist[i]]['3. low'])
    print(f'The recent average low of {symbol} is: {"${0:,.2f}".format(float(min(lowlist)))}')

    closelist=[]
    for i in range(100): #similar concept as above
        closelist.append(float(datas[dataslist[i]]['4. close']))
    volumelist=[]
    for i in range(100): #similar concept as above
        volumelist.append(float(datas[dataslist[i]]['5. volume']))

    if latest_price/(sum(closelist)/len(closelist))<1 and sum(volumelist)>1000000: #generic equation to identify liquid securities that have room for more price growth
        print(f'{symbol} is a good buy low candidate')
    elif latest_price/(sum(closelist)/len(closelist))>1 and sum(volumelist)<1000000:
        print(f'{symbol} may be a stock on the rise, buy now before everyone starts trading it.')

    else:
        print(f'Do not buy {symbol}')
