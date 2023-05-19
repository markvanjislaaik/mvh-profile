import json


def get_profile() -> dict:
    
    with open("./internal/profile.json", "r") as f:
        profile = json.load(f)
    
    return profile