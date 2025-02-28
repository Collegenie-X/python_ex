# list_todos.py

def list_todos(todos):
    if not todos:
        print("현재 할 일이 없습니다.")
    for idx, todo in enumerate(todos, 1):
        status = "완료" if todo["completed"] else "미완료"
        print(f"{idx}. {todo['task']} - {status}")
