import datetime
from hashTable import package_hash_table, distances, addresses


#Represents a delivery truck and its associated packages
# Time complexity: O(1)
class Truck:
    def __init__(self, packages, mileage, current_address, current_time):
        self.current_time = current_time
        self.current_address = current_address
        self.mileage = mileage
        self.packages = packages

    def __str__(self):  
        return "{}, {}, {}, {}".format(
            self.packages, self.mileage, self.current_address, self.current_time)


# Update the delivery info for a package.
# Time complexity: O(1)
def update_package_info(package, depart_hub_time, current_time):
    package.time_left_hub = depart_hub_time
    package.status = "Delivered"
    package.time_delivered = current_time
    package_hash_table.insert(package.package_id, package)

# Update address for a special package case.
# Time complexity: O(1)
def update_special_case(package, current_time):
    if current_time >= datetime.timedelta(hours=10, minutes=20) and package.package_id == 9:
        package.address = "410 S State St"
        package.zipcode = "84111"
        package_hash_table.insert(package.package_id, package)

# Update the truck info for each stop.
# Time complexity: O(1)
def update_truck_info(truck, next_stop, distance, del_time):
    truck.mileage += distance
    truck.current_time += datetime.timedelta(hours=del_time)
    truck.current_address = next_stop

# Deliver all packages on a truck.
# Time complexity: O(n^2)
def deliver_packages(truck):
    starting_location = truck.current_address
    depart_hub_time = truck.current_time

    while truck.packages:
        next_stop, distance = minimum_distance(truck.current_address, truck.packages)
        del_time = distance / 18

        update_truck_info(truck, next_stop, distance, del_time)

        for package in list(truck.packages):
            if next_stop == package.address:
                truck.packages.remove(package)
                update_package_info(package, depart_hub_time, truck.current_time)

            update_special_case(package, truck.current_time)

    distance_to_hub = distance_between(truck.current_address, starting_location)
    del_time_to_hub = distance_to_hub / 18
    update_truck_info(truck, starting_location, distance_to_hub, del_time_to_hub)

# Finds the closest package address to a given address and returns the address and its distance
# Time complexity: O(n)
def minimum_distance(from_address, truck_packages):
    min_distance = float('inf')  # Initialize to a large number
    min_distance_address = None

    for package in truck_packages:
        distance = distance_between(from_address, package.address)

        if 0 < distance < min_distance:
            min_distance = distance
            min_distance_address = package.address

    return min_distance_address, min_distance if min_distance != float('inf') else None

# calculate the distance between two addresses
# Time complexity: O(1)
def distance_between(address1, address2):
    distance = distances[addresses.index(address1)][addresses.index(address2)]
    return float(distance)

#Load packages onto a truck based on a list of package IDs.
# Time complexity: O(n)
def load_truck(list_of_ids):

    packages_to_deliver = [package_hash_table.search(package_id) for package_id in list_of_ids if
                           package_hash_table.search(package_id)]
    return packages_to_deliver


HUB_ADDRESS = "4001 South 700 East"

#Initialize a truck and dispatch it for delivery.
# Time complexity: O(n^2)
def initialize_and_dispatch_truck(miles, package_ids, address, time):
    truck = Truck(mileage=miles, packages=load_truck(package_ids), current_address=address, current_time=time)
    deliver_packages(truck)
    return truck


# Initialize and dispatch trucks with their package IDs and departure times
truck1 = initialize_and_dispatch_truck(0, [13, 14, 15, 16, 19, 20, 39, 34, 21, 7, 29, 4, 40, 1, 30, 8], HUB_ADDRESS,
                                       datetime.timedelta(hours=8))
truck2 = initialize_and_dispatch_truck(0, [3, 18, 36, 38, 6, 25, 28, 32, 37, 26, 31, 5, 27, 35, 10, 11], HUB_ADDRESS,
                                       datetime.timedelta(hours=9, minutes=5))
truck3 = initialize_and_dispatch_truck(0, [2, 9, 33, 12, 17, 22, 23, 24], HUB_ADDRESS, truck1.current_time)


# Calculate total mileage across all trucks
# Time complexity: O(n)
def total_mileage(trucks):
   return sum(truck.mileage for truck in trucks)

# Compute the total mileage.
# Time complexity: O(n)
total = total_mileage([truck1, truck2, truck3])
