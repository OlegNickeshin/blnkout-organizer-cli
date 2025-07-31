def main():
    import os
    import argparse
    from organizer import Organizer
    from rich import print
    from rich.console import Console
    from rich.table import Table

    console = Console()

    def parse_args():
        parser = argparse.ArgumentParser(description='Organize files in a directory.')
        parser.add_argument('path', type=str, help='Path to the folder')
        parser.add_argument('--list', action='store_true', help='List all files and folders')
        parser.add_argument('--list-dirs', action='store_true', help='List only directories')
        parser.add_argument('--list-files', action='store_true', help='List only files')
        parser.add_argument('--ext', type=str, help='Organizes a given extension')
        parser.add_argument('--ext-all', action='store_true', help='Organizes all the files in a given path')
        parser.add_argument('--file-size', type=float, help='List files larger than the given size in MB')
        parser.add_argument('--sort-size', action='store_true', help='Show files sorted by size')
        parser.add_argument('--file-info', type=str, help='Get detailed info about a file')
        parser.add_argument('--modified-after', type=int, help='Show files modified in the last N days')

        return parser.parse_args()

    def extension_exists(path, ext):
        ext = ext.lstrip('.')
        for name in os.listdir(path):
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path):
                if os.path.splitext(name)[1].lstrip('.') == ext:
                    return True
        return False

    args = parse_args()
    organizer = Organizer(args.path)

    if args.ext_all:
        organizer.folder_creation()
        organizer.files_move()
    elif args.ext:
        if extension_exists(args.path, args.ext):
            organizer.detect_and_move(args.ext)
        else:
            print(f"[red]No files with extension '.{args.ext}' found.[/red]")

    if args.list:
        print(f"[bold cyan]Files and subdirectories in the directory:[/bold cyan]")
        for i, name in enumerate(organizer.list_all(), 1):
            print(f"[dim]{i}.[/dim] [green]{name}[/green]")
    else:
        if args.list_files:
            print(f"[bold cyan]Files in the directory:[/bold cyan]")
            for i, name in enumerate(organizer.file_names(), 1):
                print(f"[dim]{i}.[/dim] [green]{name}[/green]")
        if args.list_dirs:
            print(f"[bold cyan]Subdirectories in the directory:[/bold cyan]")
            for i, name in enumerate(organizer.list_dir_folders(), 1):
                print(f"[dim]{i}.[/dim] [magenta]{name}[/magenta]")

    if args.file_size is not None:
        results = organizer.find_large(args.file_size)
        if results:
            table = Table(title=f"Files larger than {args.file_size} MB", style="bright_white on grey11")
            table.add_column("File", style="green")
            table.add_column("Size (MB)", justify="right", style="red")

            for name, size in results:
                table.add_row(name, str(size))
            console.print(table)
        else:
            print("[yellow]No files exceed that size.[/yellow]")

    if args.sort_size:
        sorted_files = organizer.sort_by_size()
        table = Table(title="Files sorted by size (largest first)", style="bright_white on grey11")
        table.add_column("File", style="green")
        table.add_column("Size (MB)", justify="right", style="yellow")

        for name in sorted_files:
            size = os.path.getsize(os.path.join(args.path, name)) / (1024 * 1024)
            table.add_row(name, str(round(size, 2)))

        console.print(table)

    if args.modified_after is not None:
        recent = organizer.modified_after(args.modified_after)
        if recent:
            table = Table(title=f"Modified in the last {args.modified_after} days", style="white on grey11")
            table.add_column("File", style="green")
            table.add_column("Size (MB)", justify="right", style="red")
            table.add_column("Modified", style="cyan")

            for name, mod_time, size in recent:
                table.add_row(name, str(size), mod_time)
            console.print(table)
        else:
            print(f"[yellow]No files modified in the last {args.modified_after} days.[/yellow]")

    if args.file_info:
        info = organizer.get_file_info(args.file_info)
        print(f"[bold cyan]Detailed information about '{args.file_info}' from '{args.path}':[/bold cyan]")

        table = Table(show_header=False, style="bright_white on grey11")
        for k, v in info.items():
            table.add_row(f"[yellow]{k}[/yellow]", f"[white]{v}[/white]")
        console.print(table)

if __name__ == "__main__":
    main()
