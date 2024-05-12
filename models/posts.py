from pydantic import BaseModel


class Comment(BaseModel):
    id: str 
    content: str

class Post(BaseModel):
    title: str 
    content: str  
    comments: list[Comment]
    likes: int 
    dislikes: int 