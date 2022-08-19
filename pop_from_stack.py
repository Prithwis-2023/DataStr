import sys

def PopfromStack(l:list, top):
    if top == l[0]:
        l.pop(0)

    elif top == l[-1]:
        l.pop(-1)

    else:
        return "Error"
        sys.exit(1)
