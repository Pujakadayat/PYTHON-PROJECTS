from instabot import Bot
bot = Bot()
bot.login(username="diary.posh" , password = "")
#bot.follow('pujakadayat0') #diary.posh le pujakadayat lai follow garxa automatically
bot.upload_photo("photo ko path dena",caption='i lpy') 
bot.unfollow("name")
bot.send_message(' i love py',["username dena jaslai msg pathaune ho", "...etc "])
followers=bot.get_user_followers("username dena eg puja")
for follower in followers:
    print(bot.get_user_info(follower)) # puja ko follower ko info denxa euta list denxa (following ko ni yeari garna sakinxa)
