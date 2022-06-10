from web_scraping import *

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
			measure_dict['low-fat ' + i] = measure_dict[i]
			# print(i, 'became ', 'low-fat ' + i)

		elif 'butter' in i:
			healthy_ingredients.append("avocado oil")
			measure_dict['avocado oil'] = measure_dict[i]
			# print(i, 'became ', "avocado oil")

		elif category == 'Meats, Fish and Seafood' and 'beef' in i:
			healthy_ingredients.append(i)
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(.5))/2
			if veggies_halved == False:
				for v in veggies:
					veggies_halved = True
					# print(v, 'measurement went from', measure_dict[v], " to ", round(2*(float(measure_dict[v])+float(measure_dict[v])*(.5)))/2)
					measure_dict[v] = round(2*(float(measure_dict[v])+float(measure_dict[v])*(.5))/2)

		elif category == 'Meats, Fish and Seafood' and 'bacon' in i:
			healthy_ingredients.append(i.replace("bacon", "turkey bacon"))
			measure_dict[i.replace("bacon", "turkey bacon")] = measure_dict[i]
			# print(i, 'became ', i.replace("bacon", "turkey bacon"))

		elif category == 'Soup' and 'beef' in i:
			healthy_ingredients.append(i.replace("beef", "chicken"))
			measure_dict[i.replace("beef", "chicken")] = measure_dict[i]
			# print(i, 'became ', i.replace("beef", "chicken"))

		elif category == 'Pasta, Rice and Beans' and 'pasta' in i:
			healthy_ingredients.append("whole-wheat pasta")
			measure_dict["whole-wheat pasta"] = measure_dict[i]
			# print(i, 'became ', "whole-wheat pasta")

		elif category == 'Pasta, Rice and Beans' and 'rice' in i:
			healthy_ingredients.append('brown rice')
			measure_dict["brown rice"] = measure_dict[i]
			# print(i, 'became ', 'brown rice')

		elif category == 'Pasta, Rice and Beans' and 'noodle' in i:
			healthy_ingredients.append('squash noodles')
			measure_dict["squash noodes"] = measure_dict[i]
			# print(i, 'became ', 'squash noodles')

		elif 'olive oil' in i:
			healthy_ingredients.append(i.replace('olive oil', 'avocado oil'))
			measure_dict[i.replace('olive oil', 'avocado oil')] = measure_dict[i]
			# print(i, 'became ', i.replace('olive oil', 'avocado oil'))

		elif category == 'Beverages' and 'wine' in i:
			healthy_ingredients.append('white wine vinegar')
			measure_dict['white wine vinegar'] = measure_dict[i]
			# print(i, 'became ', 'white wine vinegar')

		elif category == 'Herbs and Spices' and 'salt' in i:
			healthy_ingredients.append("lemon juice")
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(.5))/2)
			measure_dict['lemon juice'] = measure_dict[i]
		else:
			healthy_ingredients.append(i)
	return healthy_ingredients, measure_dict

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
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2

		elif 'butter' in i or 'oil' in i:
			unhealthy_ingredients.append(i)
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2

		elif category == 'Meats, Fish and Seafood':
			unhealthy_ingredients.append(i)
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2
			if veggies_halved == False:
				for v in veggies:
					veggies_halved = True
					# print(v, 'measurement went from', measure_dict[v], " to ", round(2*float(measure_dict[i])*(.5))/2)
					measure_dict[v] = round(2*float(measure_dict[i])*(.5))/2
		
		elif 'sugar' in i:
			unhealthy_ingredients.append(i)
			# print(i, 'measurement went from', measure_dict[i], " to ", round(2*float(measure_dict[i])*(1.5))/2)
			measure_dict[i] = round(2*float(measure_dict[i])*(1.5))/2

		elif category == 'Soup' and 'chicken' in i:
			measure_dict[i.replace("chicken", "beef")] = measure_dict[i]
			unhealthy_ingredients.append(i.replace("chicken", "beef"))
			# print(i, 'became ', i.replace("chicken", "beef"))

		elif category == 'Soup' and 'turkey' in i:
			measure_dict[i.replace("turkey", "beef")] = measure_dict[i]
			unhealthy_ingredients.append(i.replace("turkey", "beef"))
			# print(i, 'became ', i.replace("turkey", "beef"))

		elif category == 'Pasta, Rice and Beans' and 'whole-wheat' in i:
			measure_dict[i.replace('whole-wheat', '')] = measure_dict[i]
			unhealthy_ingredients.append(i.replace('whole-wheat', ''))
			# print(i, 'became ', i.replace('whole-wheat', ''))

		elif category == 'Pasta, Rice and Beans' and 'whole wheat' in i:
			measure_dict[i.replace('whole wheat', '')] = measure_dict[i]
			unhealthy_ingredients.append(i.replace('whole wheat', ''))
			# print(i, 'became ', i.replace('whole wheat', ''))

		elif category == 'Pasta, Rice and Beans' and 'brown rice' in i:
			measure_dict['white rice'] = measure_dict[i]
			unhealthy_ingredients.append('white rice')
			# print(i, 'became ', 'white rice')
		else:
			unhealthy_ingredients.append(i)
	return unhealthy_ingredients, measure_dict

# measurements = get_quant(url)
# ingredients = get_ingredients(url)
# make_healthy(ingredients, measurements)



