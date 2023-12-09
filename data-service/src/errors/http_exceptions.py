from fastapi import HTTPException, status
from starlette.status import HTTP_400_BAD_REQUEST


INTERNAL_ERROR = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Internal error"
)


INVALID_BUDGET_IMPORT_HEADER_ERROR = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Invalid budget import header"
)


INVALID_BUDGET_IMPORT_BODY_ERROR = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Invalid budget import body"
)


BUDGET_YEAR_UNIQUE_VIOLATION = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Budget year should be unique"
)

SUPPLY_UNIQUE_VIOLATION_ERROR = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Supply name should be unique"
)


INVALID_SUPPLY_IMPORT_HEADER_ERROR = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Invalid supply import header"
)


INVALID_SUPPLY_IMPORT_BODY_ERROR = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Invalid supply import body"
)

INVALID_AVAILABILITY_IMPORT_HEADER = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Invalid availability import header"
)

INVALID_AVAILABILITY_IMPORT_BODY = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Invalid availability import body"
)

AVAILABILITY_FOREIGN_KEY_VIOLATION = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Availability creation failed"
)

