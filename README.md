# Task-Master-CLI

<p align="center">
    <img src="IconTaskMaster.ico" alt="Preview" width="300" height="300">
</p>

This is a simple command-line interface (CLI) to track and manage your tasks. This app allows you to add, update, delete and list tasks, as well as mark them as in-progress or done.

## Features

TaskMaster offers several features to help users manage their tasks effectively:

- **add a task**: Users can add new tasks with any description they want.
- **delete a task**: Users can delete tasks that are no longer needed.
- **update a task**: Users can update the description of a specific task.
- **list task**: Users can view all the tasks they have added, they can also filter them by status (todo, in-progress or done).
- **mark task**: Users can mark a task as todo, in-progress or done when they start working.

## Data structure

The data is stored in a dictionary where the keys are the task IDs and the values are dictionaries containing the task information. Here is an example:

'''bash
{
    "1": {
        "description": "Make homework",
        "status": "todo",
        "createdAt": "12/11/2024, 09:32:15",
        "updatedAt": "12/11/2024, 09:32:15"
    },
    task_ID: {
        "description": task description,
        "status": todo, in-progress or done ('todo' by default),
        "createdAt": date and time where the task was created,
        "updatedAt": date and time where the task was updated
    }
}
'''
All this data is stored in a file called `TaskMaster.json` in the same directory as the script; the file is created automatically if it does not exist.

## Usage

- **Add a task**: You can use the '-a' or '--add' command followed by the task description to add a new task.
    -Example:
        '''bash
        python TaskMaster.py -a "Make homework"
                                    List of all tasks
        ╭────┬───────────────┬────────┬──────────────────────┬──────────────────────╮
        │ ID │ Description   │ Status │ Created At           │ Updated At           │
        │ 1  │ Make homework │ todo   │ 12/11/2024, 09:32:15 │ 12/11/2024, 09:32:15 │
        ╰────┴───────────────┴────────┴──────────────────────┴──────────────────────╯
        '''
- **Delete a task**: You can use the '-d' or '--delete' command followed by the task ID to delete a task. The programm will ask you to confirm the deletion.
    -Example:
        '''bash
        python TaskMaster.py -d 4                       
                                        List of all tasks
        ╭────┬────────────────────────┬────────┬──────────────────────┬──────────────────────╮
        │ ID │ Description            │ Status │ Created At           │ Updated At           │
        ├────┼────────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 4  │ Push changes to GitHub │ done   │ 12/11/2024, 09:37:07 │ 12/11/2024, 09:37:57 │
        ╰────┴────────────────────────┴────────┴──────────────────────┴──────────────────────╯
        are you sure to delete the task with ID 4? (y/n): y
        Task with ID 4 was deleted
        '''
- **Update a task**: You can use the '-u' or '--update' command followed by the task ID and the new description to update the task.
    -Example:
        '''bash
        python TaskMaster.py -u 1 "Make math homework"
                                List of all tasks
        ╭────┬────────────────────┬────────┬──────────────────────┬──────────────────────╮
        │ ID │ Description        │ Status │ Created At           │ Updated At           │
        ├────┼────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 1  │ Make math homework │ todo   │ 12/11/2024, 09:32:15 │ 12/11/2024, 13:11:10 │
        ╰────┴────────────────────┴────────┴──────────────────────┴──────────────────────╯
        '''
- **List tasks**: You can use the '-ls' or '--list' command to list all tasks. You can also indicate the task status 'all', 'todo', 'in-progress' or 'done' ('all' by default) to filter data.
    -Example:
        '''bash
        python TaskMaster.py -ls
                                    List of all tasks
        ╭────┬───────────────────────────┬────────┬──────────────────────┬──────────────────────╮
        │ ID │ Description               │ Status │ Created At           │ Updated At           │
        ├────┼───────────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 1  │ Make math homework        │ todo   │ 12/11/2024, 09:32:15 │ 12/11/2024, 13:11:10 │
        ├────┼───────────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 2  │ Go to the U               │ todo   │ 12/11/2024, 09:33:09 │ 12/11/2024, 09:33:09 │
        ├────┼───────────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 3  │ Finish TaskMaster project │ done   │ 12/11/2024, 09:33:36 │ 12/11/2024, 09:37:40 │
        ╰────┴───────────────────────────┴────────┴──────────────────────┴──────────────────────╯
        python TaskMaster.py -ls done
                                   List of done tasks
        ╭────┬───────────────────────────┬────────┬──────────────────────┬──────────────────────╮
        │ ID │ Description               │ Status │ Created At           │ Updated At           │
        ├────┼───────────────────────────┼────────┼──────────────────────┼──────────────────────┤
        │ 3  │ Finish TaskMaster project │ done   │ 12/11/2024, 09:33:36 │ 12/11/2024, 09:37:40 │
        ╰────┴───────────────────────────┴────────┴──────────────────────┴──────────────────────╯
        '''
- **Mark a task**: You can use the '-m' or '--mark' command followed by the task ID and the new status to mark a task.
    -Example:
    '''bash
    python TaskMaster.py -m 1 in-progress
                                   List of all tasks
    ╭────┬────────────────────┬─────────────┬──────────────────────┬──────────────────────╮
    │ ID │ Description        │ Status      │ Created At           │ Updated At           │
    ├────┼────────────────────┼─────────────┼──────────────────────┼──────────────────────┤
    │ 1  │ Make math homework │ in-progress │ 12/11/2024, 09:32:15 │ 12/11/2024, 13:22:28 │
    ╰────┴────────────────────┴─────────────┴──────────────────────┴──────────────────────╯
    '''

## Instalation

There are different ways to install this project:

- **Clone the repository using Git**: You can clone the repository using the following command on Git Bash CLI or your Terminal:
    '''bash
    git clone https://github.com/JDiegocampos/Task-Master-CLI.git
    '''
    **You need to install the 'rich' library for the code to work properly**

- **Installing via pip**: You can install the project using pip by running the following command on your Terminal:
    '''bash
    pip install git+https://github.com/JDiegocampos/Task-Master-CLI.git
    '''

- **Using the TaskMaster.exe file**: You can download the 'TaskMaster.exe' file from the 'dist' folder of the repository and run it in your Terminal by navigating to the directory where the 'TaskMaster.exe' file is located.
Once you're in the directory, you can use the 'TaskMaster.exe' file by typing the project name followed by the command you want to run. For example:
'''bash
TaskMaster -a "Make homework"
'''
This is the easiest way to use the proyect.
