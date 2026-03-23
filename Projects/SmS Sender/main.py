from twilio.rest import Client

# Your credentials from Twilio dashboard
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python 😎",
    from_="+1234567890",   # Twilio number
    to="+97798XXXXXXXX"    # Receiver number
)

print("Message sent! SID:", message.sid)