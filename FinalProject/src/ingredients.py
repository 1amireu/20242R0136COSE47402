import os
import json
import pandas as pd

# Step 1: Load Food-101 Class Names
food101_path = "C:\\Users\\1amir\\.cache\\kagglehub\\datasets\\dansbecker\\food-101\\versions\\1\\food-101\\food-101\\images"
food101_class_names = [folder for folder in os.listdir(food101_path) if os.path.isdir(os.path.join(food101_path, folder))]
add_class_names = ['cupcakes', 'pork_chops']
food101_class_names.extend(add_class_names)

# Step 2: Load Recipe-Dataset-Over-2M Class Names
recipe_dataset_path = "C:\\Users\\1amir\\.cache\\kagglehub\\datasets\\wilmerarltstrmberg\\recipe-dataset-over-2m\\versions\\2"
recipes_df = pd.read_csv(os.path.join(recipe_dataset_path, "recipes_data.csv"))

class_names_with_spaces = [name.replace('_', ' ') for name in food101_class_names]
recipes_df['normalized_title'] = recipes_df['title'].str.lower()
filtered_recipes = recipes_df[recipes_df['normalized_title'].isin([name.lower() for name in class_names_with_spaces])]

# Select only the 'title' and 'ingredients' columns
recipe_ingredients = filtered_recipes[['title', 'ingredients', 'normalized_title']].drop_duplicates(subset='normalized_title').drop(columns=['normalized_title'])
recipe_ingredients['title'] = recipe_ingredients['title'].str.lower().str.replace(' ', '_')
recipe_ingredients['title'] = recipe_ingredients['title'].replace({'cupcakes': 'cup_cakes', 'pork_chops': 'pork_chop'})

recipe_dict = {}
# Iterate through the rows of the DataFrame and populate the dictionary
for index, row in recipe_ingredients.iterrows():
    # Store the ingredients under the class name
    recipe_dict[row['title']] = row['ingredients']

# Write the dictionary to a JSON file
with open("..\\dataset\\recipe_ingredients.json", "w") as json_file:
    json.dump(recipe_dict, json_file, indent=4)

print("Results have been written to 'recipe_ingredients.json'.")

# Find missing class names that are not in the recipe titles
missing_class_names = [class_name for class_name in food101_class_names if class_name not in recipe_ingredients['title'].tolist()]

# Print matching titles
print(missing_class_names)


