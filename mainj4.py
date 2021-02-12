if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    content = fichier.read()

    table = [i for i in content.split('\n')]
    lettre1ok = 0
    lettre2ok = 0

    for i in table:
        s = i.split(' ')
        min = int(s[0].split('-')[0])
        max = int(s[0].split('-')[1].split(' ')[0])
        mdp = i.split(' ')[2].split(min)
        mdp = i.split(' ')[2].split(max)
        lettre = s[1].split(":")[0]
        count = mdp.count(lettre)






        if min<=count<=max :
            mdpOk = mdpOk+1

    print(mdpOk)






