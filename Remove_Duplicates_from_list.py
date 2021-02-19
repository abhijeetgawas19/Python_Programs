'''
    Remove duplicate elements from list
'''


def unique_elements(mylist):
    print(f"Old List Elements are:{mylist}")
    new_list = set(mylist)
    length = len(new_list)
    print(f"New List Elements are:{new_list}")


def accept():
    mylist = []
    n = int(input("Enter the Size of List:"))
    for i in range(0, n):
        x = int(input("Enter the Element:"))
        mylist.append(x)
    unique_elements(mylist)


accept()
