import atexit
import io
import sys

def JobScheduling(jobs,n):
    ans, count = 0, 0
    jobs = sorted(jobs, key = lambda x: x.profit, reverse=True)
    answer = [0 for i in range(n)]
    slot = [False for i in range(n)]
    for i in range(n):
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if not slot[j]:
                answer[j] = i
                slot[j] = True
                break
    for i in range(n):
        if slot[i]:
            ans += jobs[answer[i]].profit
            count += 1
    ans_ans = []
    ans_ans.append(count)
    ans_ans.append(ans)
    return ans_ans

class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n = int(input('Enter the size of the list:- '))
        info = list(map(int,input('Enter the elements of the list:- ').strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        res = JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])