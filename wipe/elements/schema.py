from pydantic import BaseModel

class Article(BaseModel): 
    title: str
    abstract: str
    summary: str
    url: str

    def display(self): 
        return f"""Title: {self.title} \nAbstract: {self.abstract} \nSummary: {self.summary} \nSource: {self.url}"""