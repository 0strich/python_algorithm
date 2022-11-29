import sys
import heapq

N = int(sys.stdin.readline())
heap = []
output = []
for _ in range(N):
	x = int(sys.stdin.readline())
	if x: heapq.heappush(heap, -x)
	else: output.append(-heapq.heappop(heap)) if heap else output.append(0)
print("\n".join(map(str, output)))