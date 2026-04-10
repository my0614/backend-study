from fastapi import Query 
from fastapi import APIRouter, Depends
from todos.service import TodoService
from todos.dependencies import get_todo_service
from auth.dependencies import get_current_user_id
from todos.schemas import UpdateTodoRequest, TodoItem, TodoList, TodoListRequest

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=TodoList)
def get_all_todo(id: int = Depends(get_current_user_id), request: TodoListRequest = Depends(), service: TodoService = Depends(get_todo_service)):
    return service.get_all_todos(request)

#GET /todos/overdue
@router.get("/overdue")
def overdue_todo(id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.get_overdue_todo()
    
#GET /todos/{todo_id}
@router.get("/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int, id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

#POST /todos
@router.post("", response_model=TodoItem, status_code=201)
def create_todo(request: TodoItem, id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.create_todo(request)

#PATCH todos/{todo_id}
@router.patch("/{todo_id}", response_model=TodoItem, status_code=200)
def update_todo(todo_id: int, request: UpdateTodoRequest, id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.update_todo(todo_id, request)

#DELETE /todos/{todo_id}
@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    service.delete_todo(todo_id)
