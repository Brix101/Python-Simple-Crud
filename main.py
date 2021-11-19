from typing import NamedTuple
import random


class Item(NamedTuple):
    id: int
    name: str


class Algo:
    def __init__(self):
        self.ItemList = []

    def create(self, value):
        self.ItemList.append(Item(id=self.newId(), name=value))

    def read(self):
        return self.ItemList

    def update(self):
        pass

    def delete(self, id):
        for item in self.ItemList:
            if item.id == id:
                index = self.ItemList.index(item)
                self.ItemList.pop(index)
                print("Item%s success removed" % str(item.id))
                return True
            else:
                print("Removing Error")
                return False

    def newId(self):
        while True:
            nId = random.randint(1000, 9999)
            for item in self.ItemList:
                if item.id != nId:
                    break
            return nId


if __name__ == '__main__':
    algo = Algo()

    algo.create("Sample1")
    algo.create("Sample2")
    algo.create("Sample3")
    algo.create("Sample4")
    algo.create("Sample5")

    while True:
        choice = input("1: Add | 2: Update | 3: Delete | 4: View \n> ")

        if choice == "1":
            algo.create(input("Type New Item \n>"))
        elif choice == "3":
            while True:
                try:
                    result = algo.delete(int(input("type Item Id to Delete \n>")))
                    print(result)
                    if result == True:
                        break
                except:
                    print("Please Type Item Id")
                    False
        elif choice == "4":
            for item in algo.read():
                print("Item%s: %s" % (str(item.id), item.name))
