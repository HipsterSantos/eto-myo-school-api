import os
import json
import random

class ProvinceService:
    def __init__(self, file_path):
        self.provinces = self.load_provinces(file_path)

    def load_provinces(self, file_path):
        with open(file_path) as json_file:
            loaded_province = json.load(json_file)
        return list(loaded_province["Angola"]["Provincias"])

    def get_province(self, index):
        return self.provinces[index] if index < len(self.provinces) else None
    
    def get_full_province(self,name):
        return filter(lambda x: x['nome'] == name, self.provinces)
    
    def get_random_province(self):
        return random.choice(self.provinces) if self.provinces else None
