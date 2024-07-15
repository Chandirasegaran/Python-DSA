# main.py

import math
from Taxi import Taxi

def createTaxis(n):
    taxis = []
    for i in range(n):
        t = Taxi()
        taxis.append(t)
    return taxis

def getFreeTaxis(taxis, pickup, pickupTime):
    freeTaxi = []
    for taxi in taxis:
        if taxi.freeTime <= pickupTime and math.fabs(ord(taxi.currentSpot) - ord(pickup)) <= pickupTime - taxi.freeTime:
            freeTaxi.append(taxi)
    return freeTaxi

def bookTaxi(customerId, pickup, dropoff, pickupTime, taxis):
    MIN = 999
    bookedTaxi = None
    distanceBetweenPickupAndDrop = None
    earnings = 0
    nextFreeTime = 0
    nextSpot = 'Z'
    tripDetail = ""

    for taxi in taxis:
        distanceBetweenCustomerAndTaxi = math.fabs(ord(taxi.currentSpot) - ord(pickup)) * 15
        if distanceBetweenCustomerAndTaxi < MIN:
            MIN = distanceBetweenCustomerAndTaxi
            bookedTaxi = taxi
            distanceBetweenPickupAndDrop = math.fabs(ord(dropoff) - ord(pickup)) * 15
            earnings = (distanceBetweenPickupAndDrop - 5) * 10 + 100
            dropTime = pickupTime + distanceBetweenPickupAndDrop / 15
            nextFreeTime = dropTime
            nextSpot = dropoff
            tripDetail = f"{taxi.id:<12}{customerId:<12}{pickup:<6}{dropoff:<6}{pickupTime:<12}{dropTime:<10}{earnings:.2f}"

    bookedTaxi.setDetails(True, nextSpot, nextFreeTime, bookedTaxi.totalEarnings + earnings, tripDetail)
    print(f"Taxi {bookedTaxi.id} booked")

def main():
    taxis = createTaxis(4)
    id = 1

    while True:
        print("--------------------------------------------------------------------------------------")
        print("Welcome to Taxi Booking")
        print("1 -> Book Taxi")
        print("2 -> View Taxi Details")
        print("3 -> Exit Taxi Booking")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 1:
            customerId = id
            print("The Available Locations are A,B,C,D,E,F")
            pickup = input("Enter pickup Point: ").upper()
            dropoff = input("Enter dropoff Point: ").upper()

            try:
                pickupTime = int(input("Enter pickup Time: "))
            except ValueError:
                print("Invalid pickup time")
                continue

            if pickup < 'A' or pickup > 'F' or dropoff > 'F' or dropoff < 'A':
                print("Invalid pickup")
                continue

            freeTaxis = getFreeTaxis(taxis, pickup, pickupTime)

            if len(freeTaxis) == 0:
                print("No Taxi available")
                continue

            freeTaxis.sort(key=lambda t: t.totalEarnings)

            bookTaxi(customerId, pickup, dropoff, pickupTime, freeTaxis)

            id += 1

        elif choice == 2:
            for taxi in taxis:
                taxi.printTaxi()

        elif choice == 3:
            print("Thank you for using Taxi Booking")
            exit(0)
        else:
            print("Invalid choice")
            continue

if __name__ == '__main__':
    main()

