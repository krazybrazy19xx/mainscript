   from rich.console import Console

   console = Console()

   def display_banner():
       banner_url = "https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/banner.txt"
       try:
           response = requests.get(banner_url)
           if response.status_code == 200:
               banner = response.text
               console.print(f"[bold cyan]{banner}[/bold cyan]")
           else:
               console.print("[bold red]Failed to fetch banner from URL[/bold red]")
       except Exception as e:
           console.print(f"[bold red]Error fetching banner: {str(e)}[/bold red]")
       
       console.print("  [bold green]CHANNEL: @TRIPLEZZX[/bold green]")

   display_banner()
