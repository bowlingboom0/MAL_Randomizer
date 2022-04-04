import requests

def get_list(user_name):
    anime_list = []

    headers = {"X-MAL-CLIENT-ID": ""} #Enter your api here
    params = {"status": "plan_to_watch", "limit": 1000}


    response = requests.get(f"https://api.myanimelist.net/v2/users/{user_name}/animelist", headers=headers, params=params)

    for anime in response.json()["data"]:
        anime_list.append(anime["node"]["title"])

    return anime_list
