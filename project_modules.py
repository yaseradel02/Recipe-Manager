import streamlit as st
import datetime
import pandas as pd



def new_recipe(recipes):
    import streamlit as st
    import datetime
    import pandas as pd
    with st.form("name"):
        r_name = st.text_input("Recipe Name:")
        options = ["Breakfast", "Lunch", "Dinner", "Dessert"]
        r_category = st.pills(
            "Category", options, selection_mode="single"
            )
        r_servings = st.slider("Number of Servings:", 1, 15, 1)
        r_ingrediants = st.text_area("Recipe Ingrediants:")
        r_time = st.time_input("Time to make:",datetime.time(0,00))
        r_time_minutes=r_time.hour*60+r_time.minute
        r_instructions = st.text_area("Recipe Instructions:")
        difficulty_options = ["Easy", "Medium", "Hard"]
        r_difficulty = st.pills("Difficulty:", difficulty_options, selection_mode="single")
        submitted = st.form_submit_button("Submit")
        if submitted and r_name and r_servings and r_category and r_ingrediants and r_instructions and r_difficulty and r_time_minutes:
            new_recipe = pd.DataFrame([[r_name, r_servings, r_category, r_ingrediants, r_time_minutes, r_instructions, r_difficulty,0,0,True]], columns=['Recipe name', 'Number of servings', 'Category', 'Ingredients', 'Preparation time in minutes', 'Cooking instructions', 'Difficulty', 'Rating', 'Number of reviews', 'Made Before'])
            st.dataframe(new_recipe)
            new_recipes=pd.concat([recipes, new_recipe], ignore_index=True, sort=False)
            st.dataframe(new_recipes.to_csv('cooking_recipes_test_data.csv', index=False))
            st.write("Thank you for adding a new recipe!")
            st.success("Submitted")
            return 



def search_by_ingerdiant(recipes):
    import streamlit as st
    import datetime
    import pandas as pd    
    with st.form("search"):
        s_ingrediants = st.text_input("Enter an Ingrediant:")
        submitted = st.form_submit_button("Search")
        if submitted and s_ingrediants:
            filter_ingredients = [recipes['Ingredients'].str.contains(s_ingrediants, case=False)]
            filter_names = [recipes['Recipe name'].str.contains(s_ingrediants, case=False)]
            st.dataframe(recipes[filter_ingredients [0] | filter_names[0]],hide_index=True)

    return



def view_all_recipes(short_recipes):
    import streamlit as st
    import datetime
    import pandas as pd
    options = ["Breakfast", "Lunch", "Dinner", "Dessert"]
    view_meal = st.pills(
    " ", options, selection_mode="single"
    )

    if view_meal=="Breakfast":
            event = st.dataframe(short_recipes[short_recipes['Category'] == 'Breakfast'],hide_index=True,on_select="rerun",selection_mode="single-row")
            if event.selection.rows:
                row_number=event.selection.rows[0]
                selected_index=row_number
                st.session_state['selected_recipe']=selected_index
                st.switch_page("pages/recipe_details.py")
    elif view_meal=="Lunch":
            event = st.dataframe(short_recipes[short_recipes['Category'] == 'Lunch'],hide_index=True,on_select="rerun",selection_mode="single-row")
            if event.selection.rows:
                row_number=event.selection.rows[0]
                selected_index=row_number
                st.session_state['selected_recipe']=selected_index
                st.switch_page("pages/recipe_details.py")
    elif view_meal=="Dinner":
            event = st.dataframe(short_recipes[short_recipes['Category'] == 'Dinner'],hide_index=True,on_select="rerun",selection_mode="single-row")
            if event.selection.rows:
                row_number=event.selection.rows[0]
                selected_index=row_number
                st.session_state['selected_recipe']=selected_index
                st.switch_page("pages/recipe_details.py")
    elif view_meal=="Dessert":
            event = st.dataframe(short_recipes[short_recipes['Category'] == 'Dessert'],hide_index=True,on_select="rerun",selection_mode="single-row")
            if event.selection.rows:
                row_number=event.selection.rows[0]
                selected_index=row_number
                st.session_state['selected_recipe']=selected_index
                st.switch_page("pages/recipe_details.py")
    else:
         event = st.dataframe(short_recipes,hide_index=True,on_select="rerun",selection_mode="single-row")
         if event.selection.rows:
              row_number=event.selection.rows[0]
              selected_index=row_number
              st.session_state['selected_recipe']=selected_index
              st.switch_page("pages/recipe_details.py")


def suggest_random_recipe(recipes):
    import streamlit as st
    import datetime
    import pandas as pd
    random_recipe = recipes[recipes['Made Before'] == False].sample(1)
    st.subheader(random_recipe['Recipe name'].values[0])
    st.badge(random_recipe['Category'].values[0], color="orange")
    if random_recipe['Difficulty'].values[0] == "Easy":
        random_color = "green"
    elif random_recipe['Difficulty'].values[0] == "Medium":
        random_color = "yellow"
    else:
        random_color = "red"
    st.badge("Difficulty: " + random_recipe['Difficulty'].values[0], color=random_color)
    st.badge("Preparation Time: " + str(random_recipe['Preparation time in minutes'].values[0]) + " minutes", color="blue")
    st.text_area("Ingrediants:", random_recipe['Ingredients'].values[0], height=100)
    st.text_area("Instructions:", random_recipe['Cooking instructions'].values[0], height=100)
    st.button("Full Recipe Details", on_click=lambda: st.session_state.update({'selected_recipe': random_recipe.index[0]}) or st.switch_page("pages/recipe_details.py"))

    