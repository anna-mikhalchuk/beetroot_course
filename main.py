import random


class Trip:
    def __init__(self, traveler_name, traveler_age):
        self.traveler_name = traveler_name
        self.traveler_age = traveler_age
        self.citycost = {
            "kyiv": 890,
            "kharkiv": 723,
            "odessa": 472,
            "poltava": 177,
            "dnipro": 200,
            "lviv": 403
        }
        print "Please input amount of nights"
        self.nights = input()

        print "Please choose one of the city: Kyiv, Kharkiv, Odessa, Poltava, Dnipro, Lviv"
        self.city = raw_input().lower()

    def plane_city_cost(self):
        plane_city_amount = 0
        if self.city in self.citycost:
            k = self.city
            plane_city_amount = self.citycost.get(k)
            return plane_city_amount
        else:
            print "Sorry, No matches found"
            return plane_city_amount

    print "The plane ride cost", plane_city_cost()

    def hotel_cost(self):
        hotel_amount = 140 * self.nights
        return hotel_amount

    print "The hotel cost is", hotel_cost()

    def rental_car_cost(self):
        cost = 40 * self.days
        if 7 > self.days >= 3:
            cost -= 20
        elif self.days >= 7:
            cost -= 50
        return cost

    print "The rental car cost is", rental_car_cost()

    def spending_money():
        print random.randint(99, 1001)
        return random.randint(99, 1001)

    def common_trip_cost(self):
        common_trip_amount = self.rental_car_cost() + self.hotel_cost() + self.plane_city_cost() + self.spending_money()
        return common_trip_amount

    print "Common trip price is", common_trip_cost()

    print "Please input amount of days for car rent"
    days = input()


first = Trip("Anna", 26)
first.plane_city_cost()
first.hotel_cost()
first.rental_car_cost()
first.spending_money()
first.common_trip_cost()

