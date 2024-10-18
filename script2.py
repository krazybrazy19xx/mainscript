import asyncio
import os
from rich.console import Console
from rich.progress import Progress
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
from datetime import datetime

console = Console()

def verify_api_credentials():
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    if not api_id or not api_hash:
        console.print("[bold red]API ID or API Hash not found in environment variables.[/bold red]")
        return False
    return True

class YourClass:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash

    async def generate_query(self):
        console.print("[bold cyan]Generating query...[/bold cyan]")
        
        with TelegramClient('anon', self.api_id, self.api_hash) as client:
            chats = []
            last_date = None
            chunk_size = 200
            groups = []

            result = await client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash=0
            ))
            chats.extend(result.chats)

            for chat in chats:
                try:
                    if chat.megagroup == True:
                        groups.append(chat)
                except:
                    continue

            console.print(f'[bold green]Choose a group to scrape members from:[/bold green]')
            for i, g in enumerate(groups):
                console.print(f'{i}. {g.title}')

            g_index = input("Enter a Number: ")
            target_group = groups[int(g_index)]

            console.print(f'[bold cyan]Fetching Members...[/bold cyan]')
            all_participants = await client.get_participants(target_group)

            console.print('[bold green]Saving In file...[/bold green]')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'members_{timestamp}.csv'
            with open(filename, "w", encoding='UTF-8') as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
                for user in all_participants:
                    if user.username:
                        username = user.username
                    else:
                        username = ""
                    if user.first_name:
                        first_name = user.first_name
                    else:
                        first_name = ""
                    if user.last_name:
                        last_name = user.last_name
                    else:
                        last_name = ""
                    name = (first_name + ' ' + last_name).strip()
                    writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
            
            console.print(f'[bold green]Members scraped successfully. Saved to {filename}[/bold green]')

    async def script2(self):
        console.print("[bold cyan]Running Script 2 (Generate Query)[/bold cyan]")
        await self.generate_query()

async def run_script2():
    if not verify_api_credentials():
        return
    
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    your_class = YourClass(api_id, api_hash)
    await your_class.script2()

if __name__ == "__main__":
    asyncio.run(run_script2())
