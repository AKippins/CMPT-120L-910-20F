def sum_2d_array(two_d_array):
    
    one_d_array = []
    
    for x in range(len(two_d_array)):
        
        tot = 0
        tot = sum(two_d_array[x])
        ##for i in range(len(two_d_array[x])):
            ##tot = tot + sum(two_d_array[int(x)])
        ##I thought i could do it this way but was way over thinking it lol
            
        one_d_array.append(tot)

    return one_d_array
    pass

if __name__ == "__main__":
    two_d_array = [
        [2, 6, 7, 98, 3, 434, 2, 4, 2],
        [-12, 3, 454, 6778, 234, -999, 2543, -2323],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [],
        [1000000000000000],
        [1],
        [0]
        ]
    answers = sum_2d_array(two_d_array)
    
    print(answers)
