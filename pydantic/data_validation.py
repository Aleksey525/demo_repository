from pydantic import BaseModel, ValidationError
from typing import List


class Fruit(BaseModel):
    name: str
    color: str
    weight: float


class Basket(BaseModel):
    fruits: List[Fruit]


try:
    basket = Basket(
        fruits=[
            Fruit(name='apple', color='green', weight=0.2),
            Fruit(name='banana', color='yellow', weight=0.4)
        ]
    )

    print(basket)

except ValidationError as error:
    print(error)
