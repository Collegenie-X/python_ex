# mark_complete.py

def mark_complete(todos, task):
    for todo in todos:
        if todo["task"] == task:
            todo["completed"] = True
            print(f"할 일이 완료되었습니다: {task}")
            return
    print(f"할 일을 찾을 수 없습니다: {task}")
