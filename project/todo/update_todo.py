# update_todo.py

def update_todo(todos, old_task, new_task):
    for todo in todos:
        if todo["task"] == old_task:
            todo["task"] = new_task
            print(f"할 일이 수정되었습니다: {old_task} -> {new_task}")
            return
    print(f"할 일을 찾을 수 없습니다: {old_task}")
