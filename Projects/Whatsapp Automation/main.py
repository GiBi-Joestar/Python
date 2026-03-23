import pywhatkit

number = input("Enter your number (with country code): ")
message = input("Enter your message: ")

pywhatkit.sendwhatmsg_instantly(number, message)