import pytest
from todo_logic import add_task, complete_task, delete_task, list_tasks, Task


def test_add_task_creates_task():
    tasks = []
    tasks, next_id = add_task(tasks, "Learn pytest", 1)

    #Test that the task exists in the list
    assert len(tasks) == 1
    #Test that the description exists
    assert tasks[0].description == "Learn pytest"
    #Test that the completed flag is False
    assert tasks[0].completed is False
    #Test that the next_id is set to 2 after running
    assert next_id == 2

#A function that tests if the completed flag flips to True after complete_task is run
def test_complete_task_marks_done():
    tasks = [Task(1, "Task 1", False)]

    updated = complete_task(tasks, 1)

    assert updated[0].completed is True

#Tests that a second task is not affected when the first task is completed
def test_complete_task_does_not_modify_other_tasks():
    tasks = [Task(1, "A", False), Task(2, "B", False)]

    updated = complete_task(tasks, 1)

    assert updated[0].completed is True
    assert updated[1].completed is False

#Tests that a nonexistent task will draw an error
def test_complete_nonexistent_task_raises():
    tasks = [Task(1, "A", False)]

    with pytest.raises(ValueError):
        complete_task(tasks, 999)

#A function that tests that a completed task cannot be completed again
def test_complete_task_cannot_be_completed_twice():
    tasks = [Task(1, "A", False)]

    # first completion should work
    updated = complete_task(tasks, 1)

    # second completion should fail
    with pytest.raises(ValueError):
        complete_task(updated, 1)

#Tests that deleting a task deletes the correct one
def test_delete_task_removes_correct_task():
    tasks = [Task(1, "A"), Task(2, "B")]

    updated = delete_task(tasks, 1)

    assert len(updated) == 1
    assert updated[0].id == 2

#Tests that deleting the task does not affect others
def test_delete_task_does_not_modify_other_tasks():
    tasks = [Task(1, "A"), Task(2, "B")]

    updated = delete_task(tasks, 1)

    assert updated[0].description == "B"

#Tests that trying to delete a nonexistent task raises an error
def test_delete_nonexistent_task_raises():
    tasks = [Task(1, "A")]

    with pytest.raises(ValueError):
        delete_task(tasks, 999)

#Tests the format of an outputted list
def test_list_tasks_formats_output():
    tasks = [
        Task(1, "Buy milk", False),
        Task(2, "Study Python", True)
    ]

    result = list_tasks(tasks)

    assert result == [
        "[ ] 1: Buy milk",
        "[x] 2: Study Python"
    ]

#Tests how the system takes an empty list as input
def test_list_tasks_empty():
    tasks = []

    result = list_tasks(tasks)

    assert result == []

#Tests that the order of the list is preserved
def test_list_tasks_order_preserved():
    tasks = [
        Task(1, "A"),
        Task(2, "B"),
        Task(3, "C")
    ]

    result = list_tasks(tasks)

    assert result[0].startswith("[ ] 1")
    assert result[1].startswith("[ ] 2")
    assert result[2].startswith("[ ] 3")

#Tests how the system uses whitespace in list_TASKS
def test_list_tasks_trims_description():
    tasks = [Task(1, "  Hello  ", False)]

    result = list_tasks(tasks)

    assert result == ["[ ] 1: Hello"]