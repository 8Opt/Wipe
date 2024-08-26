from pydantic import BaseModel


class Notify(BaseModel): 
    id: int
    title: int
    article_id: int

class Article(BaseModel): 
    id: int
    title: str
    description: str
    source: str
    summary: str

    def display(self): 
        return f"""Title: {self.title} \nAbstract: {self.description} \nSummary: {self.summary} \nSource: {self.source}"""