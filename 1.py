listOfElf=[]
liste=[]
for elem in fileContent :
    if len(elem)>1:
        liste.append(int(elem.split('\n')[0]))

    else :
        listOfElf.append(liste)
        liste=[]


sumListOfElf = sorted([sum(elem) for elem in listOfElf])


print(np.sum(sumListOfElf[-3:]))
