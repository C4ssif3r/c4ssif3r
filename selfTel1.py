from pyrogram import Client
import datetime
import pytz
import aiocron
import random

api_id = 28902021
api_hash = "94a350af6573f9dab484183692ade0d7"
app = Client("ZeroResoddBot", api_id, api_hash)



random_bio_list = ["can you see me?", "here we are baaaaack"]
@aiocron.crontab('*/1 * * * *')                                       async def attim2():
    if app.is_connected:                                                      now = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
        print (now)
        formated_time = now.strftime("%H:%M")
        formated_time = formated_time.replace("0","ð").replace("1","ð>        .replace("3","ð").replace("4","ð").replace("5","ð").replace(">
        .replace("8","ð").replace("9","ð").replace(":",":")                   new_name = f"|  {formated_time}"
        formated_time2 = now.strftime("%I:%M - %p").replace("0","ð").>        .replace("3","ð").replace("4","ð").replace("5","ð").replace(">
        .replace("8","ð").replace("9","ð").replace(":",":").replace(">
        print (formated_time2)
        random_bio = random.choice(random_bio_list)
        new_bio = f"{random_bio} {formated_time2}"
        await app.update_profile(last_name=new_name, bio=new_bi
