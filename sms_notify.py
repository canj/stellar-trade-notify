from stellar_base.address import Address
from twilio.rest import Client
import config

address = Address(address=config.address, horizon_uri=config.horizon)

client = Client(config.twilio_account_sid, config.twilio_auth_token)

message = client.messages.create(
    to=config.twilio_to,
    from_=config.twilio_from,
    body="Trade Received")  # Message to send via SMS


def trade_handler(response):
    print(response)
    print(message.sid)


# Loop that checks for updates on the address
trades = address.trades(sse=True, cursor='now')
for trade in trades:
    trade_handler(trades)
