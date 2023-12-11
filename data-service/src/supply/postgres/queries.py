IMPORT_SUPPLY = """
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
    )
"""

EXPORT_SUPPLY = """
    SELECT * FROM "supply"
    WHERE
      (unit_cost >= COALESCE(:unit_cost_min, unit_cost))
      AND (unit_cost <= COALESCE(:unit_cost_max, unit_cost))
      AND (unit_type = COALESCE(:unit_type, unit_type))
      AND (norm_unit_count_day >= COALESCE(:norm_unit_count_day_min, norm_unit_count_day))
      AND (norm_unit_count_day <= COALESCE(:norm_unit_count_day_max, norm_unit_count_day))
      AND is_active = true;
"""
