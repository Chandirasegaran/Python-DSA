class Task:
    def __init__(self,task):
        self.task=task
        self.completed=False
    def __str__(self) -> str:
        status = "✔" if self.completed else "✘"
        return f"{status} - {self.task}"

class TaskManager:
    def __init__(self):
        self.tasks=[]
        self.undo_stack=[]
        self.redo_stack=[]

    def addTask(self,task):
        self.tasks.append(task)
        self.undo_stack.append(("add",task))
        self.redo_stack.clear()

    def completeTask(self,task):
        task.completed = True
        self.undo_stack.append(("complete",task))
        self.redo_stack.clear()

    def notCompleteTask(self,task):
        task.completed = False
        self.undo_stack.append(("complete",task))
        self.redo_stack.clear()

    def viewTask(self):
        for task in self.tasks:
            print(task)

class TaskHandler:
    def __init__(self):
        self.task_manager=TaskManager()

    def addTask(self,task):
        task=Task(task=task)
        self.task_manager.addTask(task=task)
    
    def completeTask(self,task):
        item=self.findTask(task=task)
        if(item):
            self.task_manager.completeTask(item)
        else:
            print("Task Not Found!")

    def notCompleteTask(self,task):
        item=self.findTask(task=task)
        if(item):
            self.task_manager.notCompleteTask(item)
        else:
            print("Task Not Found!")

    def findTask(self,task):
        for tsk in self.task_manager.tasks:
            if tsk.task==task:
                return tsk
        return None

    def viewTasks(self):
        self.task_manager.viewTask()
    

def main():
    handler = TaskHandler()  
    handler.addTask(task="Do Coding")
    handler.viewTasks()
    handler.completeTask(task="Do Coding")
    handler.viewTasks()
    handler.notCompleteTask(task="Do Coding")
    handler.viewTasks()

if __name__ == "__main__":
    main()
