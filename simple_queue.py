
stack = ([1,2,3,4,5]) 
print('antrian sekarang:', stack)

stack.append(6)

print('antrian masuk:', 6)
print('antrian sekarang:', stack)

stack.append(7)

print('antrian masuk:', 7)
print('antrian sekarang', stack)

out = stack.popleft()

print('antrian keluar:', out) 
print('antrian sekarang:',stack)
