def printList():
  for i in range(len(names)):
    print(names[i] + ', ' + phones[i] + ', ' + dobs[i] + ', ' + areas[i] +
    ', ' + areaCodes[i])

names = ['Stefan', 'Joan', 'Martin']
phones = ['088-123 456', '01-245 7738', '086-113 3557']
dobs = ['21/01/2001', '14/02/2002', '27/12/1998']
areas = ['Raheny', 'Baldoyle', 'Marino']
areaCodes = ['Dublin 5', 'Dublin 13', 'Dublin 3']

printList()

newName = input('Enter a name:')
names.append(newName)
newPhone = input('Enter a phone:')
phones.append(newPhone)
newDob = input('Enter a dob:')
dobs.append(newDob)
newArea = input('Enter a area:')
areas.append(newArea)
newAreaCode = input('Enter a area code:')
areaCodes.append(newAreaCode)

printList()