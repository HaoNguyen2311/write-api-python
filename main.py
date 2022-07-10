from lib2to3.pytree import Base
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10,publish:bool='True',sort : Optional[str]= None):
  if(publish):
    return {'data':f'{limit} publish blogs from db list {sort}'}
  else:
    return{'data':f'{limit} blogs from db list'}
  

@app.get('/blog/unpublished')
def show(blog_id: int):
  return {'data' : 'all blog unpublished'}


@app.get('/blog/{blog_id}')
def show(blog_id: int):
  return {'data' : blog_id}


@app.get('/blog/{blog_id}/comments')
def comments():
  return {'data' : {'1','2'}}


class Blog(BaseModel):
  title:str
  body: str
  publish_at: Optional[bool]


@app.post('/blog')
def create_blog(req:Blog):
  return {'data':f'blog is created width title as {req.title}'}