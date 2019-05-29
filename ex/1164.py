n = int(input())
for i in range(n):
   x = int(input())
   divs = filter(lambda d : (x % d) == 0, range(1,x))   
   if x == sum(divs):
       print('{:d} eh perfeito'.format(x))
   else:
       print('{:d} nao eh perfeito'.format(x))