import streamlit as st
import datetime
import pandas as pd
import project_modules as pm
from recipe_api import get_recipes, add_recipe
from assistant_api import ask_chef


recipes = pd.read_csv('cooking_recipes_test_data.csv')
@st.cache_data
def fetch_and_clean_data(recipes):
    # Fetch data from URL here, and then clean it up.
    return data

short_recipes = recipes[['Recipe name','Preparation time in minutes','Difficulty','Category','Rating']]
@st.cache_data
def fetch_and_clean_data(short_recipes):
    # Fetch data from URL here, and then clean it up.
    return data

short_recipes2 = recipes[['Recipe name','Ingredients']]
@st.cache_data
def fetch_and_clean_data(short_recipes2):
    # Fetch data from URL here, and then clean it up.
    return data


st.title("Recipe Manager")


options = ["Add a Recipe", "Search by Ingrediants", "View All Ricepes", "Suggest a Random Recipe", "Smart Chef"]
selection = st.segmented_control(
    " ", options, selection_mode="single"
)


if selection=="Add a Recipe":
    st.header(selection, divider="red")
    options = ["Add manually", "Import public recipes"]
    method = st.pills(
    "Choose method", options, selection_mode="single"
    )
    if method == "Add manually":
        pm.new_recipe(recipes)
    elif method == "Import public recipes":
        key = st.secrets["TASTY_KEY"]
        st.subheader("Import Public Recipes")

        search = st.text_input("Search for a recipe")
        if st.button("Search Recipes"):
            api_recipes = get_recipes(search, key)
            st.session_state["api_recipes"] = api_recipes

        if "api_recipes" in st.session_state:
            api_recipes = st.session_state["api_recipes"]

            if not api_recipes.empty:
                selected_recipe = st.selectbox(
                    "Choose a recipe",
                    api_recipes["Recipe name"]
                )
                chosen_recipe = api_recipes[
                    api_recipes["Recipe name"] == selected_recipe
                ].iloc[0]

                st.subheader(chosen_recipe["Recipe name"])
                st.write("**Ingredients:**")
                st.write(chosen_recipe["Ingredients"])
                st.write(
                    "**Number of servings:**",
                    chosen_recipe["Number of servings"]
                )

                st.write(
                    "**Preparation time:**",
                    chosen_recipe["Preparation time in minutes"],
                    "minutes"
                )
                st.write("**Cooking instructions:**")
                st.write(chosen_recipe["Cooking instructions"])
                st.write("**Difficulty:**", chosen_recipe["Difficulty"])
                st.write("**Category:**", chosen_recipe["Category"])
                st.write("**Rating:**", chosen_recipe["Rating"])
                st.write(
                    "**Number of reviews:**",
                    chosen_recipe["Number of reviews"]
                )

                if st.button("Add Recipe"):
                    added = add_recipe(
                        chosen_recipe,
                        "cooking_recipes_test_data.csv"
                    )
                    if added:
                        st.success("Recipe added successfully!")
                    else:
                        st.warning("This recipe is already in your collection.")
        

        
elif selection=="Search by Ingrediants":
    st.header(selection, divider="green")
    pm.search_by_ingerdiant(recipes)

elif selection=="View All Ricepes":
    st.header(selection, divider="yellow")
    pm.view_all_recipes(short_recipes)

elif selection=="Suggest a Random Recipe":
    st.header(selection, divider="blue")
    pm.suggest_random_recipe(recipes)

elif selection=="Smart Chef":
    st.header(selection, divider="grey")
    key = st.secrets["OPENROUTER_KEY"]

    question = st.text_input(
        "Ask the Smart Chef",
        placeholder="How can I make this recipe vegan?"
    )

    if st.button("Ask") and question:

        with st.spinner("Chef is thinking..."):
            answer = ask_chef(question, key)

        st.write(answer)
    

else:
    st.header("Previously Created:", divider="orange")
    event = st.dataframe(short_recipes[recipes['Made Before'] == True],hide_index=True,on_select="rerun",selection_mode="single-row")
    if event.selection.rows:
        row_number=event.selection.rows[0]
        selected_index=row_number
        st.session_state['selected_recipe']=selected_index
        st.switch_page("pages/recipe_details.py")
