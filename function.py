import pandas as pd
from pandas import json_normalize
import numpy as np
import re
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import requests
import json
from IPython.display import Image
import sys
import argparse

def getDataSet():
    global data
    data=pd.read_csv("./input/data_def.csv")


def getPokemonById(id_number):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_number}")
    data = json.loads(res.text)
    pokemon = {
        "name":data["name"],
        "weight":data["weight"],
        "height":data["height"],
        "img":data["sprites"]["front_default"]  
    }
    return json_normalize(pokemon)

def mergeData(data1, data2, name):
    return(data1.merge(data2, left_on=name, right_on=name))

