import requests
from rich.console import Console

console = Console()

def display_banner():
    banner_url = "https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/banner.txt"
    try:
        response = requests.get(banner_url)
        response.raise_for_status()
        banner = response.text
        console.print(f"[bold cyan]{banner}[/bold cyan]")
    except Exception as e:
        console.print(f"[bold red]Error fetching banner: {str(e)}[/bold red]")
    
    console.print("  [bold green]CHANNEL: @TRIPLEZZX[/bold green]")

display_banner()
