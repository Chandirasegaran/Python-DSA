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


    def deleteTask(self,task):
        self.tasks.remove(task)
        self.undo_stack.append(("delete",task))
        self.redo_stack.clear()

    def notCompleteTask(self,task):
        task.completed = False
        self.undo_stack.append(("complete",task))
        self.redo_stack.clear()

    def undoTask(self):
        if self.undo_stack:
            action,task=self.undo_stack.pop()
            if action=="add":
                self.tasks.remove(task)
            elif action=="delete":
                self.tasks.append(task)
            elif action=="complete":
                task.completed = False
            self.redo_stack.append((action,task))

    def redoTask(self):
        if self.redo_stack:
            action,task=self.redo_stack.pop()
            if action=="add":
                self.tasks.append(task)
            elif action=="delete":
                self.tasks.remove(task)
            elif action=="complete":
                task.completed = True
            self.undo_stack.append((action,task))


    def viewTask(self):
        print()
        print("The Tasks are: ")
        print("-"*20)
        for task in self.tasks:
            print(task)
        print("-"*20)
        print()

class TaskHandler:
    def __init__(self):
        self.task_manager=TaskManager()

    def addTask(self,task):
        task=Task(task=task)
        self.task_manager.addTask(task=task)
        print(f"{task} - Task is added")
    
    def completeTask(self,task):
        item=self.findTask(task=task)
        if(item):
            self.task_manager.completeTask(item)
            print(f"{item} - Task is completed")
        else:
            print("Task Not Found!")

    def deleteTask(self,task):
        item=self.findTask(task=task)
        if(item):
            self.task_manager.deleteTask(item)
            print(f"{item} - Task is deleted")

    def notCompleteTask(self,task):
        item=self.findTask(task=task)
        if(item):
            self.task_manager.notCompleteTask(item)
            print(f"{item} - Task is not completed")
        else:
            print("Task Not Found!")

    def findTask(self,task):
        for tsk in self.task_manager.tasks:
            if tsk.task==task:
                return tsk
        return None

    def undo(self):
        self.task_manager.undoTask()
        print(f"*Undo*")

    def redo(self):
        self.task_manager.redoTask()
        print(f"*Redo*")

    def viewTasks(self):
        self.task_manager.viewTask()
    

def main():
    handler =TaskHandler()
    while(True):
        print("*"*30)
        print("Welcome to Task Handler")
        print("*"*30)
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Not Complete Task")
        print("5. Undo")
        print("6. Redo")
        print("7. View Task")
        print("8. Exit")
        print("*"*30)

        choice=int(input("Enter your choice: "))
        if(choice==1):
            handler.addTask(input("Enter task name: "))
        elif(choice==2):
            handler.deleteTask(input("Enter task name: "))
        elif(choice==3):
            handler.completeTask(input("Enter task name: "))
            handler.viewTasks()
        elif(choice==4):
            handler.notCompleteTask(input("Enter task name: "))
            handler.viewTasks()
        elif(choice==5):
            handler.undo()
        elif(choice==6):
            handler.redo()
        elif(choice==7):
            handler.viewTasks()
        elif(choice==8):
            exit(0)
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    main()
