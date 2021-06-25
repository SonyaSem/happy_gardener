import vk_api
from instagrapi import Client
import requests

# для Instagram. Работает но пока только с ссылками на компе
def share_to_instagram(login: str, password: str, image, caption: str = ""):
    if len(caption) <= 2200:
        bot = Client()
        bot.login(login, password)
        #bot.photo_upload(image,caption=caption)
        bot.album_upload(image, caption=caption)


share_to_instagram()
