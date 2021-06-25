import vk_api
from instagrapi import Client
import requests

# для Instagram. В теории должно работать, однако на практике нет
def share_to_instagram(login: str, password: str, *images, caption: str = ""):
    if len(caption) <= 2200:
        bot = Client()
        bot.login(login, password)
        bot.album_upload(images, caption=caption)



def share_to_vk():

    #1 открыть диалог авторизации/ ha-ha не будет работать в вебе
    app_id = "7888292"
    authlink = "https: // oauth.vk.com / authorize?client_id={client_id}" \
               "&redirect_url={redirect_url}" \
               "&display={display}" \
               "&scope={scope}" \
               "&response_type={response_type}" \
               "&{state}".format(
        client_id=app_id,
        redirect_url="gardenenr_chto-to-tam",
        display="popup",
        scope="wall",
        response_type="code",

    )
