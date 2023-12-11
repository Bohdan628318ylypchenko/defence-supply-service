IMPORT_AVAILABILITY = """
    INSERT INTO "availability" (
        is_active,
        supply_id,
        unit_count,
        expiration_date
    ) VALUES (
        :is_active,
        (SELECT id from "supply" where name=:supply_name),
        :unit_count,
        :expiration_date
    )
"""

EXPORT_AVAILABILITY = """
    SELECT 
        a.id,
        a.is_active,
        a.unit_count,
        a.expiration_date,
        s.name as supply_name
    FROM "availability" a
    LEFT JOIN "supply" s ON s.id = a.supply_id
    WHERE
        (a.expiration_date >= COALESCE(:start_date, a.expiration_date))
        AND (a.expiration_date <= COALESCE(:end_date, a.expiration_date))
        AND (a.supply_id = COALESCE(:supply_id, a.supply_id))
        AND a.is_active = true
    ORDER BY a.id;
"""
