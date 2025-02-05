# 할 일 목록을 저장할 리스트
todos = []

# 할 일 추가 함수
def add_todo(task):
    todos.append({"task": task, "completed": False})
    print(f"할 일이 추가되었습니다: {task}")

# 할 일 제거 함수
def remove_todo(task):
    global todos
    todos = [todo for todo in todos if todo["task"] != task]
    print(f"할 일이 제거되었습니다: {task}")

# 할 일 목록 출력 함수
def list_todos():
    if not todos:
        print("현재 할 일이 없습니다.")
    for idx, todo in enumerate(todos, 1):
        status = "완료" if todo["completed"] else "미완료"
        print(f"{idx}. {todo['task']} - {status}")

# 할 일 수정 함수
def update_todo(old_task, new_task):
    for todo in todos:
        if todo["task"] == old_task:
            todo["task"] = new_task
            print(f"할 일이 수정되었습니다: {old_task} -> {new_task}")
            return
    print(f"할 일을 찾을 수 없습니다: {old_task}")

# 할 일 완료 처리 함수
def mark_complete(task):
    for todo in todos:
        if todo["task"] == task:
            todo["completed"] = True
            print(f"할 일이 완료 처리되었습니다: {task}")
            return
    print(f"할 일을 찾을 수 없습니다: {task}")

# todo를 관리하는 함수
def todo_manager(action, *args):
    if action == "add":
        add_todo(*args)
    elif action == "remove":
        remove_todo(*args)
    elif action == "list":
        list_todos()
    elif action == "update":
        update_todo(*args)
    elif action == "complete":
        mark_complete(*args)
    else:
        print("알 수 없는 명령입니다.")

# 예시 실행
todo_manager("add", "Python 공부하기")
todo_manager("add", "장보기")
todo_manager("list")
todo_manager("update", "장보기", "마트 가기")
todo_manager("complete", "Python 공부하기")
todo_manager("list")
todo_manager("remove", "마트 가기")
todo_manager("list")
