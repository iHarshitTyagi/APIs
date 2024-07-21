# Import the API
from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel
import uvicorn

# This is the instance we created
app = FastAPI()


# Decorator
@app.get('/')
# Function : What we want to show
def index():
    return 'Hello'

# without using bool it does not run the else statment
# because it was reading true and false as string
# def index(limit, published : bool)

# If you want to set a defaul values
@app.get('/blog')
def index(limit =10, published : bool =True, sort: Optional[str] = None):
    if published :
        return {'data': f'{limit} published blogs from the database'}
    else :
        return {'data': f'{limit} from the database'} 

@app.get('/blog/unpublished')
def unpublished(id):
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id} 

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id =id
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post('/blog')
def create_blog(request : Blog): # or (blog : Blog)
    return {'data' : f'blog is created with title as {request.title}'}

# when we use debug it starts at the same port so we declared new port for out app and debug would run on default port
'''
if __name__ == "__main__":
    uvicorn.run (app,host="127.0.0.1", port =9000)
'''
