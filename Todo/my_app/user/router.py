from fastapi import Query 
from fastapi import APIRouter, Depends
from my_app.user.service import UserService
from my_app.user.dependencies import get_user_service
from my_app.user.schemas import UserRequest, UserReponse

router = APIRouter(prefix="/user", tags=["user"])

# POST /user/create_user
@router.post("/create_user", response_model=UserReponse)
def create_user(request: UserRequest, service: UserService = Depends(get_user_service)):
    return service.create_user(request)

# GET /user/get_user
@router.get("/get_user", response_model=UserReponse)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(id)

# DELETE /user/get_delete
@router.delete("/delete_user", response_model=None)
def delete_user(id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(id)
