def minimumNumberOfCoins(coins,numberOfCoins,value):
    required = [99999999] * (value + 1)
    required[0] = 0
    for coin in coins:
        for i in range(1, value + 1):
            if i >= coin:
                required[i] = min(required[i], required[i - coin] + 1)
    if required[value] == 99999999:
        return -1
    return required[value]

def main():
    testcases = int(input('Enter the number of test cases:- '))
    while(testcases>0):
        value = int(input('Enter teh value to be formed:- '))
        numberOfCoins = int(input('Enter how many couns do you have:- '))
        coins = [int(x) for x in input('Enter the value of coins:- ').strip().split()]
        answer=minimumNumberOfCoins(coins,numberOfCoins,value)
        print("Not Possible") if answer == -1 else print(answer)
        testcases-=1

if __name__=="__main__":
    main()