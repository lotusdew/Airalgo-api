from websocket import create_connection, WebSocketConnectionClosedException
import json

# Check and Establish connection with websocket
ws = websocket.create_connection("wss://api.airalgo.com/socket/websocket", sslopt={"cert_reqs": ssl.CERT_NONE})

# Payload to authenticate with the websocket
conn = {
    "topic" : "api:join",
    "event" : "phx_join",
    "payload" :
        {
            "phone_no" : phone_numer #"1234567890"
        },
    "ref" : ""
    }

# Authenticate with websocket
ws.send(json.dumps(conn))
print(ws.recv())

# Create Payload to subscribe Equity ltp 
# {"topic" : "api:join", "event" : "ltp_quote", "payload" : ["ACC", "ABB", "ADANIENT"], "ref" : ""}
def create_payload(tickers):
    # tickers = ["AIAENG", "APLAPOLLO"] #List of tickers to subscribe
    symbol_list = []
    for i in tickers:
        symbol_list.append(i)

    payload = {
      "topic" : "api:join",
      "event" : "ltp_quote", 
      "payload" : {
        "list": symbol_list
        }, 
      "ref" : ""
      }

    return payload

  # Returns payload for given tickers
tickers = ["AIAENG", "APLAPOLLO"] # List of tickers to be subscribed, Use the given nifty500 list symbols for reference
payload = create_payload(ticker)

  # Subscribe Tickers on Websocket 
ws.send(json.dumps(payload))

  # Recieve ltp for the subscribed tickers 
while True:
  data = json.loads(ws.recv())
  # Response for ltp_quote event, 1 ticker at a time every second for all tickers given
  #   data = {
  #     "event": "ltp_response",
  #     "payload": [
  #         {
  #             "expiry_date": "0",
  #             "instrument": "EQUITY",
  #             "option_type": "EQ",
  #             "strike_price": 0,
  #             "symbol": "ADANIENT"
  #         },
  #         25,
  #         284600,
  #         2,
  #         "2013-12-13T13:24:53Z"
  #     ],
  #     "ref": null,
  #     "topic": "api:join"
  # } 

  # Place Order, json = {"topic" : "api:join", "event" : "order", "payload" : {"phone_no" : "9634699119", "symbol" : "ACC", "buy_sell" : "B", "quantity" : 1, "price" : 1012.34}, "ref" : ""}
  order = {
     "topic" : "api:join", 
     "event" : "order", 
     "payload" : {
        "phone_no" : "9634699119", 
        "symbol" : "ACC", 
        "buy_sell" : "B", 
        "quantity" : 1, 
        "price" : 1012.34
        }, 
      "ref" : ""
      }
  ws.send(json.dumps(order))
  print(data)