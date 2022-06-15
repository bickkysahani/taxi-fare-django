import datetime

INITIAL_FARE = 25.00
FARE_PER_KILOMETER = 14.00

def calculate_fare(distance, time):
    print('calculate_fare')
    print(distance,type(distance))
    print(time, type(time))
    fare = distance * FARE_PER_KILOMETER

    #time in am between 5am and 6am 
    if time > datetime.time(5) and time < datetime.time(7):
        print('time in am between 5am and 7am')
        #add 10% surcharge to the fare + inital fare
        return INITIAL_FARE + fare + (fare * 0.1)

    if time >= datetime.time(7) and time < datetime.time(21):
        print('time in pm between 7am and 9pm')
        return INITIAL_FARE + fare

    if time >= datetime.time(21) and time < datetime.time(23):
        print('time in pm between 9pm and 11pm')
        #add 15% surcharge to the fare
        return INITIAL_FARE + fare + (fare * 0.15)

    if time >= datetime.time(23):
        print('time in pm between 11pm and 12am')
        #add 20% surcharge to the fare
        return INITIAL_FARE + fare + (fare * 0.2)

    if time >=datetime.time(0) and time <= datetime.time(5):
        print('time in am between 12am and 5am')
        #add 50% surcharge to the fare and 5% service charge
        return INITIAL_FARE + fare + (fare * 0.5) + (fare * 0.05)
