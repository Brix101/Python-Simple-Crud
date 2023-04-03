from typing import NamedTuple
import random

class Todo(NamedTuple):
    id: int
    todo: str
    is_complete: bool

class TodoList:

    def __init__(self):
        self.TodoItemList = []               
        
    def create(self, todo):
        new_todo = Todo(id=self.newId(),todo=todo,is_complete=False)

        self.TodoItemList.append(new_todo) 

    def read(self):        
        return self.TodoItemList

    def update(self, id):
        if id == 0000:
            return True
       
        for i, item in enumerate(self.TodoItemList):
            if item.id == id:
                print(item)
                todo = input("Enter todo : ")
                is_complete_choice = input("Enter is complete (T/F): ")

                # Validate the user input
                while is_complete_choice.lower() not in ('t', 'f'):
                    is_complete_choice = input("Invalid input. Please enter 'T' or 'F': ")
                
                is_complete = is_complete_choice.lower() == 't'

                updated_item = Todo(id=item.id,todo=todo,is_complete=is_complete)
                self.TodoItemList[i] = updated_item
                print(updated_item)

        return True

    def delete(self, id):
        if id == 0000:
            return True
        
        for item in self.TodoItemList:
            if item.id == id:
                index = self.TodoItemList.index(item)
                self.TodoItemList.pop(index)
                print("Todo %s deleted successfully" % str(item.id))
                return True
    
    def newId(self):
        while True:
            nId = random.randint(1000, 9999)
            for item in self.TodoItemList:
                if item.id != nId:
                    break
            return nId

if __name__ == '__main__':
    todo_list = TodoList()

    while True:
        choice = input("1: Add | 2: Update | 3: Delete | 4: View \n> ")

        if choice == "1":
            todo = input("Enter todo : ")
            todo_list.create(todo)
            
        elif choice == "2":
            while True:
                try:
                    id = int(input("Enter Id to update | 0000: to Exit \n>"))
                        
                    result = todo_list.update(id)
                    if result == True:
                        break                
                except:
                    for data in todo_list.read():
                       print(data)
                    print("Please Enter Todo Id \n")
                    
        elif choice == "3":
            while True:
                try:
                    id = int(input("Enter Id to delete | 0000: to Exit \n>"))
                                            
                    result = todo_list.delete(id)
                    if result == True:
                        break
                except:
                    for data in todo_list.read():
                       print(data)
                    print("Please Enter Todo Id \n")

        elif choice == "4":
            for data in todo_list.read():
                print(data)
