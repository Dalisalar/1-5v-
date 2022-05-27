import os
import json

def search_in_advisories(query: str, path_to_advisories: str):
    advisories = []
    for advisory_label, advisory_path in enumerate(os.listdir(path_to_advisories)):
        advisory_text = ""
        for category_path in os.listdir(os.path.join(path_to_advisories, advisory_path)):
            with open(os.path.join(path_to_advisories, advisory_path, category_path)) as f:
                data = json.load(f)
            
            if data["description"]:
                advisory_text += data["description"]

            for entry in data["entries"]:
                advisory_text += entry["trait"]["description"]
        
        advisories.append([advisory_path, advisory_label, advisory_text.count(query)])

    return advisories


def search_in_categories(query: str, path_to_advisories: str, advisory_key: int):
    """Returns a dict of advisories that include keyword and count of traits with this word"""
    categories = []
    for advisory_label, advisory_path in enumerate(os.listdir(path_to_advisories)):
        if advisory_label != advisory_key:
            continue
        category_text = ""
        for category_label, category_path in enumerate(os.listdir(os.path.join(path_to_advisories, advisory_path))):
            with open(os.path.join(path_to_advisories, advisory_path, category_path)) as f:
                data = json.load(f)
            
            category_name = data["name"]
            if data["description"]:
                category_text += data["description"]

            for entry in data["entries"]:
                category_text += entry["trait"]["description"]
        
            categories.append([category_name, category_label, category_text.count(query)])
    
    return categories


def search_in_traits(keyword: str, filter_advisory: str, filter_category: str,):
    """Returns a dict of advisories that include keyword and count of traits with this word"""
    pass