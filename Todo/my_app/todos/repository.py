# todos/repository.py
import logging
from datetime import date
from todos.models import Todo
from sqlalchemy.orm import Session
from todos.schemas import UpdateTodoRequest, TodoListRequest, TodoItem, TodoList

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    # Todo 목록 조회
    def get_todo_list(self, request: TodoListRequest) -> TodoList:                                                                                                                   
      query = self.db.query(Todo)                                                        
      if request.is_completed is not None:
          query = query.filter(Todo.is_completed == request.is_completed)                                                                                                                                    
      if request.priority is not None:                                   
          query = query.filter(Todo.priority == request.priority)                                                                                                                                               
      return query.order_by(Todo.due_date).all() 

    # Todo 단건 조회
    def get_todo(self, todo_id: int) -> Todo | None:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    # Todo 저장
    def save_todo(self, request: TodoItem) -> Todo:
        todo = Todo(title=request.title, description=request.description, priority=request.priority, due_date=request.due_date)                                                                                                                                                                                                                                                                                                                                   
        self.db.add(todo)     
        self.db.commit()
        self.db.refresh(todo) # id 등 DB 생성 값 갱신
        return todo

    # Todo 수정
    def update_todo(self, todo_id: int, request: UpdateTodoRequest) -> Todo | None:
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        if todo:
            update_data = request.model_dump(exclude_none=True) # True -> none 제외
            for key, value in update_data.items():
                
                setattr(todo, key, value)
            
            self.db.commit()
            self.db.refresh(todo)
            return todo
    
    # Todo 삭제
    def delete_todo(self, todo_id: int) -> bool:
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        if todo:
            self.db.delete(todo)
            self.db.commit()
            return True
        
        return False
