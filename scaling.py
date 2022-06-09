from web_scraping import *

url = 'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/'

def scale(ingredients, measurements, s):
	factor = 0
	if s == 'double':
		factor = 2
	elif s == 'half':
		factor = .5
	else:
		print('Invalid Scale! Please enter double or half')
		return
	measure_dict = {}
	for i in range(len(ingredients[0])):
		measure_dict[ingredients[0][i]] = measurements[i]
	scaled_measurements = {}
	for i in ingredients[1]:
		print(i, ' went from ', measure_dict[i], ' to ', float(measure_dict[i]) * float(factor))
		scaled_measurements[i] = float(measure_dict[i]) * float(factor)
	return scaled_measurements


measurements = get_quant(url)
ingredients = get_ingredients(url)
scale(ingredients, measurements, 'double')