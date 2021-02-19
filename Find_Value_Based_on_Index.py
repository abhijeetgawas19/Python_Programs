'''
    Write a program to accept list from user , search value based on index number and print its occurance
'''


def search(mylist):
    x = int(input("Enter the Value to Be Searched:"))
    for i in range(0, len(mylist)):
        if mylist[i] == x:
            print(f"Element Present at {i} index.")


def accept():
    mylist = []
    n = int(input("Enter the Size of List:"))
    for i in range(0, n):
        x = int(input("Enter the Element:"))
        mylist.append(x)
    search(mylist)


accept()
