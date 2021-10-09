import heapq

pq=[5,20,1,30,4]

heapq.heapify(pq)

print(pq)

print(heapq.heappushpop(pq,2))

print(pq)


print("ans",heapq.heappushpop(pq,0))

print("ele",pq)


print(heapq.heapreplace(pq,-1))
print(pq)
