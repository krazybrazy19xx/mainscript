   import asyncio
   from rich.console import Console
   from rich.progress import Progress
   import time
   import os
   from datetime import datetime
   from telethon.sync import TelegramClient

   console = Console()

   class CustomTelegramClient(TelegramClient):
       # Paste the CustomTelegramClient class here

   class YourClass:
       def __init__(self, api_id, api_hash):
           self.api_id = api_id
           self.api_hash = api_hash

       # Paste the rest of the YourClass methods here, including script1

   async def run_script1():
       api_id = os.getenv('API_ID')
       api_hash = os.getenv('API_HASH')
       your_class = YourClass(api_id, api_hash)
       await your_class.script1()

   asyncio.run(run_script1())
