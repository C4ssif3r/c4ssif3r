from pyrogram import Client, filters
import datetime
import pytz
import aiocron
import random
import requests as r
from fake_useragent import UserAgent
ua = UserAgent()
agent = ua.random

#from PIL import Image, ImageDraw, ImageFont
#r = requests.Session()
api_id = 27598328
api_hash = "f6307daf72923bac12525d307b086c7a"
app = Client("mojiResoddBot", api_id, api_hash)

# Change the path to the location of your image file
#img_path = "i.jpg"
url = "https://raw.githubusercontent.com/C4ssif3r/c4ssif3r/main/RandomBio.txt"
#random_bio_list = r.get(url)
@aiocron.crontab('*/1 * * * *')
async def attim2():
    if app.is_connected:
        headers = {"User-Agent":ua.random}
        andom_bio_list = r.get(url, headers=headers).text
        random_bio_list = andom_bio_list.splitlines()
        print(random_bio_list)
        now = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
  #      print (now)
        formated_time = now.strftime("%H:%M")
        formated_time = formated_time.replace("0","𝟎").replace("1","𝟏").replace("2","𝟐")\
        .replace("3","𝟑").replace("4","𝟒").replace("5","𝟓").replace("6","𝟔").replace("7","𝟕")\
        .replace("8","𝟖").replace("9","𝟗").replace(":",":")
        formated_time2 = now.strftime("%I:%M %p").replace("0","𝟎").replace("1","𝟏").replace("2","𝟐")\
        .replace("3","𝟑").replace("4","𝟒").replace("5","𝟓").replace("6","𝟔").replace("7","𝟕")\
        .replace("8","𝟖").replace("9","𝟗").replace(":",":").replace("AM","𝐀𝐌").replace("PM","𝐏𝐌")
 #       print (formated_time2)
        random_bio = random.choice(random_bio_list)
        new_bio = f"{random_bio} | AT {formated_time2}"
        
        # Draw the time on the image
#        img = Image.open(img_path)
 #       draw = ImageDraw.Draw(img)
  #      font = ImageFont.truetype('arial.ttf', 50)
   #     draw.text((0, 0), formated_time, font=font)

        # Save the image
    #    img.save('i_with_time.jpg')
        new_name = f"|  {formated_time}"
        # Update profile picture and bio
        await app.update_profile(bio=new_bio, last_name=new_name)
     #   await app.set_profile_photo(photo='i_with_time.jpg')

app.run()
