from web_scraping import *

url = 'https://www.allrecipes.com/recipe/284313/spicy-low-carb-eggplant-with-beef-and-tomatoes/'

def make_healthy(ingredients, measurements):
	healthy_ingredients = []
	veggies_halved = False
	veggies = [key for key,value in ingredients[1].items() if (value == 'Produce' and 'minced' not in key)]
	measure_dict = {}
	for i in range(len(ingredients[0])):
		measure_dict[ingredients[0][i]] = measurements[i]

	for i in ingredients[1]:
		category = ingredients[1][i]
		if category == 'Dairy, Eggs and Milk' and 'eggs' not in i and 'butter' not in i:
			healthy_ingredients.append('low-fat ' + i)
			print(i, 'became ', 'low-fat ' + i)

		elif 'butter' in i:
			healthy_ingredients.append("avocado oil")
			print(i, 'became ', "avocado oil")

		elif category == 'Meats, Fish and Seafood' and 'beef' in i:
			healthy_ingredients.append(i)
			print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(.5))/2
			if veggies_halved == False:
				for v in veggies:
					veggies_halved = True
					print(v, 'measurement went from', measure_dict[v], " to ", round(2*(float(measure_dict[v])+float(measure_dict[v])*(.5)))/2)
					measure_dict[v] = round(2*(float(measure_dict[v])+float(measure_dict[v])*(.5))/2)

		elif category == 'Meats, Fish and Seafood' and 'bacon' in i:
			healthy_ingredients.append(i.replace("bacon", "turkey bacon"))
			print(i, 'became ', i.replace("bacon", "turkey bacon"))

		elif category == 'Soup' and 'beef' in i:
			healthy_ingredients.append(i.replace("beef", "chicken"))
			print(i, 'became ', i.replace("beef", "chicken"))

		elif category == 'Pasta, Rice and Beans' and 'pasta' in i:
			healthy_ingredients.append("whole-wheat pasta")
			print(i, 'became ', "whole-wheat pasta")

		elif category == 'Pasta, Rice and Beans' and 'rice' in i:
			healthy_ingredients.append('brown rice')
			print(i, 'became ', 'brown rice')

		elif category == 'Pasta, Rice and Beans' and 'noodle' in i:
			healthy_ingredients.append('squash noodles')
			print(i, 'became ', 'squash noodles')

		elif 'olive oil' in i:
			healthy_ingredients.append(i.replace('olive oil', 'avocado oil'))
			print(i, 'became ', i.replace('olive oil', 'avocado oil'))

		elif category == 'Beverages' and 'wine' in i:
			healthy_ingredients.append('white wine vinegar')
			print(i, 'became ', 'white wine vinegar')

		elif category == 'Herbs and Spices' and 'salt' in i:
			healthy_ingredients.append(i)
			print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(.5))/2

		else:
			healthy_ingredients.append(i)
	return healthy_ingredients

def make_unhealthy(ingredients, measurements):
	unhealthy_ingredients = []
	veggies_halved = False
	veggies = [key for key,value in ingredients[1].items() if (value == 'Produce' and 'minced' not in key)]
	measure_dict = {}
	for i in range(len(ingredients[0])):
		measure_dict[ingredients[0][i]] = measurements[i]

	for i in ingredients[1]:
		category = ingredients[1][i]
		if category == 'Dairy, Eggs and Milk' and 'eggs' not in i:
			unhealthy_ingredients.append(i)
			print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2

		elif 'butter' in i or 'oil' in i:
			unhealthy_ingredients.append(i)
			print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2

		elif category == 'Meats, Fish and Seafood':
			unhealthy_ingredients.append(i)
			print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2
			if veggies_halved == False:
				for v in veggies:
					veggies_halved = True
					print(v, 'measurement went from', measure_dict[v], " to ", round(2*float(measure_dict[i])*(.5))/2)
					measure_dict[v] = round(2*float(measure_dict[i])*(.5))/2

		elif category == 'Soup' and 'chicken' in i:
			unhealthy_ingredients.append(i.replace("chicken", "beef"))
			print(i, 'became ', i.replace("chicken", "beef"))

		elif category == 'Soup' and 'turkey' in i:
			unhealthy_ingredients.append(i.replace("turkey", "beef"))
			print(i, 'became ', i.replace("turkey", "beef"))

		elif category == 'Pasta, Rice and Beans' and 'whole-wheat' in i:
			unhealthy_ingredients.append(i.replace('whole-wheat', ''))
			print(i, 'became ', i.replace('whole-wheat', ''))

		elif category == 'Pasta, Rice and Beans' and 'whole wheat' in i:
			unhealthy_ingredients.append(i.replace('whole wheat', ''))
			print(i, 'became ', i.replace('whole wheat', ''))

		elif category == 'Pasta, Rice and Beans' and 'brown rice' in i:
			unhealthy_ingredients.append('white rice')
			print(i, 'became ', 'white rice')
		else:
			unhealthy_ingredients.append(i)
	return unhealthy_ingredients

measurements = get_quant(url)
ingredients = get_ingredients(url)
make_healthy(ingredients, measurements)



