def leap_year(x):
    """
    - Add code in the defined function to figure out whether or not the given x is a leap x or not. 
    
    - Every x that is exactly divisible by four is a leap x, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are. - Wikipedia
    
    - Take in a parameter called x and return “Is a leap x” or “Not a leap x”
    """
    # Write your code here. 

if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    ##answers = []
    for x in range(0, len(years)):
        if years[x] % 4 == 0:
            if years[x] % 100 == 0:
                if years[x] % 400 == 0:
                    print(years[x], "is a leap year.")
                else:
                    print(years[x], "is not a leap year.")
            else:
                print(years[x], "is a leap year.")
        else:
            print(years[x], "is not a leap year.")
    ##answers.append(leap_year(x))
    ##print(answers)
            
    ##My reasoning for noting out the answers array list and the appending to it, is because if we want to
    ##return if each index of the years array is a leap year or not, theres no need to add the ones that are to a seperate array just to print that, when
    ##The code could sort through each index individually and give the answer within its own array.

    ##I suppose another way I could have done it is by adding the leap years to the answer array and making another for loop just to
    ##iterate through like so
            ##for i in answers:
                ##print(i + "is a leap year.") but that feels kind of silly to do. So I didn't. 
