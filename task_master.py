import argparse
import json
from datetime import datetime
import sys

dataset = "TaskMaster.json"
def main():
    data = get_data(dataset)

    parser =  argparse.ArgumentParser(description='Task management by CLI')
    parser.add_argument('-a', '--add', type=str, help='Add a new task')
    parser.add_argument('-d', '--delete', type=str, help='Delete a task')
    parser.add_argument('-ls', '--list', help='List all tasks or based on their status')
    parser.add_argument('-u', '--update', nargs=2, help='update the descrition of a task')
    parser.add_argument('-m', '--mark', help='Mark a task')
    args = parser.parse_args()

    if args.add:
        add_task(data, args.add)
    elif args.delete:
        delete_task(data, args.delete)
    elif args.list:
        pass
    elif args.update:
        if len(args.update) == 2:
            update_task(data, args.update[0], args.update[1])
        else:
            print("Please give an task ID and a new description")

def get_data(file):
    try:
        with open(file, 'r')as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    finally:
        return data

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def add_task(data, description):
    id = str(int(max([key for key in data], default=0)) + 1)
    data[id] = {
        "description":  description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    }
    save_data(data, dataset)

def delete_task(data, id):
    if id in data:
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
        save_data(data, dataset)
    else:
        print(f"Task with ID {id} not found.")

if __name__ ==  "__main__":
    main()