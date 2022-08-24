import json
import requests

NUTRITIONIX_APP_ID = "d55cee16"
NUTRITIONIX_API_KEY = "b44c75399135d0847c095609d9acddb1"

NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_HEADERS = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_API_KEY}

SHEETY_AUTH_KEY = "af4G^nfjs*JDk7(lkd:A#hl247HJklU3!"
SHEETY_ENDPOINT = "https://api.sheety.co/0b894557eeaf40d648330c8d67568854/myWorkouts/workouts"

SHEETY_HEADERS = {"Authorization":"Bearer "+SHEETY}

exercise = "ran 3 miles"

exercise_post_data = {"query": exercise, "gender": "male", "height_cm": 180, "age": 21}

# nutritionix_request = requests.post(
#     url=NUTRITIONIX_EXERCISE_ENDPOINT,
#     json=exercise_post_data,
#     headers=nutritionix_headers,
# )
# exercise_data = nutritionix_request.json()
# with open("exercise_data.json", "w") as f:
#     json.dump(exercise_data, f)
with open("exercise_data.json") as f:
    exercise_dict = json.load(f)
    
print(exercise_dict)

