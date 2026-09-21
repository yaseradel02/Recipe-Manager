import streamlit as st
import datetime
import pandas as pd


recipes = pd.read_csv('cooking_recipes_test_data.csv')
@st.cache_data
def fetch_and_clean_data(recipes):
    # Fetch data from URL here, and then clean it up.
    return data


st.page_link("Yaser_Project_1.py", label="Home", icon="🏠")
st.title("Recipe Manager")

recipe_number = st.session_state.get('selected_recipe', None)
chosen_recipe=recipes.iloc[recipe_number]

st.subheader(chosen_recipe['Recipe name'])
st.badge(chosen_recipe['Category'], color="orange")
if chosen_recipe['Difficulty'] == "Easy":
    random_color = "green"
elif chosen_recipe['Difficulty'] == "Medium":
    random_color = "yellow"
else:
    random_color = "red"
st.badge("Difficulty: " + chosen_recipe['Difficulty'], color=random_color)
st.badge("Preparation Time: " + str(chosen_recipe['Preparation time in minutes']) + " minutes", color="blue")
st.badge("Number of Servings: " + str(chosen_recipe['Number of servings']), color="yellow")
st.text_area("Ingrediants:", chosen_recipe['Ingredients'], height=100)
st.text_area("Instructions:", chosen_recipe['Cooking instructions'] , height=100)


options = ["Scalling Ingrediants"]
help_user = st.pills(
    " ", options, selection_mode="single"
    )

if help_user == "Scalling Ingrediants":
    st.text("Number of Servings: " + str(chosen_recipe['Number of servings']))
    desired_servings = (
        st.slider("X Servings :", 1, 10, 1)
        * chosen_recipe['Number of servings']
    )
    st.text("Scaled Servings: " + str(desired_servings))

    if st.button("Scale Ingrediants"):
        scaled_ingredients = []
        for ingredient in chosen_recipe['Ingredients'].split(','):
            parts = ingredient.strip().split(' ', 1)
            if len(parts) == 2:
                quantity, name = parts
                try:
                    scaled_quantity = (
                        float(quantity)
                        * desired_servings
                        / chosen_recipe['Number of servings']
                    )
                    scaled_ingredients.append(
                        f"{scaled_quantity} {name}"
                    )
                except ValueError:

                    scaled_ingredients.append(ingredient.strip())

            else:

                scaled_ingredients.append(ingredient.strip())

        st.session_state["scaled_ingredients"] = scaled_ingredients

    if "scaled_ingredients" in st.session_state:
        st.dataframe(
            pd.DataFrame({
                "Scaled Ingrediants":
                st.session_state["scaled_ingredients"]
            }),
            hide_index=True
        )
        shopping_list = pd.DataFrame({
            "Shopping List":
            st.session_state["scaled_ingredients"]
        })
        csv = shopping_list.to_csv(index=False)
        st.download_button(
            "Save Shopping List",
            csv,
            "shopping_list.csv",
            "text/csv"
        )



if chosen_recipe['Made Before']:
    st.write("You have made this recipe before. Please rate it below:")
else:
    st.write("If you have made this recipe before, please rate it below:")

sentiment_mapping = [1, 2, 3, 4, 5]
selected = st.feedback("stars")
recipe_rate = sentiment_mapping[selected] if selected is not None else None
if recipe_rate is not None:
    recipes.loc[recipe_number,'Made Before'] = True
    if recipes.loc[recipe_number, 'Number of reviews'] == 0:
        recipes.loc[recipe_number, 'Rating'] = recipe_rate
        recipes.loc[recipe_number, 'Number of reviews'] += 1
    else:
        total_reviews=recipes.loc[recipe_number, 'Number of reviews']
        total_rate = total_reviews*recipes.loc[recipe_number, 'Rating'] + recipe_rate
        recipes.loc[recipe_number, 'Number of reviews'] += 1
        recipes.loc[recipe_number, 'Rating'] = (total_rate / recipes.loc[recipe_number, 'Number of reviews'])
    recipes.to_csv('cooking_recipes_test_data.csv', index=False)
