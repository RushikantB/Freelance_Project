import json
import os

class LocatorReader:
    def __init__(self, file_path=None):
        if not file_path:
            file_path = os.path.join(os.path.dirname(__file__), '../Resources/Locators.json')
        with open(file_path, 'r') as file:
            self.locators = json.load(file)

    def get(self, page, element):
        try:
            return self.locators[page][element]
        except KeyError:
            raise Exception(f"Locator for '{element}' not found on page '{page}'")
