from fastapi import Query 
from fastapi import APIRouter, Depends
from todos.service import TodoService
from todos.dependencies import get_todo_service
from auth.dependencies import get_current_user_id
from todos.schemas import UpdateTodoRequest, TodoItem, TodoList, TodoListRequest

router = APIRouter(prefix="/todos", tags=["todos"])

# GET /todos
@router.get("", response_model=TodoList)
def get_all_todo(user_id: int = Depends(get_current_user_id), request: TodoListRequest = Depends(), service: TodoService = Depends(get_todo_service)):
    request.user_id = user_id
    return service.get_all_todos(request)

#GET /todos/overdue
@router.get("/overdue")
def overdue_todo(user_id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.get_overdue_todo(user_id)
    
#GET /todos/{todo_id}
@router.get("/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int, user_id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id, user_id)

#POST /todos
@router.post("", response_model=TodoItem, status_code=201)
def create_todo(request: TodoItem, user_id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    request.user_id = user_id 
    return service.create_todo(request)

#PATCH todos/{todo_id}
@router.patch("/{todo_id}", response_model=TodoItem, status_code=200)
def update_todo(todo_id: int, request: UpdateTodoRequest, user_id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    request.user_id = user_id
    return service.update_todo(todo_id, request)

#DELETE /todos/{todo_id}
@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, user_id: int = Depends(get_current_user_id), service: TodoService = Depends(get_todo_service)):
    service.delete_todo(todo_id, user_id)
