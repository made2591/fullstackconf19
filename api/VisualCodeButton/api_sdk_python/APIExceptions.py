class APIException(Exception):
  pass

class BadRequestException(APIException):
  pass
  
class UnauthorizedException(APIException):
  pass
  
class ForbiddenException(APIException):
  pass
  
class NotFoundException(APIException):
  pass
  
class ConflictException(APIException):
  pass
  
class InternalServerErrorException(APIException):
  pass