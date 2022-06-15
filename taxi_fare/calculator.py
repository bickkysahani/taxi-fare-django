import datetime

INITIAL_FARE = 25.00
FARE_PER_KILOMETER = 14.00

def calculate_fare(distance, time):
    print('calculate_fare')
    print(distance,type(distance))
    print(time, type(time))
    #time in am between 5am and 6am 
    if time > datetime.time(5) and time < datetime.time(7):
        #add 10% surcharge to the fare + inital fare of 25 + km fare
        return INITIAL_FARE + (distance * FARE_PER_KILOMETER) + ((distance * FARE_PER_KILOMETER * 0.1))
    elif time >= datetime.time(7) and time < datetime.time(21):
           return INITIAL_FARE + (distance * FARE_PER_KILOMETER)
    elif time >= datetime.time(21) and time < datetime.time(23):
            #add 15% surcharge to the fare
            return INITIAL_FARE + (distance * FARE_PER_KILOMETER) + ((distance * FARE_PER_KILOMETER * 0.15))
    elif time >= datetime.time(23):
        #add 20% surcharge to the fare
        return INITIAL_FARE + (distance * FARE_PER_KILOMETER) + ((distance * FARE_PER_KILOMETER * 0.2))
    elif time >=datetime.time(0) and time <= datetime.time(5):
        #add 50% surcharge to the fare and 5% service charge
        return INITIAL_FARE + (distance * FARE_PER_KILOMETER) + ((distance * FARE_PER_KILOMETER * 0.5)) + ((distance * FARE_PER_KILOMETER * 0.05))
    else:
        return INITIAL_FARE + (distance * FARE_PER_KILOMETER)