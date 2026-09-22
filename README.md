# Project Title

## Topic: Recipe Manager


### Video demonstration
https://drive.google.com/file/d/1aF2jxmiFVJDckDtJBG07QqBiXtgFRYII/view?usp=sharing


### App Link
https://recipe-manager-hd7wuh6i8vepa8t523gmgx.streamlit.app/


### Project Overview

Recipe Manager is a Python web application built with Streamlit and Pandas that allows users to store, search, view, and manage recipes using a CSV file.

The application loads saved recipes when it starts and provides an easy interface for managing a personal recipe collection.

Main Features
Add new recipes with:
Recipe name
Ingredients
Preparation time
Cooking instructions
Difficulty level
Category
Number of servings
Search recipes by ingredient.
View all saved recipes.
Get a random recipe suggestion.
Categorize recipes as Breakfast, Lunch, Dinner, or Dessert.
Scale ingredient quantities based on the desired number of servings.
Rate recipes and sort them by rating.
Track the number of reviews.
Generate a downloadable shopping_list.csv.
Track whether a recipe has been made before.
Use API integration to retrieve external recipes.
Use a Smart Chef AI assistant for recipe suggestions and ingredient substitutions.
Technologies Used
Python
Streamlit
Pandas
CSV
Requests / APIs
LLM API integration
Data Storage

Recipes are stored in a CSV file and loaded using Pandas:

recipes = pd.read_csv("cooking_recipes_test_data.csv")

This allows recipe information and updates to remain available between sessions.

This project demonstrates Python programming, CSV file handling, Pandas data manipulation, Streamlit development, session state, API integration, user input handling, data filtering, sorting, and basic AI integration.
