"""Restaurant rating lister."""


filename = 'scores.txt'
data = open(filename)

restaurant_ratings = {}

for line in data:
    line = line.rstrip().split(":")
    restaurant_name, rating = line
    restaurant_ratings[restaurant_name] = rating


def print_restaurants_alphabetically(restaurant_ratings_dict):
    """
    take a restaurant rating dictionary and print ratings in alphabetical order by restaurant

    parameter:
        - restaurant_ratings_dict (dictionary)
    """
    for restaurant, rating in sorted(restaurant_ratings_dict.items()):
        print(f"{restaurant} is rated at {rating}.")


def ask_user_correct_input_Y_N():
    """
    make sure user inputs Y or N
    """
    while True:
        add_restaurant = input("Do you want to add a restaurant to the list? Y/N ").upper()

        if add_restaurant == "Y" or add_restaurant == "N":
            return add_restaurant
        
        print("Invalid input. Please try again.")


def validate_new_score():
    """
    make sure user inputs score from 1 to 5
    """
    while True:
        rating = input("What rating would you give it? ")

        if rating.isnumeric():
            rating = int(rating)
            if rating in range(1, 6):  # 0 < rating <= 5:
                return rating
        
        print("Invalid input. Please try again.")


def add_restaurant_rating(restaurant_ratings_dict):
    """
    ask the user for restaurant and rating and prints ratings in alphabetical order by restaurant

    parameter:
        - restaurant_ratings_dict (dictionary)
    """
    
    add_restaurant = ask_user_correct_input_Y_N()
    
    if add_restaurant == "Y":
        restaurant = input("What restaurant would you like to add? ").capitalize()
        rating = validate_new_score()
        restaurant_ratings_dict[restaurant] = rating
    elif add_restaurant == "N":
        print("Good bye")

    print_restaurants_alphabetically(restaurant_ratings_dict)


add_restaurant_rating(restaurant_ratings)