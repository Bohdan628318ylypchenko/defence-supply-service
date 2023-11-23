from fastapi import HTTPException, status
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


INTERNAL_ERROR = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Internal error"
)

AVAILABILITY_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Availability not found"
)

AVAILABILITY_CREATION_FAIL = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Availability creation failed"
)

SUPPLY_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Supply not found"
)

SUPPLY_CREATION_FAIL = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Supply creation failed"
)

ACTION_CREATION_FAIL = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Action creation failed"
)

BUDGET_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Budget not found"
)

BUDGET_CREATION_FAIL = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Budget creation failed"
)

BUDGET_ACTION_CREATION_FAIL = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="budget action creation failed"
)

AVAILABILITY_ACTION_CREATION_FAIL = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Availability action creation fail"
)

SUPPLY_ACTION_CREATION_FAIL = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Supply action creation fail"
)

EXECUTION_STATUS_NOT_FOUND = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="Execution status not found"
)

ACTION_TYPE_NOT_FOUND = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="Action status not found"
)

STATUS_UPDATE_FAIL = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail="Status update fail"
)
