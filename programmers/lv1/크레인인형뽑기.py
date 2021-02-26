def solution(board, moves):
    answer = 0    
    stack = []

    for i in moves:

        cnt = 0
        while cnt < len(board): 

            if board[cnt][i - 1] != 0:
                if stack[-1:] == [board[cnt][i - 1]]:
                        answer += 2
                        stack.pop()                    
                else:
                    stack.append(board[cnt][i - 1])

                board[cnt][i - 1] = 0
                cnt = len(board)

            cnt +=1

    return answer

###############################################################

def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer