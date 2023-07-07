# Pricing structure in format: (room_type, tier): price
pricing_structure = {
    ("inside", 1): 2,
    ("inside", 2): 5,
    ("inside", 3): 7,
    ("outside", 1): 2,
    ("outside", 2): 5,
    ("outside", 3): 7,
    ("balcony", 1): 3,
    ("balcony", 2): 6,
    ("balcony", 3): 8,
    ("suite", 1): 4,
    ("suite", 2): 7,
    ("suite", 3): 9,
    ("yacht", 1): 5,
    ("yacht", 2): 8,
    ("yacht", 3): 10
}

# Tiers in format: tier: max_rooms
tiers = {
    1: 585,
    2: 1025,
    3: 1000000
}

def calculate_commission(rooms_sold):
    total_commission = 0
    total_rooms = 0
    current_tier = 1
    tier_commission = {1:0, 2:0, 3:0} # This will store commission per tier

    # Loop through the priority order of rooms
    for room_type in ["inside", "outside", "balcony", "suite", "yacht"]:
        if room_type in rooms_sold:
            for room in range(rooms_sold[room_type]):
                total_rooms += 1
                
                # check if total_rooms exceeds the current tier's max_rooms
                if total_rooms > tiers[current_tier]:
                    current_tier += 1

                # add to the total_commission and commission per tier
                commission = pricing_structure[(room_type, current_tier)]
                total_commission += commission
                tier_commission[current_tier] += commission
                
    return total_commission, tier_commission

# Usage
rooms_sold = {}
for room_type in ["inside", "outside", "balcony", "suite", "yacht"]:
    rooms_sold[room_type] = int(input(f"Enter the number of {room_type} rooms sold: "))

total_commission, tier_commission = calculate_commission(rooms_sold)

print("Total commission: $", total_commission)
for tier, commission in tier_commission.items():
    print(f"Commission for tier {tier}: $", commission)
