from pydantic import BaseModel
from pydantic_core import from_json


class Fruit(BaseModel):
    name: str
    color: str
    weight: float


fruit = Fruit(name='apple', color='green', weight=0.2)
fruit_json = fruit.model_dump_json()
try:
    result = from_json(fruit_json, allow_partial=False)
    print(result)
except ValueError as error:
    print(error)