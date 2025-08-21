points_scored = [24, 33, 20, 27]

running_total = 0
for point_amount in points_scored:
    running_total += point_amount

print(f"The player has scored {running_total} points")