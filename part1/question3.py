################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.

import json

# ¡FOR THIS EXERCISE, I WANTED TO MAKE A CODE DOCUMENTATION!


def make_oven():
    """
    Return an oven instance

    Returns
    -------
    Oven: An instance of Oven class
    """
    return Oven()


def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    oven.temperature = temperature
    return oven.get_output()


class Oven:
    def __init__(self):
        self._ingredients = []
        self._temperature = 20
        self._output = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

        if temperature < 0:
            self._freeze()
        elif temperature >= 100:
            self._boil()
        else:
            self._wait()

    def add(self, ingredient):
        """
        Add an ingredient to the oven

        Parameters
        ----------
        ingredient : str
            Element or ingredient to be added to the oven
        """
        self._ingredients.append(ingredient)

    def _freeze(self):
        """
        Assigns to the output the result of the preparation by assigning as freeze state
        """
        self._output = self._get_preparation_state("freeze")

    def _boil(self):
        """
        Assigns to the output the result of the preparation by assigning as boil state
        """
        self._output = self._get_preparation_state("boil")

    def _wait(self):
        """
        Assigns to the output the result of the preparation by assigning as wait state
        """
        self._output = " + ".join(self._ingredients)

    def get_output(self):
        """
        Returns the result of the recipe

        Returns
        -------
        str: Recipe result
        """
        return self._output

    def _get_preparation_state(self, state):
        """
        Searches for and returns the preparation of the
        inserted ingredients from the state passed as an argument.

        Parameters
        ----------
        state : str
            State of preparation defined by oven temperature.

        Returns
        -------
        str: The result of the preparation according to the ingredients and temperature.
        None: This value is returned if the combination of ingredients entered is non-existent.
        """
        preparations_state = self._find_combination()

        if not preparations_state:
            return None

        preparations_state = preparations_state[state]

        temperature_comparator = (
            lambda: self.temperature <= int(gr)
            if state == "freeze"
            else lambda: self.temperature >= int(gr)
        )

        grades = preparations_state.keys()

        for gr in grades:
            if temperature_comparator():
                return preparations_state[gr]

    def _find_combination(self):
        """
        Searches for the combination of ingredients inserted in the file
        'recipes.json'.

        Returns
        -------
        dict: Recipe ingredients and the results that can be obtained for each state.
        None: This value is returned if the recipe does not exist in the file 'recipes.json'.
        """
        recipes = None
        with open("recipes.json", "r") as f:
            recipes = json.load(f)

        ingredients_added_sorted = sorted(self._ingredients)

        if recipes:
            for rec in recipes:
                if sorted(rec["ingredients"]) == ingredients_added_sorted:
                    return rec
