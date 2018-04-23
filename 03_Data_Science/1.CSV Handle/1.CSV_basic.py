import csv

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
    data = list(csv.reader(infile))

#Count Participants
countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': "+ str(countParticipantsIndex))

countParticipants = []
#index = 0

for row in data[1:]:
    countParticipants.append(row[countParticipantsIndex])

print("<COUNT PARTICIPANTS>")
for participant in countParticipants:
    print(participant)


#Count Female
countParticipantsIndex = data[0].index("COUNT FEMALE")
print("The index of 'COUNT FEMALE': "+ str(countParticipantsIndex))

countParticipants = []
#index = 0

for row in data[1:]:
    countParticipants.append(row[countParticipantsIndex])

print("<COUNT FEMALE>")
for participant in countParticipants:
    print(participant)