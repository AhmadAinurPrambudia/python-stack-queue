fromcollectionsimportdeque

queue= deque([1,2,3,4,5])
print('antriansekarang:',queue)

queue.append(6)
print('antrianmasuk:',6)
print('antriansekarang:',queue)

queue.append(7)
print('antrianmasuk:',7)
print('antriansekarang:',queue)

out=queue.popleft()
print('antriankeluar:',out)
print('antriansekarang: ',queue)
