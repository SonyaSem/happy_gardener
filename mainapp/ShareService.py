from instagrapi import Client
from pathlib import Path
from typing import List

INSTAGRAM_MAX_PICTURE_AMOUNT = 10
INSTAGRAM_MAX_CAPTION_SIMBOLS_AMOUNT=2200

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
    if len(caption) <= INSTAGRAM_MAX_CAPTION_SIMBOLS_AMOUNT and len(images) <= INSTAGRAM_MAX_PICTURE_AMOUNT:
        bot = Client()
        bot.login(login, password)
        bot.album_upload(images, caption=caption)

