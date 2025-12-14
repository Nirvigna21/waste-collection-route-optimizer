import pandas as pd
import math

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

data = pd.read_csv("data.csv")

bins_to_collect = data[data["fill_level"] >= 70]

truck_location = (17.385, 78.486)

route = []
current = truck_location
total_distance = 0

bins = bins_to_collect.copy()

while not bins.empty:
    nearest_index = None
    nearest_dist = float("inf")

    for i, row in bins.iterrows():
        d = distance(current, (row["latitude"], row["longitude"]))
        if d < nearest_dist:
            nearest_dist = d
            nearest_index = i

    selected = bins.loc[nearest_index]
    route.append(selected["bin_id"])
    total_distance += nearest_dist
    current = (selected["latitude"], selected["longitude"])
    bins = bins.drop(nearest_index)

print("Optimized Collection Order:", route)
print("Total Distance Covered:", round(total_distance, 3))
