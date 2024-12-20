from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    color: str
    weight: float


fruit = Fruit(name='apple', color='green', weight=0.2)
fruit_json = fruit.model_dump_json()
print(fruit_json)
