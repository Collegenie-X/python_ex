# add_task.py
class AddTask:
    def __init__(self, task_manager, task_name):
        self.task_manager = task_manager
        self.task_name = task_name

    def execute(self):
        """새로운 할 일 추가"""
        self.task_manager.add_task(self.task_name)
