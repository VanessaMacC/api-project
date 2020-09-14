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
import function as fun


def parse():
    parser = argparse.ArgumentParser(description = "¿Qué quieres saber sobre el mundo Pokemon")
    parser.add_argument("-i",dest="number",type=int,help="Escribe el número de Pokemon del que buscas información", default=0)
    parser.add_argument("-n",dest="name",type=str,help="Escribe el nombre de Pokemon del que buscas información (en minúsculas)",default='None')
    parser.add_argument("-s",dest="species",type=str,help="Introduce la especie de Pokemon que quieres comprobar de entre las más populares, :\n - Mouse Pokémon \n - Fox Pokémon \n - Dragon Pokémon \n - Pumpkin Pokémon \n - Flame Pokémon",default='None')
    parser.add_argument("-im",dest="imagen",type=str,help="Introduce el rating mínimo deseado(valor entre 0-9)",default=0)
    args = parser.parse_args()
    return args

def main():
    args=parse()
    number=args.number
    name=args.name
    species=args.species
    imagen=args.imagen
    fun.getPokemonById(args.number)
    fun.getDataSet
    fun.mergeData
    if args.number !=0:
        print(fun.getPokemonById(args.number)) 

data=pd.read_csv("./input/dataset_pokemon.csv")
print(f'El resultado de la media de ataques es: ', data["attack"].mean())
print(f'El resultado del mínimo valor de ataques es: ', data["attack"].min())
print(f'El resultado del máximo valor de ataques es: ', data["attack"].max())


if __name__ == "__main__":
    main()
    