from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []
# get all todos
@app.get("/todos")
async def get_todos():
    return todos

# get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

# create a new todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}

# update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return {"message": "Todo updated successfully"}
    return {"message": "Todo not found"}

# delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            del todos[i]
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}