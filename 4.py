inputPath = 'input_d4.txt'

with open(inputPath) as file :
    fileContent = file.readlines()


pairsOfElf = [elem.strip().split(',') for elem in fileContent]

sections = []
for pair in pairsOfElf:
    liste1=[]
    for elf in pair :
        [a,b]= elf.split('-')

        liste1.append(list(range(int(a),int(b)+1)))
    sections.append(liste1)


counter=0
for [lst1,lst2] in sections:
    intersection = set(lst1) & set(lst2)

    if len(intersection) in [len(lst1), len(lst2)]:
        counter+=1
print("part 1 : ", counter)



counter=0
for [lst1,lst2] in sections:
    intersection = set(lst1) & set(lst2)
    if len(intersection)!=0 :
        counter+=1
print("part 2 : ", counter)