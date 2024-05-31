spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [spicy_food["name"] for spicy_food in spicy_foods]
    return names
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_food for spicy_food in  spicy_foods if spicy_food["heat_level"] > 5] 
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        return (f"{food["name"]} ({food["cuisine"]}) | Heat level: {food["heat_level"] * "🌶️" }")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    pass

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    total = sum(heat_levels)
    average = total / (len (heat_levels))
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

