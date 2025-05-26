"""x = "Awesome"

def myfunc():
    x = "Fantastic"
    print("python is " + x)

myfunc()
print("python is " + x)
"""

x = "Fantastic"
def myfunc():
    global x
    x = "Awesome"
    print("python is " + x)

myfunc()
print("python is " + x)