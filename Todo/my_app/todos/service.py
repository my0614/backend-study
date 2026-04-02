import logging
from todos.models import Todo
from fastapi import HTTPException
from todos.repository import TodoRepository
from todos.schemas import TodoItem, TodoList, TodoListRequest, UpdateTodoRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def get_all_todos(self, request: TodoListRequest) -> TodoList:
        todo_list = self.repository.get_todo_list(request)
        return TodoList(todolist=todo_list)
    
    def get_todo(self, todo_id: int) -> TodoItem:
        todo = self.repository.get_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        return todo

    def create_todo(self, request: TodoItem) -> TodoItem:
        todo = self.repository.save_todo(request)
        return todo
    
    def update_todo(self, todo_id: int, request: UpdateTodoRequest) -> TodoItem:
        todo = self.repository.update_todo(todo_id, request)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        return todo
        
    def delete_todo(self, todo_id: int) -> None:
        status = self.repository.delete_todo(todo_id)
        if status == False:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
    
    def get_overdue_todo(self) -> TodoList:
        todo = self.repository.get_overdue_todo()
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다.")
        return TodoList(todolist=todo)
