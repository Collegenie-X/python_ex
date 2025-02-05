# task_manager.py
from task import Task

class TaskManager:
    def __init__(self):
        """할 일 목록 초기화"""
        self.tasks = []
        self.index_counter = 1  # 인덱스는 1부터 시작

    def add_task(self, task_name):
        """새로운 할 일 추가"""
        task = Task(self.index_counter, task_name)
        self.tasks.append(task)
        self.index_counter += 1  # 인덱스 번호 증가
        print(f"할 일 '{task_name}'가 추가되었습니다.")

    def update_task(self, task_index, new_task_name):
        """할 일 이름 수정"""
        for task in self.tasks:
            if task.index == task_index:
                task.name = new_task_name
                print(f"할 일 '{task_index}'이 '{new_task_name}'로 수정되었습니다.")
                return
        print(f"할 일 인덱스 '{task_index}'을 찾을 수 없습니다.")

    def delete_task(self, task_index):
        """할 일 삭제"""
        for task in self.tasks:
            if task.index == task_index:
                self.tasks.remove(task)
                print(f"할 일 '{task_index}'가 삭제되었습니다.")
                return
        print(f"할 일 인덱스 '{task_index}'을 찾을 수 없습니다.")

    def get_tasks(self):
        """현재 할 일 목록 조회"""
        return self.tasks

    def mark_task_completed(self, task_index):
        """할 일을 완료 상태로 변경"""
        for task in self.tasks:
            if task.index == task_index:
                task.mark_completed()
                print(f"할 일 '{task_index}'가 완료되었습니다.")
                return
        print(f"할 일 인덱스 '{task_index}'을 찾을 수 없습니다.")

    def mark_task_pending(self, task_index):
        """할 일을 미완료 상태로 변경"""
        for task in self.tasks:
            if task.index == task_index:
                task.mark_pending()
                print(f"할 일 '{task_index}'가 미완료로 변경되었습니다.")
                return
        print(f"할 일 인덱스 '{task_index}'을 찾을 수 없습니다.")
