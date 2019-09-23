# This script is for testing notification responses in console.


from stellar_base.address import Address
import config


address = Address(address=config.address, horizon_uri=config.horizon)


# Trade complete response - Need to add transaction info
def payment_handler(response):
    print(response)


# Check for new trade
payments = address.payments(sse=True, cursor='now')
for payment in payments:
    payment_handler(payments)
