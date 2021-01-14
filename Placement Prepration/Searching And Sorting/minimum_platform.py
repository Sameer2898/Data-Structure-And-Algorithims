import atexit
import io
import sys

def minimumPlatform(n,arr,dep):
    platform = 1
    order = []
    for i in range(n):
        order.append([arr[i], 0])
        order.append([dep[i], 1])
    order = sorted(order, key=lambda x: (x[0], x[1]))
    required = 0
    for i in range(2*n):
        if order[i][1] == 0:
            required += 1
            platform = max(platform, required)
        else:
            if required:
                required -= 1
    return platform

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:_ '))
    for cases in range(test_cases) :
        n = int(input('Enter the size of the array:- '))
        arrival = list(map(str,input('Enter the arrival array:- ').strip().split()))
        departure = list(map(str,input('Enter the deprature array:- ').strip().split()))
        print(minimumPlatform(n,arrival,departure))