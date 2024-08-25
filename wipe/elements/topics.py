from pydantic import BaseModel

class Article(BaseModel): 
    title: str
    summary: str
    url: str