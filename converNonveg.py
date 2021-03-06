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

def conver2Nonveg(u):
    result, type = get_ingredients(u)
    steps = get_step(u)
    units = get_unit(u)
    quant = get_quant(u)
    replaces = {}
    # print(result)
    for ingred in result:
        if any([k in ingred for k in meat_list]) or any([ingred in k for k in meat_list]):
            print('This is already a non-vegetarian recipe')
            return []
    # we don't want all the vegetable transfer to meat(2 is enough)
    count = 0
    for i in result:
        if count == 2:
            return
        if type[i] == 'Basic Cooking Ingredients':
            continue
        if len(i) > 1:
            i_NonPlural = i[:-1]
        if i in meat_sub or i in veg or i_NonPlural in meat_sub or i_NonPlural in veg:
            if i in replaces:
                continue
            else:                
                replaces[i] = random.choice(meat_list)
                count += 1
        nlp = spacy.load("en_core_web_sm")
        step = nlp(i)
        for tok in step:
            if len(tok.text) > 1:
                tok_NonPlural = tok.text[:-1]
            if tok.text in meat_sub or tok.text in veg or tok_NonPlural in meat_sub or tok_NonPlural in veg:
                replaces[i] = tok.text.replace(tok.text, random.choice(meat_list))
                count += 1
                break

    ing = get_ingredients(u)

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

    return new_ingre, new_steps

