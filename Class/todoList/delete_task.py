# delete_task.py
class DeleteTask:
    def __init__(self, task_manager, task_index):
        self.task_manager = task_manager
        self.task_index = task_index

    def execute(self):
        """할 일 삭제"""
        self.task_manager.delete_task(self.task_index)
