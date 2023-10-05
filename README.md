# WGU-DeliverySystem
In the code provided, the self-adjusting algorithm employed is a Greedy Algorithm. The algorithm dynamically adjusts to the packages loaded on a truck and decides the most efficient sequence in which to deliver them, based on the closest neighbor to the truck's current location.
The self-adjusting part comes into play in the deliver_packages function. Given the current location of the truck and the packages it has, this function calculates the closest next stop for delivery. It updates the truck's information and proceeds to deliver the package at the chosen stop, thereby dynamically adjusting the delivery route based on the remaining packages and their destinations.
