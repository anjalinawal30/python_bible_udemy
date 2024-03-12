print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

print(*numbers) #unpack iterable data
print("abc")
print(*"abc")

def add(x,y):
    return x+y

add(10,10)

#pack
def add(*numbers):
    total = 0
    for number in numbers:
        total = total+number
    return total

answer = add(1,2,3,4,5,6,7,8,9)
print(answer)

#unpack keyword arguments
def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

disc = {"name": "Anjali", "age":23, "likes":"Dancing"}
answer1 = about(**disc) #as it is keyword argument
print(answer1)


#pack keywords arguments
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

foo(huda="Female",ziyad="male",john="male")
