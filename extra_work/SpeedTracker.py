distance = float(input('enter the distance between the 2 speed cameras (m): '))
time = float(input('enter the time the car took to pass them both (s): '))
spdlmt = int(input('enter the speed limit (m/s)'))
numplate = input('enter the number plate: ').strip().lower()
spd = distance / time
if spd > spdlmt:                                        
    print('YOUR GOING TO FAST. SLOW DOWN')
else:
    print('good booyyy your driving like a safe person :3')
