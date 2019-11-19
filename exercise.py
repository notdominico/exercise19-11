people = ['Dyl','Eric','Wais','Lay']
greetings = "Dear"
invitation = "you are coordinally invited to my dinner party"
print(greetings,people, invitation)
unavailable = 'Eric'
people.remove(unavailable)
print(people)

print(greetings, people, invitation)
people.insert(0,'Patrick')
people.insert(2,'Yowen')
people.append('Vincent')
print(greetings, people, invitation)

people.pop(0)
for i in range (3) :
    people.pop(i)
print(greetings, people, invitation)

del people [0:2]
print(greetings, people, invitation)

places = ['Malta','Berlin','New Zealand','Moscow','Shanghai']
print(places)
print(sorted(places))
places.reverse()
print(places)
places.sort(reverse=True)
print(places)
