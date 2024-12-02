from pydantic import BaseModel, ValidationError, AfterValidator
from typing import Annotated
from typing import List


def weight_is_positive(v: float) -> float:
    if v <= 0:
        raise ValueError('Вес должен быть положительным')
    return v


PositiveFloat = Annotated[float, AfterValidator(weight_is_positive)]


class Fruit(BaseModel):
    name: str
    color: str
    weight: PositiveFloat


class Basket(BaseModel):
    fruits: List[Fruit]


try:
    basket = Basket(
        fruits=[
            Fruit(name='apple', color='green', weight=0.2),
            Fruit(name='banana', color='yellow', weight=-6)
        ]
    )

    print(basket)

except ValidationError as error:
    print(error)
