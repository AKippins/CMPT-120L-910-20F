#if statement
if True:
    print("Hi.")

#if else statement
if True:
    print("Hi!")
else:
    print("Bye!")

#elif else statement
if True:
    print("Hi!!")
elif False:
    print("Bye!!")
else:
    print("Uhhh... You still there?")

#for loop with range
for num in range(10):
    print(num)

#array printing
for x in arr:
    print(x)

print(len(arr))

#index iteration while loop
iteration = 0
while iteration < 6:
    print(iteration)
    iteration += 1

#adding two numbers together
def addNums(inp1, inp2):
    tot = inp1 + inp2
    print(tot)

addNums(2, 5)

def oddOrEven(inp1):
    if inp1 % 2 == 0:
        print(inp1, " is even!")

    else:
        print(inp1, " is odd!")

#Dog class part
class Dog(object):
    def __init__(self, name, height, weight, breed):
        self.name = name
        self.height = height
        self.weight = weight
        self.breed = breed

    def info(self):
        print("Name:", self.name)
        print("Weight:", str(self.weight) + " Pounds")
        print("Height:", str(self.height) + " Inches")
        print("Breed:", self.breed)

Bailey = Dog("Bailey", "7", "12", "Pug")
Bailey.info()
