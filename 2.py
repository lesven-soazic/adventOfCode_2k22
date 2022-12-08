def countPoints(set):
    sumOfPoints = 0
    for content in set:
        if content in winningCombinaison :
            sumOfPoints+=6

        elif content in doubleCombinaison :
            sumOfPoints+=3

        sumOfPoints+=points[content[-1]]
        
    return(sumOfPoints)


def part2(liste): 
    liste2 = liste.copy()

    for idx, content in enumerate(liste) : 
        instructions = content[-1]

        if instructions == "X":
            liste2[idx] = [elem for elem in losingCombinaison if content[0] in elem][0]

        elif instructions == "Y":
            liste2[idx] = [elem for elem in doubleCombinaison if content[0] in elem][0]

        elif instructions == "Z":
            liste2[idx] = [elem for elem in winningCombinaison if content[0] in elem][0]

    return liste2





winningCombinaison = ["A Y","B Z", "C X"]
losingCombinaison = ["A Z","B X", "C Y"]
doubleCombinaison = ["A X","B Y", "C Z"]
points = {"X":1, "Y":2, "Z":3}
correspondances = {"A":"X", "B":"Y", "C":"Z"}

pathOfFile = 'input_d2.txt'

with open(pathOfFile) as file:
    fileContent = file.readlines()

fileContent_stripped=[content.strip() for content in fileContent]
modifyFileContent = part2(fileContent_stripped)

print(countPoints(fileContent_stripped))
print(countPoints(modifyFileContent))
