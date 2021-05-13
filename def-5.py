city = input("Enter city:")
nights =int( input("Enter nights:"))
days =int(input("How many days of car rental:"))
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
        if city == "Charlotte":
            return 183
        elif city == "Tampa":
            return 220
        elif city == "Pittsburgh":
            return 222
        elif city == "Los Angeles":
            return 475

def rental_car_cost(days):

        if days >= 7:
            cost = (days * 40)-50
        elif days >= 3:
            cost = (days * 40)- 20
        else:
            cost = days * 40
        return cost;

def trip_cost(city, days,):
    print(rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city))

trip_cost(city, days)