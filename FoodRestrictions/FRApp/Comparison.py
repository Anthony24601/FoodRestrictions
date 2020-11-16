from django.db import models

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

#This will be some input that we can change the code for later
num_id = 1

dataevent = Event.objects.get(id=num_id)

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
