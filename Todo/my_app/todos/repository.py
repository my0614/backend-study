# todos/repository.py
from datetime import date    
from todos.models import Todo
from sqlalchemy.orm import Session
from todos.schemas import CreateTodoRequest

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    # Todo 목록 조회
    def get_todo_list(self) -> list[Todo]:
        return self.db.query(Todo).all()

    # Todo 단건 조회
    def get_todo(self, todo_id: int) -> Todo | None:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def save_todo(self, request: CreateTodoRequest) -> Todo:
        todo = Todo(title=request.title, description=request.description,  priority=request.priority,due_date=date.fromisoformat(request.due_date))                                                                                                                                                                                                                                                                                                                                   
        self.db.add(todo)       # INSERT 준비
        self.db.commit()        # DB에 실제로 저장
        self.db.refresh(todo)   # id 등 DB 생성 값 갱신
        return todo

    # Todo 삭제
    def delete(self, todo: Todo) -> None:
        self.db.delete(todo)
        self.db.commit()