
N = int(input())

inf = 1000000000
ans = inf

for i in range(N):
	x, y = map(int, input().split())
	if x <= y:
		ans = min(ans, y)


if ans == inf:
	print(-1)
else:
	print(ans)