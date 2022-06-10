
from __future__ import annotations
from web_scraping import get_ingredients, get_quant, get_unit, get_step
import json
import random
def tansform_to_chinese(url):
    ingrads,b = get_ingredients(url)
    quants = get_quant(url)
    units = get_unit(url)
    steps = get_step(url)
    f = open("ingredient.json", encoding="utf-8")
    data = json.load(f)
    chinese_ingredients = { 
                category: [
            item for item, classes in dic.items() if 'chinese' in classes] for category,
                dic in data['ingredients'].items()}
    
    substitute = {}
    ings = []
    annotations = []
    for ingrad in ingrads:
        temp = ingrad.split(',')
        if len(temp) == 1:
            annotations.append('')
            ings.append(temp[0])
        else:
            annotations.append(temp[1])
            ings.append(temp[0])
    

    for ing in ings:
        if ing not in substitute.keys():
            substitution = find_chinese(ing, data, chinese_ingredients)
            substitute[ing] = substitution
    
    # print()
    # print('ingredients:')
    final_ingredients = []
    for i in range(len(ings)):
        final_ingredients.append(quants[i] + ' ' + units[i] + ' ' + substitute[ings[i]] + annotations[i])
    
    # print()
    # print('steps')
    final_steps = []
    for step in steps:
        for ing in ings:
            step = step.replace(ing, substitute[ing])
        final_steps.append(step)
        # print(step)
    return final_ingredients, final_steps


def find_chinese(ingrad, data, chinese_ingredients):
    category = ''
    needChange = False
    for type, values in data['ingredients'].items():
        for name, style in values.items():
            if name == ingrad:
                category = type
                if 'chinese' not in style:
                    needChange = True
    
    if needChange:
        chinese_substitutions = chinese_ingredients[category]
        upper_bound = len(chinese_substitutions) - 1
        index = random.randint(0, upper_bound)
        chinese_substitution = chinese_substitutions[index]
        return chinese_substitution
    return ingrad

# tansform_to_chinese("https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/")
