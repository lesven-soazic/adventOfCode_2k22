crates = {
    "1":["F","C", "P", "G", "Q", "R"],
    "2":["W","T", "C","P"],
    "3":["B","H", "P", "M", "C"],
    "4":["L","T", "Q", "S", "M", "P","R"],
    "5":["P","H", "J", "Z", "V", "G","N"],
    "6":["D","P", "J"],
    "7":["L","G", "P", "Z", "F", "J","T","R"],
    "8":["N","L", "H", "C", "F", "P","T","J"],
    "9":["G","V", "Z", "Q", "H", "T","C","W"],
    # "1":["Z","N"],
    # "2":["M","C", "D"],
    # "3":["P"]
}

def part1(text, inputDict):
    for content in text:
        numberOfMove = int(content.split("from")[0].split("move")[-1])
        entryOrigin = str(int(content.split("from")[-1].split("to")[0]))
        entryDestination = str(int(content.split("from")[-1].split("to")[-1]))

        for _ in range(numberOfMove):
            element = inputDict[entryOrigin].pop(-1)
            inputDict[entryDestination].append(element)

    variable = "".join(crate[-1] for crate in inputDict.values())
    print(variable)


def part2(text, inputDict):
    for content in text:
        numberOfMove = int(content.split("from")[0].split("move")[-1])
        entryOrigin = str(int(content.split("from")[-1].split("to")[0]))
        entryDestination = str(int(content.split("from")[-1].split("to")[-1]))

        liste=[]
        for _ in range(numberOfMove):
            element = inputDict[entryOrigin].pop(-1)
            liste.append(element)


        liste.reverse()
        for elem in liste :
            inputDict[entryDestination].append(elem)

    variable = "".join(crate[-1] for crate in inputDict.values())
    print(variable)


with open("input_d5.txt") as file: 
    fileContent = file.readlines()

part2(fileContent, crates)