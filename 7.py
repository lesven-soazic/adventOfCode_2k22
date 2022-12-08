currentDirectory = ""
directory={}
historic = []
totalSum = 0


with open("input_d7.txt") as file :
    fileContent = file.readlines()


for line in fileContent :
    line=line.strip()

    if "$ cd .." in line :
        currentDirectory=historic[-1]
        del historic[-1]



    elif "$ cd" in line :
        currentDirectory= line.split("$ cd")[-1]
        historic.append(currentDirectory)

        directory[currentDirectory] = []


    elif line[0].isnumeric():
        directory[historic[-1]].append(line.split(" ")[0])


    elif "dir" in line :
        directory[currentDirectory].append(line.split("dir")[-1])


reversedKeys = list(directory.keys())
reversedKeys.reverse()

def count(liste, previousSum):
    
    for elem in liste :

        if elem.isnumeric():
            previousSum+=int(elem)

        else : 
            previousSum+=count(directory[elem], previousSum)

    return previousSum



for key in reversedKeys:
    sumDirectory = count(directory[key],0)
    
    if sumDirectory<100000:
        totalSum+=sumDirectory

print(totalSum)