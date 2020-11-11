from math import ceil
from math import sqrt

def prime_or_composite(number):
    
    primeNum = True
    
    if number > 1:
        for i in range(2, math.ceil(sqrt(number))):
            if number % i == 0:
                primeNum = False
                break

            else:
                primeNum = True
                
        if primeNum:
           print (number, "is prime.")

        elif number <= 1:
            primeNum = False
    
    pass
    
if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))

    ##I removed the print(answers) because I feel like this above code is more efficent.
    ##forigve me if i'm wrong. 
