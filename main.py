""" LU2.A08 """
import json


def adjust_recipe(original_recipe, num_people):
    adjusted_ingredients = {}
    original_servings = original_recipe['servings']
    factor = num_people / original_servings

    for ingredient, amount in original_recipe['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjusted_recipe = {
        'title': original_recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people,
    }
    return adjusted_recipe


def load_recipe(original_recipe):
    return json.loads(original_recipe)


if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    orig_recipe = json.loads(recipe_json)
    adj_recipe = adjust_recipe(orig_recipe, 2)