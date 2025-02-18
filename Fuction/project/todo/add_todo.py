# add_todo.py

def add_todo(todos, task):
    todos.append({"task": task, "completed": False})
    print(f"할 일이 추가되었습니다: {task}")
