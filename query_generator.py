from telethon import TelegramClient
from telethon.functions import messages
from telethon.types import InputBotAppShortName, AppWebViewResultUrl
import urllib.parse

async def generate_query(client, peer: str, bot: str, start_param: str, shortname: str):
    webapp_response: AppWebViewResultUrl = await client(messages.RequestAppWebViewRequest(
        peer=peer,
        app=InputBotAppShortName(bot_id=await client.get_input_entity(bot), short_name=shortname),
        platform='ios',
        write_allowed=True,
        start_param=start_param if start_param else None
    ))

    query_url = webapp_response.url
    query = urllib.parse.unquote(string=query_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0])
    
    return query

# Tambahkan ini di akhir file untuk memudahkan pengujian dan impor
if __name__ == "__main__":
    print("This module contains the generate_query function for use in the main script.")
