import logging 
from pydantic import BaseModel


#Write a line that prins the dynamic name of the current file/module
print(__name__)
#Write a line that prints the internal __name__ attribute of the imported logging module
print(logging.__name__)

def make_object(cls: typ) -> object:
    return cls()

def load_data[T: BaseModel](model_cls: type[T], raw_json: str) -> T | None:
    pass 
