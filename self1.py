# -*-coding:utf8-*-
from pyrogram import Client
import datetime
import pytz
import aiocron
import random

# Info
api_id = 28902021
api_hash = "94a350af6573f9dab484183692ade0d7"
app = Client("ZeroResoddBot", api_id, api_hash)
# -Info-

# Time def
random_bio_list = ["can you see me?", "here we are baaaaack"]
@aiocron.crontab('*/1 * * * *')
async def attim2():
    if app.is_connected:
        now = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
        formated_time = now.strftime("%H:%M")
        formated_time = formated_time.replace("0","𝟎").replace("1","𝟏").replace("2","𝟐")\
        .replace("3","𝟑").replace("4","𝟒").replace("5","𝟓").replace("6","𝟔").replace("7","𝟕")\
        .replace("8","𝟖").replace("9","𝟗").replace(":",":")
        new_name = f"|  {formated_time}"
        formated_time2 = now.strftime("%I:%M - %p").replace("0","𝟎").replace("1","𝟏").replace("2","𝟐")\
        .replace("3","𝟑").replace("4","𝟒").replace("5","𝟓").replace("6","𝟔").replace("7","𝟕")\
        .replace("8","𝟖").replace("9","𝟗").replace(":",":").replace("AM","𝐀𝐌").replace("PM","𝐏𝐌")
        random_bio = random.choice(random_bio_list)
        new_bio = f"{random_bio} {formated_time2}"
        await app.update_profile(last_name = new_name,bio=new_bio)
# -Time def-

app.run()