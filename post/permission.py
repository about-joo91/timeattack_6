from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsCandidate(BasePermission):
    """
    candidate만 사용가능
    """
    message = '접근 권한이 없습니다.'
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail" : "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED,detail=response)
        if user.user_type_id != 1:
            response = {
                "detail" : "지원자만 지원을 할 수 있습니다."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED,detail=response)
        if user.user_type_id == 1:
            return True
        return False