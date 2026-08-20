from typing import Optional, List
from pydantic import BaseModel, EmailStr, SecretStr, Field


# Task1
class User1(BaseModel):
    id: int
    name: str
    email: EmailStr


user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com"}
user_json = User1(**user_data).model_dump_json(indent=4)
user1 = User1.model_validate_json(user_json)

# Task2
class User2(User1):
    age: Optional[int] = Field(gt=0, default=None)

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com", "age": 30}
user_data2 = {"id": 2, "name": "Петр", "email": "petr@example.com"}

user2_1 = User2(**user_data).model_dump_json(indent=4)
user2_2 = User2(**user_data2).model_dump_json(indent=4)

# Task3
class Address(BaseModel):
    street: str
    city: str
    zip_code: int

class User3(User1):
    address: Address

user_data = {
    "id": 1,
    "name": "Иван",
    "email": "ivan@example.com",
    "address": {"street": "Тверская", "city": "Москва", "zip_code": "123456"}
}

user_json = User3(**user_data).model_dump_json(indent=4)
user3 = User3.model_validate_json(user_json)

#Task4
class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    items: List[Item]

order_data = {"items": [{"name": "Яблоко", "price": 1.5}, {"name": "Банан", "price": 2.0}]}
order_json = Order(**order_data).model_dump_json(indent=4)
order = Order.model_validate_json(order_json)

#Task5
users_data = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Петр", "email": "petr@example.com"}
]
users = [User1(**user) for user in users_data]
print(users)