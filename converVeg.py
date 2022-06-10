from difflib import SequenceMatcher
from hashlib import new
from secrets import choice
from web_scraping import get_step, get_ingredients, get_method, get_website, get_quant, get_unit
from bs4 import BeautifulSoup
from helper import meat_sub, meat_list, veg, sau, exc
import requests
import re
import spacy
import random

u = "https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/"

def conver2veg(u):
    result, type = get_ingredients(u)
    steps = get_step(u)
    units = get_unit(u)
    quant = get_quant(u)
    replaces = {}

    # map ing in steps to ing list


    for i in type:
        if any([k in i for k in exc]):
            continue

        if type[i] == 'Meats, Fish and Seafood':
            # print(i)
            if i in replaces:
                continue
            else:
                
                replaces[i] = random.choice(meat_sub)
        
        elif any([k in i for k in meat_list]):
            if 'flavored' in i:
                tem = i
                s = i.find('flavored')
                tem = i[s + 9:]
                replaces[tem] = 'vegan ' + tem
                replaces[i] = 'vegan ' + tem
            elif 'sauce' in i:
                replaces[i] = random.choice(sau)
            
            else: 
                replaces[i] = random.choice(veg)

    ing = get_ingredients(u)
    if len(replaces) == 0:
        print('This is already a vegetarian recipe')
        return
    # update ingredient
    new_ingre = []
    for i in range(len(result)):
        tem = result[i]
        if result[i] in replaces:
            tem = replaces[result[i]]
        if units[i] != '':
            new_line = quant[i] + ' ' + units[i] + ' ' + tem
        else:
            new_line = quant[i] + ' ' + tem
        new_ingre.append(new_line)

    # print(new_ingre)

    # update step
    steps = get_step(u)
    new_steps = []
    for step in steps:
        tem = step

        nlp = spacy.load("en_core_web_sm")
        step = nlp(step.lower())
        for r in replaces:
            for tok in step.noun_chunks:           
                if r in tok.text:
                    tem = tem.replace(r, replaces[r])
                elif tok.text in r:
                    tem = tem.replace(tok.text, replaces[r])
                

        new_steps.append(tem)
        
    # print(new_steps)
    

    # print(replaces)
    return new_ingre, new_steps