# update_task.py
class UpdateTask:
    def __init__(self, task_manager, task_index, new_task_name):
        self.task_manager = task_manager
        self.task_index = task_index
        self.new_task_name = new_task_name

    def execute(self):
        """할 일 이름 수정"""
        self.task_manager.update_task(self.task_index, self.new_task_name)
