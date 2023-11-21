GET_BUDGET_BY_ID = """
    SELECT  
        id,
        is_active,
        balance,
        year
    FROM "budget"
    WHERE id = :budget_id
"""

GET_BUDGET_BY_YEAR = """
    SELECT
        id,
        is_active,
        balance,
        year
    FROM "budget"
    WHERE year = :year
"""

CREATE_BUDGET = """
    INSERT INTO "budget" (
        is_active,
        balance,
        year
    )
    VALUES (
        :is_active,
        :balance,
        :year
    ) RETURNING *
"""

DELETE_BUDGET_BY_ID = """
    UPDATE "budget"
    SET
        is_active = :is_active
    WHERE id = :budget_id
    RETURNING *
"""

DELETE_BUDGET_BY_YEAR = """
    UPDATE "budget"
    SET 
        is_active = :is_active
    WHERE year = :year
    RETURNING *
"""
