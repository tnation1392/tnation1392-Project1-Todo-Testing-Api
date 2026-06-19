from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    if not data or "description" not in data:
        return jsonify({"error": "Description is required"}), 400

    task = {
        "id": next_id,
        "description": data["description"].strip(),
        "completed": False
    }
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201

@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return jsonify({"error": "Already completed"}), 400

            task["completed"] = True
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks = new_tasks
    return jsonify({"message": "Deleted"})

def reset_data():
    global tasks, next_id
    tasks = []
    next_id = 1

@app.route("/reset", methods=["POST"])
def reset():
    reset_data()
    return jsonify({"message": "reset"}), 200

if __name__ == "__main__":
    app.run(debug=True)



