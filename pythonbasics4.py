# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 5

def d():
    print("inside d:", a)
def e():
    a = 2
    print("inside e:",a)
def f():
    global a
    a = 4
    print("inside f:",a)

print("global:",a)
d()
print("global:",a)
e()
print("global:",a)
f()
print("global:",a)


