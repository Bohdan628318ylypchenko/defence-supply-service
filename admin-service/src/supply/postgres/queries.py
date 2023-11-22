GET_SUPPLY_BY_ID = """
    SELECT 
        is_active,
        id,
        name,
        unit_cost,
        unit_type,
        norm_unit_count_day
    FROM "supply"
    WHERE id = :supply_id
"""

GET_SUPPLY_BY_NAME = """
    SELECT 
        id,
        is_active,
        name,
        unit_cost,
        unit_type,
        norm_unit_count_day
    FROM "supply"
    WHERE name = :name
"""

CREATE_SUPPLY = """
    INSERT INTO "supply" (
        name,
        unit_cost,
        unit_type,
        norm_unit_count_day,
        is_active
    ) VALUES (
        :name,
        :unit_cost,
        :unit_type,
        :norm_unit_count_day,
        :is_active
    ) RETURNING id 
"""

DELETE_SUPPLY_BY_ID = """
    UPDATE "supply"
    SET 
        is_active = :is_active
    WHERE id = :supply_id
    RETURNING
        id,
        name,
        is_active,
        unit_cost,
        unit_type,
        norm_unit_count_day
"""

DELETE_AVAILABILITY_BY_SUPPLY_ID = """
    UPDATE "availability"
    SET 
        is_active = :is_active
    WHERE supply_id = :supply_id
"""
