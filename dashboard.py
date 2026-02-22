import time
import psutil
from datetime import timedelta
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn


console = Console()


def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))


def make_bar(percent):
    progress = Progress(
        TextColumn("{task.percentage:>3.0f}%"),
        BarColumn(bar_width=30),
        expand=False,
    )
    task = progress.add_task("", total=100, completed=percent)
    return progress


def build_dashboard():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    disk_path = "/System/Volumes/Data" if __import__("os").path.exists("/System/Volumes/Data") else "/"
    disk = psutil.disk_usage(disk_path)
    uptime = get_uptime()

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column("Stat", style="bold cyan", width=8)
    table.add_column("Bar")
    table.add_column("Detail", style="dim")

    table.add_row("CPU", make_bar(cpu), f"{cpu:.1f}%")
    table.add_row(
        "RAM",
        make_bar(ram.percent),
        f"{ram.used / 1e9:.1f} GB / {ram.total / 1e9:.1f} GB  ({ram.percent:.0f}%)",
    )
    table.add_row(
        "Disk",
        make_bar(disk.percent),
        f"{disk.used / 1e9:.0f} GB / {disk.total / 1e9:.0f} GB  ({disk.percent:.0f}%)",
    )

    panel = Panel(
        table,
        title="[bold green]System Stats Dashboard[/bold green]",
        subtitle=f"[dim]uptime {uptime}  •  press ctrl+c to quit[/dim]",
        border_style="green",
    )
    return panel


def main():
    with Live(build_dashboard(), refresh_per_second=0.5, screen=True) as live:
        while True:
            time.sleep(2)
            live.update(build_dashboard())


if __name__ == "__main__":
    main()
