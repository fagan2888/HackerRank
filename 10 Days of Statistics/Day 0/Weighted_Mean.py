# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
mean = sum([a*b for a,b in zip(x,w)])
print(round((mean/sum(w)),1))
