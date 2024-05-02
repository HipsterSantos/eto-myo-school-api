import os
import json
import random

class ProvinceService:
    def __init__(self):
        pass
    
    @staticmethod
    def load_provinces():
        with open(os.path.join(os.path.dirname(__file__), '../static/province.json')) as json_file:
            loaded_province = json.load(json_file)
        return list(loaded_province["Angola"]["Provincias"])
    
    @staticmethod
    def get_province(index):
        provinces = ProvinceService.load_provinces()
        return provinces[index] if index < len(provinces) else []
    
    @staticmethod
    def get_random_province():
        provinces = ProvinceService.load_provinces()
        return random.choice(provinces) if provinces else None
