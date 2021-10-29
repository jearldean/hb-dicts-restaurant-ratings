"""Restaurant rating lister."""

import sys
import random


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


def ask_user_choice():
    """
    make sure user inputs 1, 2, or 3
    """
    while True:
        print("""Would you like to
    [1] add a restaurant rating
    [2] update a random restaurant rating
    [3] print all restaurant ratings
    [4] quit""")
        user_choice = input("> ")

        if user_choice in ["1", "2", "3", "4"]:
            return user_choice
        
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
    while True:
        user_choice = ask_user_choice()
        
        if user_choice == "1":
            restaurant = input("What restaurant would you like to add? ").title()
            rating = validate_new_score()
            restaurant_ratings_dict[restaurant] = rating
        elif user_choice == "2":
            restaurant = random.choice(list(restaurant_ratings_dict.keys()))
            print(f"Have you been to {restaurant}?")
            rating = validate_new_score()
            restaurant_ratings_dict[restaurant] = rating
        elif user_choice == "3":
            print_restaurants_alphabetically(restaurant_ratings_dict)
        elif user_choice == "4":
            sys.exit("Good bye.")

        


add_restaurant_rating(restaurant_ratings)