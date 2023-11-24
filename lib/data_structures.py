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
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
        return [f for f in spicy_foods if f["heat_level"] > 5]
pass
spiciest_result = get_spiciest_foods(spicy_foods)
print(spiciest_result)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        if food["heat_level"] > 5: 
             print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
print_spiciest_foods(spicy_foods)
    
def get_average_heat_level(spicy_foods):
    temp = (food["heat_level"] for food in spicy_foods)
    average = (int(sum(temp)/len(spicy_foods)))
    return average
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods + [spicy_food]
    return new_spicy_foods
food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
new_spicy_foods = create_spicy_food(spicy_foods, food)
print(new_spicy_foods)
