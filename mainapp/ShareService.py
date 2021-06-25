from instagrapi import Client


# для Instagram. Работает но пока только с ссылками на компе
def share_to_instagram(login: str, password: str, image, caption: str = ""):
    if len(caption) <= 2200 and len(image) <= 10:
        bot = Client()
        bot.login(login, password)
        bot.album_upload(image, caption=caption)
