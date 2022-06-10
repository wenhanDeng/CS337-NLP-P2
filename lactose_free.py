from web_scraping import *

url = 'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/'

def lactose_free(ingredients):
	lactose_free_ingredients = []
	
	for i in ingredients[1]:
		category = ingredients[1][i]

		if category == 'Dairy, Eggs and Milk' and 'eggs' not in i:
			if 'milk' in i and 'almond' not in i and 'soy' not in i and 'coconut' not in i and 'oat' not in i:
				# print(i, ' became ', 'dairy-free milk of choice')
				lactose_free_ingredients.append('dairy-free milk of choice (oat, soy, coconut, almond')

			elif 'cream' in i and 'almond' not in i and 'soy' not in i and 'coconut' not in i and 'oat' not in i and 'ice' not in i:
				# print(i, ' became ', 'dairy-free cream of choice')
				lactose_free_ingredients.append('dairy-free cream of choice')

			elif 'yogurt' in i and 'almond' not in i and 'soy' not in i and 'coconut' not in i and 'oat' not in i:
				# print(i, ' became ', 'dairy-free yogurt of choice')
				lactose_free_ingredients.append('dairy-free yogurt of choice')

			elif 'cheese' in i:
				# print(i, ' became ', 'dairy-free ' + i)
				lactose_free_ingredients.append('dairy-free ' + i)

			elif 'butter' in i and 'almond' not in i and 'soy' not in i and 'coconut' not in i and 'nut' not in i:
			# print('nut butter or coconut butter')
				lactose_free_ingredients.append('nut butter or coconut butter')

		elif 'butter' in i and 'almond' not in i and 'soy' not in i and 'coconut' not in i and 'nut' not in i:
			# print('nut butter or coconut butter')
			lactose_free_ingredients.append('nut butter or coconut butter')

		else:
			lactose_free_ingredients.append(i)

	# print(ingredients[1])
	# print(lactose_free_ingredients)
	return lactose_free_ingredients
		

# measurements = get_quant(url)
# ingredients = get_ingredients(url)
# lactose_free(ingredients)