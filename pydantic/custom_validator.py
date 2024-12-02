from pydantic import BaseModel, ValidationError, field_validator
from typing import List


class Fruit(BaseModel):
    name: str
    color: str
    weight: float

    @field_validator('weight')
    def weight_is_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('Вес должен быть положительным')
        return v


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
