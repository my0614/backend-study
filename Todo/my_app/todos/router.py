from fastapi import Query 
from fastapi import APIRouter, Depends
from todos.service import TodoService
from todos.dependencies import get_todo_service
from todos.schemas import CreateTodoRequest, TodoResponse, CreateTodoResponse, UpdateTodoRequest, TodoListResponse

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=TodoListResponse)
def get_all_todo(                                                                                                                                                                                         
      is_completed: bool | None = Query(default=None),
      priority: str | None = Query(default=None),                                                                                                                                                           
      service: TodoService = Depends(get_todo_service)                                                                                                                                                      
  ):
    return service.get_all_todos(is_completed,priority)

#GET /todos/{todo_id}
@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

#POST /todos
@router.post("", response_model=CreateTodoResponse,status_code=201)
def create_todo(request: CreateTodoRequest, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(request)

#PATCH todos/{todo_id}
@router.patch("/{todo_id}")
def update_todo(todo_id: int, request: UpdateTodoRequest, service: TodoService = Depends(get_todo_service)):
    service.update_todo(todo_id, request)

#DELETE /todos/{todo_id}
@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    service.delete_todo(todo_id)
