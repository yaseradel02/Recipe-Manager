import requests
import json
import pandas as pd

def get_recipes(search, key):

    response = requests.get(
        "https://tasty.p.rapidapi.com/recipes/list",
        headers={
            "x-rapidapi-key": key,
            "x-rapidapi-host": "tasty.p.rapidapi.com"
        },
        params={
            "from": "0",
            "size": "3",
            "q": search
        }
    )

    response.raise_for_status()

    results = response.json()["results"]

    recipes = []

    for r in results:

        ingredients = []

        for section in r.get("sections", []):
            for item in section.get("components", []):
                ingredients.append(item.get("raw_text", ""))


        instructions = [
            f"{i + 1}. {step['display_text']}"
            for i, step in enumerate(r.get("instructions", []))
        ]

        total_time = r.get("total_time_minutes")

        if not total_time:
            total_time = (
                (r.get("prep_time_minutes") or 0)
                + (r.get("cook_time_minutes") or 0)
            )

        category = "Other"

        tags = [
            tag["name"].lower()
            for tag in r.get("tags", [])
        ]

        for option in ["breakfast", "lunch", "dinner", "dessert"]:
            if option in tags:
                category = option.title()
                break

        rating_data = r.get("user_ratings", {})

        score = rating_data.get("score")

        rating = round(score * 5, 1) if score else 0

        reviews = (
            rating_data.get("count_positive", 0)
            + rating_data.get("count_negative", 0)
        )

        recipes.append({
            "Recipe name": r.get("name"),
            "Ingredients": ", ".join(ingredients),
            "Number of servings": r.get("num_servings", 1),
            "Preparation time in minutes": total_time,
            "Cooking instructions": " ".join(instructions),
            "Difficulty": "Unknown",
            "Category": category,
            "Rating": rating,
            "Number of reviews": reviews,
            "Made Before": False
        })

    return pd.DataFrame(recipes)



def add_recipe(recipe, file_name):

    recipes = pd.read_csv(file_name)

    recipe_name = recipe["Recipe name"].strip().lower()

    existing_names = (
        recipes["Recipe name"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    if recipe_name in existing_names.values:
        return False

    recipes.loc[len(recipes)] = recipe

    recipes.to_csv(file_name, index=False)

    return True

