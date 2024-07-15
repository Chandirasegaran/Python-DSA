# Taxi.py

class Taxi:
    no_of_taxi = 0

    def __init__(self):
        self.booked = False
        self.currentSpot = 'A'
        self.freeTime = 4
        self.totalEarnings = 0
        self.trips = []
        Taxi.no_of_taxi += 1
        self.id = Taxi.no_of_taxi

    def setDetails(self, booked, currentSpot, freeTime, totalEarnings, tripDetail):
        self.booked = booked
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.totalEarnings = totalEarnings
        self.trips.append(tripDetail)

    def printTaxi(self):
        print("--------------------------------------------------------------------------------------")
        print(f"Taxi - {self.id} | Total Earnings {self.totalEarnings:.2f}")
        print("--------------------------------------------------------------------------------------")
        print(
            f"{'TaxiID':<8}{'BookingID':<12}{'CustomerID':<12}{'From':<6}{'To':<6}{'PickUpTime':<12}{'DropTime':<10}{'Amount'}")
        for trip in self.trips:
            print(f"{self.id:<8}{trip}")
