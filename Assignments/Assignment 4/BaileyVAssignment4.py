class Number:
    def numSum(num):
        count = []
        for x in range(1, (num+1)):
            count.append(x)
            print(sum(count))


    if __name__ == "__main__":
        num = int(input("Enter A Number: "))
        numSum(num)

