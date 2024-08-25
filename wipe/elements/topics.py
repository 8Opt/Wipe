from pydantic import BaseModel, Field

class NewsTopic(BaseModel): 
    id: int
    title: str
    summary: str
    url: str