from dataclasses import dataclass

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False

def add_task(tasks, description, next_id):
    if not description or not description.strip():
        raise ValueError("Description cannot be empty")

    new_task = Task(id=next_id, description=description.strip())

    return tasks + [new_task], next_id + 1

def complete_task(tasks, task_id):
    found = False
    updated_tasks = []

    for task in tasks:
        if task.id == task_id:
            if task.completed:
                raise ValueError(f"Task {task_id} is already completed")

            updated_tasks.append(Task(task.id, task.description, True))
            found = True
        else:
            updated_tasks.append(task)

    if not found:
        raise ValueError(f"Task with id {task_id} not found")

    return updated_tasks

def delete_task(tasks, task_id):
    updated_tasks = [task for task in tasks if task.id != task_id]

    if len(updated_tasks) == len(tasks):
        raise ValueError(f"Task with id {task_id} not found")

    return updated_tasks

def list_tasks(tasks):
    output = []

    for task in tasks:
        # Step 1: determine status
        if task.completed:
            status = "[x]"
        else:
            status = "[ ]"

        # Step 2: build formatted string
        formatted = f"{status} {task.id}: {task.description.strip()}"

        # Step 3: add to output
        output.append(formatted)

    return output