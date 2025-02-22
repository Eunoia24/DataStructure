import sys
input = sys.stdin.readline

k = int(input())
sign = input().split()

visited = [False for _ in range(10)]
max_ans = ""
min_ans = ""

def check(i, j, k):
    if k == ">":
        return i > j
    else:
        return i < j
    
def solve(depth, s):
    global max_ans, min_ans

    if depth == k + 1:
        max_ans = s
        if len(min_ans) == 0:
            min_ans = s
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), sign[depth-1]):
                visited[i] = True
                solve(depth + 1, s + str(i))
                visited[i] = False

solve(0, "")
print(max_ans)
print(min_ans)