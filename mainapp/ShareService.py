from instagrapi import Client
from pathlib import Path
from typing import List

# для Instagram. Работает но пока только с ссылками на компе
def share_to_instagram(login: str, password: str, images:List[Path], caption: str = ""):
    """
    Posts to Instagram

    Parameters
    ----------
    login:str
        User Login
    password:str
        User password
    images:List[Path]
        Uploading images (max amount = 10)
    caption:str
        Post caprion (max length = 2200)
    """
    if len(caption) <= 2200 and len(images) <= 10:
        bot = Client()
        bot.login(login, password)
        bot.album_upload(images, caption=caption)

