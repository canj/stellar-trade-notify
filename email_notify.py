from stellar_base.address import Address
import requests
import config

address = Address(address=config.address, horizon_uri=config.horizon)


def email_alert(transaction_id):
    report = {"value1": transaction_id}  # Use this to add transaction information
    requests.post(config.trigger, data=report)


# Trade complete response - Need to add transaction info
def trade_handler(response):
    print(response)
    email_alert('transaction complete') # Email Message text


# Check for new trade
trades = address.trades(sse=True, cursor='now')
for trade in trades:
    trade_handler(trades)
