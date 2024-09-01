"""
    Define schema for the Event
"""

from datetime import datetime
from uuid import uuid4, UUID
from pydantic import BaseModel, Field


class Event(BaseModel):
    """The Event (Notification) that will be made after the Article is created."""

    id: str = Field(default_factory=lambda: str(uuid4()))  # Generate and convert UUID to string
    title: str
    article_id: str  # Assuming article_id is also a string representation of UUID
    created_at: str = Field(default_factory=datetime.now().isoformat)  # String formatted date

    class Config:
        """Pydantic configuration for cleaner schema definition and example."""
        json_schema_extra = {
            "example": {
                "id": "your-unique-uuid-string",
                "title": "Article Created Notification",
                "article_id": "another-unique-uuid-string",
                "created_at": "2024-09-01T11:43:00+07:00",  # Example ISO formatted date
            }
        }

    def __str__(self):
        """Describe the event in a clear and concise format."""
        return f"""Event ID: {self.id}\nTitle: {self.title}\nArticle ID: {self.article_id}\nCreated At: {self.created_at}"""

class Article(BaseModel):
    """The Article that the Publisher creates."""
    id: str = Field(default_factory=lambda: str(uuid4()))  # Generate and convert UUID to string
    title: str
    description: str
    source: str
    summary: str
    created_at: str = Field(default_factory=datetime.now().isoformat)
    class Config:
        """Pydantic configuration for cleaner string formatting."""
        json_schema_extra = {
            "example": {
                "title": "Interesting Article Title",
                "description": "A short description of the article",
                "source": "https://www.example.com/article",
                "summary": "A concise summary of the article content",
            }
        }

    def __str__(self):
        """Describe the article in a clear and concise format."""
        return f"""Title: {self.title}\nAbstract: {self.description}\nSummary: {self.summary}\nSource: {self.source}"""