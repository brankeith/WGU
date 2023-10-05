import csv
from Package import Package
# HashTable class using chaining. Citation: from C950-Webinar-1-Let's Go Hashing
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

# Load a CSV file and return its data.
def load_csv(file_name, as_nested_list=True):
    csv_data = []
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        if as_nested_list:
            csv_data = [row for row in reader]
        else:
            csv_data = [item for row in reader for item in row]
    return csv_data


# Assign the hash table to a variable
package_hash_table = HashTable()
# load the csvs for distances and addresses
distances = load_csv('CSV/Distances.csv')
addresses = load_csv('CSV/Address.csv', False)

# Load package data from CSV into a hash table.
def load_package_data():
    package_data = load_csv('CSV/Packages.csv')
    for data in package_data:
        package_id = int(data[0])
        address = data[1]
        city = data[2]
        state = data[3]
        zipcode = int(data[4])
        deadline = data[5]
        mass = data[6]

        package_list = Package(package_id, address, city, state, zipcode, deadline, mass, status="At Hub",
                               time_delivered=None,
                               time_left_hub=None)

        package_hash_table.insert(package_id, package_list)


load_package_data()