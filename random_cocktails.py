url="https://www.thecocktaildb.com/api/json/v1/1/random.php"

cocktails=requests.get(url).json()
cocktails

cocktail_image=cocktails["drinks"][0]['strDrinkThumb']
cocktail_image

cocktail_instructions=cocktails["drinks"][0]['strInstructions']
cocktail_instructions

cocktail_name= cocktails["drinks"][0]['strDrink']
cocktail_name

cocktail_ingredients=cocktails["drinks"][0]['strIngredient1']
cocktail_ingredients

cocktail_measurements= cocktails["drinks"][0]["strMeasure1"]
cocktail_measurements

