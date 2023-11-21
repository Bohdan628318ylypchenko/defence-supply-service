GET_AVAILABILITY_BY_ID = """
    SELECT 
        id,
        is_active,
        supply_id,
        unit_count,
        expiration_datetime
    FROM "availability"
    WHERE id = :availability_id
"""

CREATE_AVAILABILITY = """
    INSERT INTO "availability" (
        supply_id,
        is_active,
        unit_count,
        expiration_datetime
    ) VALUES (
        :supply_id,
        :is_active,
        :unit_count,
        :expiration_datetime
    ) RETURNING id
"""

GET_AVAILABILITY_LIST_BY_SUPPLY_ID = """
    SELECT 
        id,
        is_active,
        supply_id,
        unit_count,
        expiration_datetime
    FROM "availability"
    WHERE supply_id = :supply_id
"""

DELETE_AVAILABILITY_BY_ID = """
    UPDATE "availability"
    SET
        is_active = :is_active
    WHERE id = :availability_id
    RETURNING 
        id,
        is_active,
        supply_id,
        unit_count,
        expiration_datetime
"""
