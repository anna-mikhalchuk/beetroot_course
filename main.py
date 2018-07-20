import random
from dictionary import citycost


class Trip:
    def __init__(self, traveler_name, traveler_age, city, nights, days):
        self.traveler_name = traveler_name
        self.traveler_age = traveler_age
        self.city = city
        self.citycost = citycost
        self.days = days
        self.nights = nights

    #@property
    def plane_city_cost(self):
        self.plane_city_amount = 0
        if self.city in self.citycost:
            k = self.city
            self.plane_city_amount = self.citycost.get(k)
            return self.plane_city_amount
        else:
            print "Sorry, No matches found"
            return self.plane_city_amount

    #@property
    def hotel_cost(self):
        hotel_amount = 140 * self.nights
        return hotel_amount

    #@property
    def rental_car_cost(self):
        cost = 40 * self.days
        if 7 > self.days >= 3:
            cost -= 20
        elif self.days >= 7:
            cost -= 50
        return cost

   # @property
    def spending_money(self):
        return random.randint(99, 1001)

    #@property
    def common_trip_cost(self):
        common_trip_amount = self.rental_car_cost() + self.hotel_cost() + self.plane_city_cost() + self.spending_money()
        return common_trip_amount


print "Please choose one of the city: Kyiv, Kharkiv, Odessa, Poltava, Dnipro, Lviv"
city = raw_input().lower()
print "Please input amount of nights"
nights = input()
print "Please input amount of days for car rent"
days = input()

first = Trip("Anna", 26, city, nights, days)

print "The plane ride cost", first.plane_city_cost()
print "The hotel cost is", first.hotel_cost()
print "The rental car cost is", first.rental_car_cost()
print "Common trip price is", first.common_trip_cost()
print "Spending money", first.spending_money()




