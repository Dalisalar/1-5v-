import os
import json

from numpy import byte

ROOT_PATH = os.getcwd()
PATH_TO_ADVISORY = os.path.join(ROOT_PATH, "assets", "advisory")

def read_advisories(path_to_advisories):
    """Returns all text in advisories"""
    advisories = {}
    for advisory_filename in os.listdir(path_to_advisories):
        advisories[advisory_filename] = ""
        for category_filename in os.listdir(os.path.join(path_to_advisories, advisory_filename)):
            with open(os.path.join(path_to_advisories, advisory_filename, category_filename)) as f:
                category_data = json.load(f)

            category_desc = category_data["description"]
            if category_desc:
                advisories[advisory_filename] += category_desc

            for entry in category_data["entries"]:
                trait = entry["trait"]
                trait_desc = trait["description"]
                advisories[advisory_filename] += trait_desc

    return advisories


def read_categories(path_to_advisories, advisory):
    """Returns all text in categories by advisory name"""
    for advisory_filename in os.listdir(path_to_advisories):
        if advisory_filename != advisory:
            continue

        categories = {}
        for category_filename in os.listdir(os.path.join(path_to_advisories, advisory_filename)):
            with open(os.path.join(path_to_advisories, advisory_filename, category_filename)) as f:
                category_data = json.load(f)
            advisories = {}
            category_desc = category_data["description"]
            if category_desc:
                advisories[advisory_filename] += category_desc

            for entry in category_data["entries"]:
                trait = entry["trait"]
                trait_desc = trait["description"]
                advisories[advisory_filename] += trait_desc


def search_in_advisories(keyword: str):
    """Returns a dict of advisories that include keyword and count of traits with this word"""
    pass


def search_in_categories(keyword: str):
    """Returns a dict of advisories that include keyword and count of traits with this word"""
    pass


def search_in_traits(keyword: str, filter_advisory: str, filter_category: str,):
    """Returns a dict of advisories that include keyword and count of traits with this word"""

    for advisory_name in os.listdir(PATH_TO_ADVISORY):
        if filter_advisory:
            if advisory_name != filter_advisory:
                continue

        for category_filename in os.listdir(os.path.join(PATH_TO_ADVISORY, advisory_name)):
            with open(os.path.join(PATH_TO_ADVISORY, advisory_name, category_filename)) as f:
                category_data = json.load(f)
            category_name = category_data["name"]
            if filter_category:
                if category_name != filter_category:
                    continue

from io import StringIO
import csv

def check_file(bytearr):
    """Check file content is correct"""
    file_is_correct = False

    f = StringIO(bytearr.decode("utf-8"))
    reader = csv.reader(f, delimiter="\t")

    for row in reader:
        if row[0][0] == "#":
            continue
        else:
            if len(row) == 4:
                file_is_correct = True
            break
    
    return file_is_correct