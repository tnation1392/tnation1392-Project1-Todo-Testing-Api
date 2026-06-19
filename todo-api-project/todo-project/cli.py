import sys
from todo_logic import add_task, complete_task, delete_task, list_tasks
from storage import save_tasks, load_tasks


def main(filename="tasks.json"):
    # Allow filename override from CLI (used in tests)
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    # Load existing tasks
    tasks = load_tasks(filename)

    # Compute next_id safely
    next_id = max((task.id for task in tasks), default=0) + 1

    print("Simple Todo App (type 'help' for commands)")

    while True:
        user_input = input(">>> ").strip()

        # ✅ Quit
        if user_input == "quit":
            print("Goodbye!")
            break

        # ✅ Help
        if user_input == "help":
            print("Commands:")
            print("  add <description>")
            print("  list")
            print("  complete <id>")
            print("  delete <id>")
            print("  quit")
            continue

        # ✅ Add
        if user_input.startswith("add "):
            description = user_input[4:]

            try:
                tasks, next_id = add_task(tasks, description, next_id)
                save_tasks(tasks, filename)
                print("Task added.")
            except ValueError as e:
                print(f"Error: {e}")

            continue

        # ✅ List
        if user_input == "list":
            output = list_tasks(tasks)

            if not output:
                print("No tasks.")
            else:
                for line in output:
                    print(line)

            continue

        # ✅ Complete
        if user_input.startswith("complete "):
            try:
                parts = user_input.split()
                task_id = int(parts[1])

                tasks = complete_task(tasks, task_id)
                save_tasks(tasks, filename)

                print("Task completed.")
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")

            continue

        # ✅ Delete
        if user_input.startswith("delete "):
            try:
                parts = user_input.split()
                task_id = int(parts[1])

                tasks = delete_task(tasks, task_id)
                save_tasks(tasks, filename)

                print("Task deleted.")
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")

            continue

        # ✅ Unknown command
        print("Unknown command. Type 'help' for options.")


if __name__ == "__main__":
    main()