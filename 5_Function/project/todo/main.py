from todo_manager import todo_manager


def display_menu():
    print("\n*** 할 일 관리 프로그램 ***")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 수정")
    print("4. 할 일 완료")
    print("5. 할 일 삭제")
    print("6. 종료")


def main():
    todos = []
    while True:
        display_menu()

        # 사용자 입력을 받음
        user_choice = input("원하는 작업을 선택하세요 (1, 2, 3, 4, 5, 6): ")

        if user_choice == "1":
            task = input("추가할 할 일을 입력하세요: ")
            todos = todo_manager(todos, "add", task)

        elif user_choice == "2":
            todos = todo_manager(todos, "list")

        elif user_choice == "3":
            old_task = input("수정할 할 일을 입력하세요: ")
            new_task = input("새로운 할 일을 입력하세요: ")
            todos = todo_manager(todos, "update", old_task, new_task)

        elif user_choice == "4":
            task = input("완료할 할 일을 입력하세요: ")
            todos = todo_manager(todos, "complete", task)

        elif user_choice == "5":
            task = input("삭제할 할 일을 입력하세요: ")
            todos = todo_manager(todos, "remove", task)

        elif user_choice == "6":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    # 프로그램 실행
    main()
