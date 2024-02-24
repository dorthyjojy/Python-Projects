# in this project, you'll create a program to search for receipes
# based on an ingredient. The standard project uses Edamam Recipe API
# creating a function to store ingredient
import requests

def get_recipe(ing, id, key):
    # the get request will search the API based on the given ingredients
    # the arguement is the ingredient whose recipe has to be searched
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ing, id, key)
    results = requests.get(url)
    data = results.json()

    if 'hits' in data:
        return data['hits']
    else:
        return None

def main():
    ingredient = input('Enter an ingredient: ')
    app_id = input("Please enter a valid application ID: ")
    app_key = input("Please enter a valid key for the above: ")
    print()
    recipe1 = get_recipe(ingredient, app_id, app_key)
    print('----------------------------------------------')
    if recipe1 == None:
        print('No recipe found')
    else:
        for result in recipe1:
            recipe = result['recipe']
            print('Recipe: ', recipe['label'])
            print('Link: ', recipe['uri'])
            print()


main()