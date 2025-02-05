# remove_todo.py

def remove_todo(todos, task):
    todos = [todo for todo in todos if todo["task"] != task]
    print(f"할 일이 제거되었습니다: {task}")
    return todos
