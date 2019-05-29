c = dict()
c['tesoura'] = ['papel','lagarto']
c['papel'] = ['pedra','Spock']
c['pedra'] = ['lagarto','tesoura']
c['lagarto'] = ['Spock','papel']
c['Spock'] = ['tesoura','pedra']

n = int(input())
for i in range(1, n+1):
    sheldon, raj = input().split()
    if raj in c[sheldon]:
        print('Caso #{:d}: Bazinga!'.format(i))
    elif sheldon in c[raj]:
        print('Caso #{:d}: Raj trapaceou!'.format(i))
    else:
        print('Caso #{:d}: De novo!'.format(i))