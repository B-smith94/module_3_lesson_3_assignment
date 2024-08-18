#Task 1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
unique_destinations = our_routes.difference(competitor_routes)
unshared_destinations = our_routes.symmetric_difference(competitor_routes)

print(f"Destinations both airlines fly to: {common_destinations}")
print(f"Destinations unique to our airline: {unique_destinations}")
print(f"Destinations shared by neither airline: {unshared_destinations}")
