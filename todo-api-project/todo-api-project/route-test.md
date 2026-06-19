
## Route
- Path: /tasks
- Method: GET
- Function name: get_tasks
- Purpose: Return all tasks
- Input: None
- Success response: JSON list of tasks
- Likely status code: 200 OK
- Failure response(s): None shown in this snippet

## Test coverage
- **Test name: test_get_tasks_empty**
  - This test verifies that the GET /tasks route returns an empty collection correctly when there are no tasks yet.

---


## Route
- Path: /tasks
- Method: PUT
- Function name: create_tasks
- Purpose: Creates a task
- Input: JSON body
- Success Response: JSON for created task
                    201 Created code
- Failure: 400 bad request

## Test Coverage
- **Test Name: test_create_task**
  - verifies a valid task can be created successfully
- **Test Name: test_create_task_missing_description****
  - verifies the API rejects requests missing the description field

---

## Route
- Path: /tasks/<int:task_id>/complete
- Method:
- Function Name: complete_task
- Purpose: Mark a task as completed
- Input: Task ID
- Success Response: 200
- Failure Response:
  - 400 if already completed 
  - 404 if task is not found

## Test Coverage
- **Test Name: test_complete_task**
- Verifies that a valid task is marked complete
- **Test Name: test_complete_invalid_task**
- Verifies that completion fails for an invalid or nonexistent task
- **Test Name: test_complete_already_completed_task**
- Verifies that you cannot complete an already completed task
- **Test Name: test_complete_task_cases**
- Verifies that completed a created Task ID 1 returns a 200
- **Test Name: test_complete_task_cases**
- Verifies task ID 999 give a 404 response

--- 

## Route
- Path: likely /tasks/<task_id>
- Method: likely DELETE
- Function name: unknown until route is shown
- Purpose: Delete a task
- Input: Task ID in URL
- Success response: Confirmation or empty response
- Likely status code: 200 OK or 204 No Content
- Failure response(s): likely 404 Not Found for invalid task ID

## Test coverage
**- Test Name: test_delete_task**
- likely verifies a valid task can be deleted
- **Test Name: test_delete_invalid_task**
  - likely verifies deletion fails for an invalid or nonexistent task
 
---

## ID Validation Testing

- **test_invalid_task_ids[0]**
- **test_invalid_task_ids[-1]**
- **test_invalid_task_ids[999]**
