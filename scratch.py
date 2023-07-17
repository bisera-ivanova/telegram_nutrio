import json

import requests
from py_edamam import Edamam

API_KEY = "429455007444f9ca9fbdcb4da3a1c2c4	"
API_ID = "3cc47b2b"

edamam = Edamam(nutrition_appid=API_ID, nutrition_appkey=API_KEY)

recipe_data = edamam.search_nutrient("100 grams chicken breast")

print(recipe_data)
