import logging
from fastapi import HTTPException
from todos.repository import TodoRepository
from todos.models import Todo
from todos.schemas import CreateTodoRequest, UpdateTodoRequest, TodoListResponse, TodoListRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def get_all_todos(self, is_completed: bool | None, priority: str | None) -> TodoListResponse:
        todo_list = self.repository.get_todo_list(is_completed,priority)
        return TodoListResponse(todolist=todo_list)
    
    def get_todo(self, todo_id: int) -> Todo:
        todo = self.repository.get_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        return todo

    def create_todo(self, request: CreateTodoRequest) -> Todo:
        todo_data = self.repository.save_todo(request)
        return todo_data
    
    def update_todo(self, todo_id: int, request: UpdateTodoRequest) -> Todo:
        todo_data = self.repository.update_todo(todo_id, request)
        if todo_data is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        return todo_data
        
    def delete_todo(self, todo_id: int) -> Todo:
        status = self.repository.delete_todo(todo_id)
        if status == False:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")