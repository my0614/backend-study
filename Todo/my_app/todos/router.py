from fastapi import APIRouter, Depends
from todos.dependencies import get_todo_service
from todos.schemas import CreateTodoRequest, TodoResponse, CreateTodoResponse
from todos.service import TodoService

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=list[TodoResponse])
def get_all_todo(service: TodoService = Depends(get_todo_service)):
    return service.get_all_todos()

#GET /todos/{todo_id}
@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

#POST /todos
@router.post("", response_model=CreateTodoResponse,status_code=201)
def create_todo(request: CreateTodoRequest, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(request)