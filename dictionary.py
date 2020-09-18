states = {
 'haryana' : 'Hr',
 'bihar' : 'bh'
}

cities = {
 'Hr':'faridabad',
'bh' : 'patna'
}

cities['up'] = 'lucknow'

print(states)
print(cities)
print('-'*10)
print("hr state has:", cities['Hr'])
print("bh state has:", cities['bh'])


for state, abbrevation in states.items():
 print(f"{state} is abbrevated {abbrevation}")

 
print(states.get('bihar'))

x = [5,6,8]
if not x :
 print("list is empty")
else :
 print("list is filled")
