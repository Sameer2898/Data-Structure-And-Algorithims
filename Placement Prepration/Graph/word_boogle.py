rr = [-1,-1,-1, 0, 0, 1, 1, 1]
cc = [-1, 0, 1,-1, 1,-1, 0, 1]

def is_valid(board,r,c):
    if( r<0 or r>=len(board) ):
        return False
    if( c<0 or c>=len(board[r]) ):
        return False
    return True

def match(board,r,c,word,index):
    if index is len(word):                                           
        return True
    char=board[r][c]
    board[r][c]='0'                                                  
    for i in range(8):
        nextr=r+rr[i]
        nextc=c+cc[i]
        if is_valid(board,nextr,nextc) is True:                      
            if board[nextr][nextc] is word[index]:                   
                if match(board,nextr,nextc,word,index+1) is True:
                    board[r][c]=char                                 
                    return True
    board[r][c]=char                                                
    return False

def boggle(board,dictionary):
    ret=[]
    for i in dictionary:
        found=False
        for j in range(len(board)):
            if(found):
                break                         
            for k in range(len(board[j])):
                if(found):
                    break                      
                if board[j][k] is i[0]:        
                    if(match(board,j,k,i,1)):  
                        ret.append(i)
                        found=True
    return ret

def main():
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter how many words you want to enter in an dictionary:- '))
        dictionary = [x for x in input('Enter the words:- ').strip().split()]
        line = input('Enter the word to be search:- ').strip().split()
        r = int(line[0])
        c = int(line[1])
        board = []
        for _ in range(r):
            board.append( [x for x in input().strip().split()] )
        found = boggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
        
    
if __name__ == "__main__":
    main()