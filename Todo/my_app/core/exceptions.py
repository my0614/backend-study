# app/core/exceptions.py
from fastapi import HTTPException

class AppException(HTTPException):
    def __init__(self, status_code: int, code: str, message: str, detail=None):
            super().__init__(status_code=status_code)
            self.code = code
            self.message = message
            self.detail = detail
            
class BadRequestException(AppException):
      def __init__(self, message: str, code: str = "BAD_REQUEST", detail=None):
          super().__init__(400, code, message, detail)
          
class UnauthorizedException(AppException):
    def __init__(self,message:str="인증이 필요합니다",code:str="UNAUTHORIZED"):
        super().__init__(401, code, message)
        
class ForbiddenException(AppException):
    def __init__(self,message:str="접근 권한이 없습니다",code:str="FORBIDDEN"):
        super().__init__(403, code, message)

class NotFoundException(AppException):
      def __init__(self, message: str, code: str = "NOT_FOUND"):
          super().__init__(404, code, message)

class ConflictException(AppException):
      def __init__(self, message: str, code: str = "CONFLICT"):
          super().__init__(409, code, message)