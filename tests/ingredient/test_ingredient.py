from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Onion")

    assert ingredient1.name == "Tomato"

    assert hash(ingredient1) == hash("Tomato")

    assert repr(ingredient1) == "Ingredient('Tomato')"

    assert ingredient1 == ingredient1

    assert ingredient1 != ingredient2

    assert ingredient1.restrictions == set()
