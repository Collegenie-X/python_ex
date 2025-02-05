# todo_manager.py
from add_todo import add_todo
from remove_todo import remove_todo
from list_todos import list_todos
from update_todo import update_todo
from mark_complete import mark_complete

def todo_manager(todos, action, *args):
    if action == "add":
        add_todo(todos, *args)
    elif action == "remove":
        todos = remove_todo(todos, *args)
    elif action == "list":
        list_todos(todos)
    elif action == "update":
        update_todo(todos, *args)
    elif action == "complete":
        mark_complete(todos, *args)
    else:
        print("알 수 없는 명령입니다.")
    return todos
