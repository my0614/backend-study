from fastapi import APIRouter, Depends
from todos.dependencies import get_todo_service
from todos.schemas import CreateTodoRequest, TodoResponse
from todos.service import TodoService

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=list[TodoResponse])
def get_all_todo(service: TodoService = Depends(get_todo_service)):
    return service.get_all_todos()

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)