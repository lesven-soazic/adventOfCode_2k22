def findCommonLetters1(rucksacks):
    commonLetters = []

    for rucksack in rucksacks : 
        for letter in rucksack[0]:
            if letter in rucksack[1]:
                commonLetters.append(letter)
                break
    return(commonLetters)

def calculatePriorities(liste):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return sum(alphabet.index(letter)+1 for letter in liste)

def findCommonLetters2(rucksacks):
    commonLetters = []

    for rucksack in rucksacks : 
        for letter in rucksack[0]:
            if letter in rucksack[1] and letter in rucksack[2]:
                commonLetters.append(letter)
                break
    return(commonLetters)


filePath = "input_d3.txt"

with open(filePath) as file:
    fileContent = file.readlines()

rucksacks1 = [[elem[:len(elem)//2],elem[len(elem)//2:]] for elem in fileContent]
priorities = findCommonLetters1(rucksacks1)
print(calculatePriorities(priorities))


rucksacks2 = [[fileContent[i],fileContent[i+1],fileContent[i+2]] for i in range(0,len(fileContent),3)]
priorities = findCommonLetters2(rucksacks2)
print(calculatePriorities(priorities))
