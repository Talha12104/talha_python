import click # type: ignore # to create cli
import json # to save and load tasks froma file
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_task():
    if not os.path.exists(TODO_FILE):
        save_task([])  # Initialize with empty list if file doesn't exist
    with open(TODO_FILE, "r") as file:
        content = file.read()
        return json.loads(content) if content else []

def save_task(task):
    with open(TODO_FILE, "w") as file:
        return json.dump(task, file, indent=4)
    
@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_task(tasks)
    click.echo(f"Task added: {task}")

cli.add_command(add)

if __name__ == "__main__":
    cli()
