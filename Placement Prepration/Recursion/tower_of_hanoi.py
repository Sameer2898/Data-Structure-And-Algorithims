def toh(N, fromm, to, aux):
    if N == 1:
        print('move disk '+ str(N) + ' from rod ' + str(fromm) + ' to rod ' + str(to))
        return 1
    moves = 0
    moves += toh(N - 1, fromm, aux, to)
    moves += 1
    print('move disk ' + str(N) + ' from rod ' + str(fromm) + ' to rod ' + str(to))
    moves += toh(N-1, aux, to, fromm)
    return moves

def main():
    T = int(input('Enter the number of test cases:- '))
    while(T > 0):
        N = int(input('Enter a number:- '))
        print(toh(N, 1, 3, 2))
        T -= 1

if __name__ == "__main__":
    main()