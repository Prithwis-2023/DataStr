import sys

def ViewStack(l:list, top):
    if top == l[0]:
        print("+--------------+")
        for elements in l:
            print(elements)
            print("+--------------+") 
    
    elif top == l[-1]:
        print("+--------------+")
        for elements in list(reversed(l)):
            print(elements)
            print("+--------------+")

    else:
        print("Error")
        sys.exit(1)