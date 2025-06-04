import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel, field_validator

logger = logging.getLogger(__name__)

class Person(BaseModel):
    name: str
    age: int
    address: str
    postal_code: str
    city: str
    country: str
    
    @field_validator("name")
    @classmethod
    def capitalise_name(cls, value: str):
        return value.upper()
     

app = FastAPI()


@app.get("/{name}")
async def welcome(name: str) -> dict:
    """Passing a path parameter it should return
    Welcome, <the parameter value>

    Args:
        name (str): arbitrary string value

    Returns:
        dict: JSONResponse
    """
    return JSONResponse({"detail": f"Welcome, {name.capitalize()}"})


@app.post("/person")
async def create_person(person: Person):
    """Receives a payload in order to create an object type person.
    
    At this point this is only for explanatory purposes and won't be done here.

    Args:
        person (Person): the payload

    Returns:
        Any: anything described
    """
    # insert logic to create a person
    # for example using an ORM to store and return information
    
    return person


@app.delete("/{id}")
async def delete_id(id: int):
    """Delete a person by the corresponding id
    
    At this point this is only for explanatory purposes and won't be done here.

    Args:
        id (int): _description_
    """

    logger.info(f"deleted {id}")
    
       
@app.put("/person")
async def update_person(person: Person):
    """Receives a payload in order to update an object type person.
    
    At this point this is only for explanatory purposes and won't be done here.

    Args:
        person (Person): the payload

    Returns:
        Any: anything described
    """
    # insert logic to update a person
    # for example using an ORM to store and return information
    
    return person.name 
