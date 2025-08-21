from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

c = Console()
c.print(Panel.fit("[bold magenta]Py-playground[/]\n[green]Du är KING BROR![/] 🚀"))
for _ in track(range(20), description="Bygger självförtroende…"):
    sleep(0.05)

c.print("[bold cyan]Klart![/] Nu vidare till nästa nivå. ✨")
