from pydantic import BaseModel, Field
from typing import Optional

class BookModel(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    pages: int = Field(..., gt=0)
    year: int = Field(..., le=2026)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "O Senhor dos Anéis",
                "author": "J.R.R. Tolkien",
                "pages": 1200,
                "year": 1954
            }
        }