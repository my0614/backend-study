from user.service import UserService
from fastapi import APIRouter, Depends
from user.schemas import UserRequest, UserReponse
from auth.dependencies import get_current_user_id
from user.dependencies import get_user_service

router = APIRouter(prefix="/user", tags=["user"])

# POST
@router.post("", response_model=UserReponse)
def create_user(request: UserRequest, service: UserService = Depends(get_user_service)):
    return service.create_user(request)

# GET
@router.get("", response_model=UserReponse)
def get_user(id: int = Depends(get_current_user_id), service: UserService = Depends(get_user_service)):
    return service.get_user(id)

# DELETE
@router.delete("", response_model=None)
def delete_user(id: int = Depends(get_current_user_id), service: UserService = Depends(get_user_service)):
    return service.delete_user(id)
