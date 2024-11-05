import argparse
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table, box

console = Console()
dataset = "TaskMaster.json"
def main():
    #get the current data
    data = get_data(dataset)
    #Add arguments or commands
    parser =  argparse.ArgumentParser(description='Task management by CLI')
    parser.add_argument('-a', '--add', type=str, help='Add a new task by typing its description')
    parser.add_argument('-d', '--delete', type=int, help='Delete a task by typing its ID')
    parser.add_argument('-ls', '--list', nargs='?', const='all', choices=["all", "todo", "in-progress", "done"], help='List all tasks or based on their status ("all", "todo", "in-progress", "done")')
    parser.add_argument('-u', '--update', nargs=2, help='Update the description of a task by typing its ID and a new description')
    parser.add_argument('-m', '--mark', nargs=2, help='Mark a specific task by typing its ID and status as "todo", "in-progress" or "done"')

    args = parser.parse_args()

    try:
        if args.add:
            add_task(data, args.add)
        elif args.delete:
            delete_task(data, str(args.delete))
        elif args.list:
            list_task(data, status=args.list)
        elif args.update:
            if len(args.update) == 2:
                update_task(data, str(args.update[0]), args.update[1])
            else:
                console.print("Please give a task ID and a new description")
        elif args.mark:
            if len(args.mark) == 2:
                mark_task(data, str(args.mark[0]), args.mark[1])
            else:
                console.print("Please give a task ID and a status")
    except Exception as e:
        console.print(f"An error occurred: {e}")

def get_data(file):
    try:
        with open(file, 'r')as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    finally:
        return data

def save_data(data, file):
    #save the data to the .json file or create a new one if it does not exist
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def add_task(data, description):
    id = str(int(max([key for key in data], default=0)) + 1) #obtains the last ID of the data and adds 1 to it
    data[id] = {
        "description":  description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    }
    #Create a new task with the given description, show it to the user and save it to the data
    list_task(data, id=id)
    save_data(data, dataset)

def delete_task(data, id):
    if id in data:
        list_task(data, id=id)
        confirmation = input(f"are you sure to delete the task with ID {id}? (y/n): ")
        if confirmation.lower() == 'y':
            del data[id]
            save_data(data, dataset)
            print(f"Task with ID {id} was deleted")
    else:
        print(f"Task with ID {id} not found.")

def update_task(data, id, description):
    if id in data:
        data[id]["description"] = description
        data[id]["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        list_task(data, id=id)
        save_data(data, dataset)
    else:
        print(f"Task with ID {id} not found.")

def list_task(data, status="all", id=None):
    #Table configuration to list tasks.
    table = Table(title=f"List of {status} tasks", show_lines=True, box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Description")
    table.add_column("Status")
    table.add_column("Created At")
    table.add_column("Updated At")
    if id != None:
        #If an ID is passed to the function, it filters the tasks in which the key is equal to the given ID.
        filtered_tasks = {k: v for k, v in data.items() if k == id}
        if filtered_tasks:
            for task_id, task in filtered_tasks.items():
                table.add_row(task_id, task['description'], task['status'], task['createdAt'], task['updatedAt'])
    elif status != "all":
        #If a status is passed to the function, it filters the tasks in which the status is equal to the given status
        filtered_tasks = {k: v for k, v in data.items() if v['status'] == status}
        if filtered_tasks:
            for task_id, task in filtered_tasks.items():
                table.add_row(task_id, task['description'], task['status'], task['createdAt'], task['updatedAt'])
        else:
            print(f"No tasks found with status '{status}'.")
    else:
        #If no status or ID is passed to the function, it lists all tasks.
        for task_id, task in data.items():
            table.add_row(task_id, task['description'], task['status'], task['createdAt'], task['updatedAt'])
    console.print(table)

def mark_task(data, id, status):
    if id in data:
        if status in ["todo", "in-progress", "done"]:
            data[id]["status"] = status
            data[id]["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            list_task(data, id=id)
            save_data(data, dataset)
        else:
            print(f"Invalid status {status}. Status must be one of: todo, in_progress, done")
    else:
        print(f"Task with ID {id} not found.")

if __name__ ==  "__main__":
    main()