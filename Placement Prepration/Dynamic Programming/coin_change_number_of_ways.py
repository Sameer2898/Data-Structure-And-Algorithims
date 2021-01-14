def numberOfWays(coins,numberOfCoins,value):
    ways = [0] * (value + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(1, value + 1):
            if i >= coin:
                ways[i] = ways[i] + ways[i - coin]
    return ways[value]

def main():
    testcases = int(input('Enter the number of test cases:- '))
    while(testcases>0):
        value = int(input('Enter teh value to be formed:- '))
        numberOfCoins = int(input('Enter how many couns do you have:- '))
        coins = [int(x) for x in input('Enter the value of coins:- ').strip().split()]
        print(numberOfWays(coins,numberOfCoins,value))
        testcases -= 1

if __name__=="__main__":
    main()