
filecompare = 'CompareList.txt'
filecompare.strip()

fileinput = 'FakeInputList.txt'
fileinput.strip()

allergies = []
with open (filecompare, 'r') as infile:
    for line in infile:
        allergies.append(line.strip("\n").strip().lower())

ingredients = []
with open (fileinput, 'r') as infile:
    for line in infile:
        ingredients.append(line.strip("\n").strip().lower())

dict1 = {}
for i in range(len(allergies)):
    dict1[allergies[i]] = 1

out = "The ingredients "
for i in range(len(ingredients)):
    if ingredients[i] in dict1:
        out += ingredients[i]+", "

out = out[:len(out)-2]
tempint = out.rindex(",")
out = out[:tempint+1] + " and" + out[tempint+1:]
out += " may cause allergies."
print(out)
