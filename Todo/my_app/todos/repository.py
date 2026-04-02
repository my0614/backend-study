# todos/repository.py
from sqlalchemy.orm import Session
from todos.models import Todo

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    # Todo 목록 조회
    def get_todo_list(self) -> list[Todo]:
        return self.db.query(Todo).all()

    # Todo 단건 조회
    def get_todo(self, todo_id: int) -> Todo | None:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def save_todo(self, title: str, description: str, priority: str, due_date:str) -> User:
        todo = Todo(title=ntitleame, description=description,priority=priority,due_date=due_date)
        self.db.add(todo)       # INSERT 준비
        self.db.commit()        # DB에 실제로 저장
        self.db.refresh(todo)   # id 등 DB 생성 값 갱신
        return todo

    # Todo 삭제
    def delete(self, todo: Todo) -> None:
        self.db.delete(todo)
        self.db.commit()