from web_scraping import *
from lactose_free import *
from converNonveg import *
from conversions import *
from converVeg import *
from scaling import *
from tansform_to_chinese import *

def convert_from_veg(url):
	res = conver2Nonveg(url)
	if len(res)>1:
		ingredients, steps = res
		print('Updated Ingredients:')
		for i in ingredients:
			print(i)
		print('Updated Steps:')
		for s in steps:
			print(s)

def convert_to_veg(url):
	res = conver2veg(url)
	if len(res)>1:
		ingredients, steps = res
		print('Updated Ingredients:')
		for i in ingredients:
			print(i)
		print('Updated Steps:')
		for s in steps:
			print(s)

def convert_to_healthy(url, measurements, orig_ingredients):
	ingredients, measure_dict = make_healthy(orig_ingredients, measurements)
	print('Updated Ingredients/Measurements:')
	units = get_unit(url)
	for i, ing in enumerate(ingredients):
		if units[i] != ' ':
			print(measure_dict[ing], ' ', units[i], ' ', ing)
		else:
			print(measure_dict[ing], ' ', ing)


def convert_to_unhealthy(url, measurements, orig_ingredients):
	ingredients, measure_dict = make_unhealthy(orig_ingredients, measurements)
	print('Updated Ingredients/Measurements:')
	units = get_unit(url)
	for i, ing in enumerate(ingredients):
		if units[i] != ' ':
			print(measure_dict[ing], ' ', units[i], ' ', ing)
		else:
			print(measure_dict[ing], ' ', ing)

def convert_to_chinese(url):
	printed = []
	ingredients, steps = tansform_to_chinese(url)
	print()
	print('Updated Ingredients:')
	for i in ingredients:
		print(i)
	print()
	print('Updated Steps:')
	for s in steps:
		if s not in printed:	
			print(s)
		printed.append(s)

def double_recipe(url):
	steps = get_step(url)
	for step in steps:
		newStr = ''
		temp = step
		for w in temp.split(' '):
			if w.isdigit():
				newStr += str(float(w)*2)
			else:
				newStr += w
			newStr += ' '
		print(newStr)

def half_recipe(url):
	steps = get_step(url)
	for step in steps:
		newStr = ''
		temp = step
		for w in temp.split(' '):
			if w.isdigit():
				newStr += str(float(w)*.5)
			else:
				newStr += w
			newStr += ' '
		print(newStr)

def remove_lactose(url, measurements, orig_ingredients):
	ingredients = lactose_free(orig_ingredients)
	print('Updated Ingredients:')
	units = get_unit(url)
	for i, ing in enumerate(ingredients):
		if units[i] != ' ':
			print(measurements[i], ' ', units[i], ' ', ing)
		else:
			print(measurements[i], ' ', ing)

def print_descriptor(url):
	res = get_descriptor(url)
	for r in res:
		print(r)

def menu():
	print('Welcome to the Interactive Cookbook!')
	print('Please input the URL of your recipe:')
	url = input()
	measurements = get_quant(url)
	orig_ingredients, ingredient_types = get_ingredients(url)
	ingredients = get_ingredients(url)
	quantities = get_quant(url)
	units = get_unit(url)
	print()
	print('Tools:')
	for i in get_tool(url):
		print(i)
	print()
	print('Method:')
	for i in get_method(url):
		print(i)
	print()
	print('Ingredients:')
	for i, ing in enumerate(ingredients[0]):
		if units[i] != ' ':
			print(quantities[i], ' ', units[i], ' ', ing)
		else:
			print(quantities[i], ' ', ing)
	print()
	print('Steps:')
	for step in get_step(url):
		print(step)
	print()
	repeat = True
	while repeat == True:
		print('What would you like to do with this recipe? Please enter a number.')
		print('1. Alter based on dietary needs/preferences')
		print('2. Alter based on quantity or style.')
		print('3. Get info about recipe.')
		valid_choice = False
		choice1 = int(input())
		if choice1 == 'x':
			break
		while valid_choice == False:
			if choice1 == 1:
				print('Please select an option below.')
				print('1. Make this recipe vegetarian.')
				print('2. Make this recipe non-vegetarian.')
				print('3. Make this recipe healthier.')
				print('4. Make this recipe less healthy.')
				print('5. Make this recipe lactose free.')
				choice1_2 = int(input())
				valid_choice = True
				if valid_choice:
					if choice1_2 == 1:
						convert_to_veg(url)
					elif choice1_2 == 2:
						convert_from_veg(url)
					elif choice1_2 == 3:
						convert_to_healthy(url, measurements, [orig_ingredients,ingredient_types])
					elif choice1_2 == 4:
						convert_to_unhealthy(url, measurements, [orig_ingredients,ingredient_types])
					elif choice1_2 == 5:
						remove_lactose(url, measurements, [orig_ingredients,ingredient_types])
					else:
						print('Invalid Choice! Try Again.')
						valid_choice = False
						break
			elif choice1 == 2:
				print('1. Make this recipe in Chinese style.')
				print('2. Double this recipe.')
				print('3. Cut this recipe in half')
				choice2_2 = int(input())
				valid_choice = True
				if valid_choice:
					if choice2_2 == 1:
						convert_to_chinese(url)
					elif choice2_2 == 2:
						double_recipe(url)
					elif choice2_2 == 3:
						half_recipe(url)
			elif choice1 == 3:
				print('1. Return a list of ingredient descriptors/preparations.')
				choice3_2 = int(input())
				valid_choice = True
				if valid_choice:
					if choice3_2 == 1:
						print_descriptor(url)
			else:
				print('Invalid choice! Try again.')

def main():
	menu()
	

if __name__ == '__main__':
    main()