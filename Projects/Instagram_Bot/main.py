from instabot import Bot
import time

bot = Bot()

user = input("Enter your username: ")
passwd = input("Enter your password: ")

if bot.login(username=user, password=passwd):
    print("✅ Logged in")

    time.sleep(5)
    bot.follow('gibi.joestar')
    print("✅ Followed user")

else:
    print("❌ Login failed")