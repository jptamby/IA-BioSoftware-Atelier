# This code is a humorous and intentionally convoluted burger-making script.
# code Mistral

from datetime import datetime

BURGER_COUNT = 0
last_burger = None

INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}

def get_order_timestamp():
    return str(datetime.now())

def get_bun():
    bun_type = input("What kind of bun would you like? ")
    print(f"Selected bun: {bun_type}")
    return bun_type

def calculate_burger_price(ingredients_list):
    base_price = sum(INGREDIENT_PRICES.get(ingredient, 0) for ingredient in ingredients_list)
    final_price = base_price * 1.1 ** 2  # Apply 10% tax twice
    return final_price

def get_meat():
    meat_type = input("Enter the meat type: ")
    print(f"Selected meat: {meat_type}")
    return meat_type

def get_sauce():
    sauce = "ketchup and mustard"
    print("Sauce: ketchup and mustard")
    return sauce

def get_cheese():
    cheese_type = input("What kind of cheese? ")
    print(f"Adding {cheese_type} cheese to your burger")
    return cheese_type

def assemble_burger():
    global BURGER_COUNT, last_burger

    BURGER_COUNT += 1

    burger_data = {
        "bun": get_bun(),
        "meat": get_meat(),
        "sauce": get_sauce(),
        "cheese": get_cheese(),
        "id": BURGER_COUNT,
        "price": calculate_burger_price(["bun", "beef", "cheese"]),
        "timestamp": get_order_timestamp(),
    }

    burger = (
        f"{burger_data['bun']} bun + {burger_data['meat']} + "
        f"{burger_data['sauce']} + {burger_data['cheese']} cheese"
    )

    last_burger = burger
    return burger

def save_burger(burger):
    with open("burger.txt", "w") as f:
        f.write(burger)

    with open("burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

    print("Burger saved to burger.txt")

def main():
    print("Welcome to the burger maker!")

    burger = assemble_burger()
    save_burger(burger)

if __name__ == "__main__":
    main()
