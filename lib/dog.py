#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="", breed=""):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value, capture_output=False):
        if not isinstance(value, str) or not 1 <= len(value) <= 25:
            error_message = "Name must be a string between 1 and 25 characters."
            if capture_output:
                print(error_message)
            else:
                raise ValueError(error_message)
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value, capture_output=False):
        if value not in self.APPROVED_BREEDS:
            error_message = "Breed must be in the list of approved breeds."
            if capture_output:
                print(error_message)
            else:
                raise ValueError(error_message)
        else:
            self._breed = value

dog = Dog()
dog.name = "bobby"
dog.breed = "Corgi"

print(f"Dog's name is {dog.name}")
print(f"Dog's breed is {dog.breed}")
