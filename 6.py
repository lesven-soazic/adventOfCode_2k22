with open("input_d6.txt") as file :
    fileContent = list(file.readlines()[0])

numberOfDiffCaracters = 14
chaine = fileContent[:numberOfDiffCaracters].copy()


for idx,elem in enumerate(fileContent[numberOfDiffCaracters:]):
    del chaine[0]
    chaine.append(elem)

    counter = 0
    for ec1 in chaine :
        for ec2 in chaine :
            if ec1 == ec2:
                counter +=1

    if counter==numberOfDiffCaracters:
        print(idx+numberOfDiffCaracters+1)
        break

