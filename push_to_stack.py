import sys

def PushtoStack(l:list, top, element):
    if top == l[0]:
        l.insert(0, element)

    elif top == l[-1]:
        l.append(element)
    else:
        print("Error")
        sys.exit(1)