from bs4 import BeautifulSoup
import nltk
import requests
import re
import spacy
from collections import Counter

def get_toollist(filename):
    my_file = open(filename, "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    for i in range(len(data_into_list)):
        data_into_list[i] = data_into_list[i].lower()
    my_file.close()
    return data_into_list

def get_website(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    result=soup.find_all("input", {"class":"checkbox-list-input"})
    #dict contains all information about food

    return result


def get_ingredients(url):
    temp = get_website(url)
    result = []
    for i in temp:
        t = i.attrs
        if "data-ingredient" in t:
            result.append(t["data-ingredient"])
    print(result)
    return result

def get_quant(url):
    temp = get_website(url)
    result = []
    for i in temp:
        t = i.attrs
        if "data-init-quantity" in t:
            result.append(t["data-init-quantity"])
    print(result)
    return result


def get_unit(url):
    temp = get_website(url)
    result = []
    for i in temp:
        t = i.attrs
        if "data-unit" in t:
            result.append(t["data-unit"])
    print(result)
    return result

def get_step(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    steps = []
    result=soup.find_all(class_ = "paragraph")
    for step in result:
        steps.append(step.get_text())
    return steps

def get_tool(url):
    nlp = spacy.load("en_core_web_sm")
    steps = get_step(url)
    tool_list = get_toollist("Kitchentools.txt")
    result = []
    for step in steps:
        doc = nlp(step)
        for token in doc:
            if (token.pos_ == "NOUN" or token.pos_ == "PROPN") and token.text.lower() in tool_list:
                result.append(token.text.lower())
    for step in steps:
        step = step.split()
        for i in step:
            doc = nlp(i)
            for token in doc:
                if (token.pos_ == "NOUN" or token.pos_ == "PROPN") and token.text.lower() in tool_list:
                    result.append(token.text.lower())
    result = set(result)
    print(result)
    return result

def get_method(url):
    nlp = spacy.load("en_core_web_sm")
    steps = get_step(url)
    tool_list = get_toollist("Method.txt")
    result = []
    for step in steps:
        doc = nlp(step)
        for token in doc:
            if token.pos_ == "VERB" and token.text.lower() in tool_list:
                result.append(token.text.lower())
    for step in steps:
        step = step.split()
        for i in step:
            doc = nlp(i)
            for token in doc:
                if token.pos_ == "VERB" and token.text.lower() in tool_list:
                    result.append(token.text.lower())
    result = set(result)
    print(result)
    return result

u = "https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/"
#get_website(u)
#get_toollist("Kitchentools.txt")
#get_step(u)
get_tool(u)
get_method(u)
#get_ingredients(u)
#get_quant(u)
#get_unit(u)
    