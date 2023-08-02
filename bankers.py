def findID(finish, id, n):
 flag = 0
 for i in range(n):
 if finish[i] == 0:
 flag = 1
 break
 if flag == 0:
 return -1
 else:
 if finish[id] == 1:
 return -2
 else:
 return 0
def computeAvail(total, alloc, n, m):
 available = [0] * m
 allocation = [0] * m

 for j in range(m):
 for i in range(n):
 allocation[j] += alloc[i][j]
 available[j] = total[j] - allocation[j]
 return available
def printTable(maxim, alloc, need, avail):
 print('Max Alloc Need Avail')
 for i in range(n):
 for j in range(m):
 print(maxim[i][j],end=" ")
 print(" ",end="")
 for j in range(m):
 print(alloc[i][j],end=" ")
 print(" ",end="")
 for j in range(m):
 print(need[i][j],end=" ")
 print(" ",end="")
 if(i==0):
 for j in range(m):
 print(avail[j],end=" ")
 print()

def bankers(maxim, alloc, total, n, m):
 finish = [False] * n
 safe = [-1] * n
 need = []
 for i in range(n):
 a = []
 for j in range(m):
 a.append(maxim[i][j] - alloc[i][j])
 need.append(a)
 avail = computeAvail(total, alloc, n, m)
 work = avail.copy()
 id = 0
 k = 0
 while True:
 status = findID(finish, id, n)
 if status == -2:
 id = (id + 1) % n
 elif status == -1:
 break
 else:
 flag = 0
 for j in range(m):
 if need[id][j] > work[j]:
 flag = 1
 break
 if flag == 0:
 for j in range(m):
 work[j] += alloc[id][j]
 safe[k] = id
 k += 1
 finish[id] = 1
 id = (id + 1) % n
 else:
 id = (id + 1) % n
 return need, avail, safe
n = int(input())
m = int(input())
maxim = []
for i in range(n):
 a = []
 for j in range(m):
 a.append(int(input()))
 maxim.append(a)
alloc = []
for i in range(n):
 b = []
 for j in range(m):
 b.append(int(input()))
 alloc.append(b)
total = []
for j in range(m):
 c = int(input())
 total.append(c)
need, avail, safe = bankers(maxim, alloc, total, n, m)
print("The system is safe.\n")
printTable(maxim, alloc, need, avail)
seq = []
for i in range(n):
 seq.append('P' + str(safe[i]))
print('\nSafe Seequence is : ', tuple(seq))
