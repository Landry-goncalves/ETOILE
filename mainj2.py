if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    content = fichier.read()

    montableau = [ int(i) for i in content.split('\n')]
    for i in montableau:
        for j in montableau:
            for k in montableau:
                somme= i + j + k
                if somme == 2020:
                    print(i*j*k)
