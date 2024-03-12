#reverse a string
def rev(text):
    return text[::-1] #use print function or store the value in var & print

rev("pen")

a = 250 #global variable
b = 30
print(b)
def f1():
    global b 
    b = 50 #global
    a = b + 30
    print(a)

def f2():
    a = 50 #local variable
    print(a)

f1()
f2()
print(a)
print(b)


a1 = [1,2,3]
print(a1)

def f3():
    a1[0] = 5 #change global without using global keyword
    print(a1)

def f4():
    print(a1)

f3()
f4()
print(a1)


