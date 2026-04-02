from fastapi import Query 
from fastapi import APIRouter, Depends
from todos.service import TodoService
from todos.dependencies import get_todo_service
from todos.schemas import UpdateTodoRequest, TodoItem, TodoList, TodoListRequest

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=TodoList)
def get_all_todo(request: TodoListRequest = Depends(), service: TodoService = Depends(get_todo_service)):
    return service.get_all_todos(request)

#GET /todos/{todo_id}
@router.get("/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

#POST /todos
@router.post("", response_model=TodoItem,status_code=201)
def create_todo(request: TodoItem, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(request)

#PATCH todos/{todo_id}
@router.patch("/{todo_id}")
def update_todo(todo_id: int, request: UpdateTodoRequest, service: TodoService = Depends(get_todo_service)):
    service.update_todo(todo_id, request)

#DELETE /todos/{todo_id}
@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    service.delete_todo(todo_id)
