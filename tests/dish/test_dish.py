from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    ingredient1 = Dish("Tomato", 10.0)
    ingredient2 = Dish("Onion", 20.0)

    assert ingredient1.name == "Tomato"
    assert ingredient1.price == 10.0

    assert repr(ingredient1) == "Dish('Tomato', R$10.00)"

    assert hash(ingredient1) == hash("Dish('Tomato', R$10.00)")

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Tomato", "10.0")

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Tomato", -10.0)

    assert ingredient1 == Dish("Tomato", 10.0)

    assert ingredient1 != ingredient2

    assert ingredient1 == ingredient1

    ingredient1.add_ingredient_dependency(Ingredient("Onion"), 1)

    assert ingredient1.recipe == {Ingredient("Onion"): 1}

    assert ingredient1.get_restrictions() == set()

    assert ingredient1.get_ingredients() == {Ingredient("Onion")}
