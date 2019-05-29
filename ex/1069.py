n = int(input())
for i in range(n):
    a = list(input().replace('.', ''))
    encontrou = True
    cont = 0
    while encontrou:
        encontrou = False
        for i in range(len(a)-1):
            if a[i] == '<' and a[i+1] == '>':
                a.pop(i)
                a.pop(i)
                cont += 1
                encontrou = True
                break
    print(cont)