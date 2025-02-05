# view_task.py
class ViewTasks:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def execute(self):
        """할 일 목록 조회"""
        tasks = self.task_manager.get_tasks()
        if tasks:
            print("\n--- 할 일 목록 ---")
            for task in tasks:
                print(task)
        else:
            print("할 일이 없습니다.")
