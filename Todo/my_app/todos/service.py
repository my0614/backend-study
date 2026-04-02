from fastapi import HTTPException
from todos.repository import TodoRepository
from todos.models import Todo
from todos.schemas import CreateTodoRequest

class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def get_all_todos(self) -> list[Todo]:
        todo_list = self.repository.get_todo_list()
        if todo_list is None:
            raise HTTPException(status_code=404, detail=f"Todo 리스트가 존재하지 않습니다.")
        return todo_list
    
    def get_todo(self, todo_id: int) -> Todo:
        todo = self.repository.get_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        return todo

    def create_todo(self, request: CreateTodoRequest) -> Todo:
        todo_data = self.repository.save_todo(request)
        return todo_data
    
    def update_todo(self, todo_id: int) -> Todo:
        todo_data = self.repository.update_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")
        
    def delete_todo(self, todo_id: int) -> Todo:
        status = self.repository.delete_todo(todo_id)
        if status == False:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {todo_id}")