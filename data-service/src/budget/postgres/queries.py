IMPORT_BUDGET = """
    INSERT INTO "budget" (
        year,
        balance,
        is_active
    ) VALUES (
        :year,
        :balance,
        :is_active
    )
"""

EXPORT_BUDGET = """
    SELECT * FROM budget
    WHERE
      (balance >= COALESCE(:balance_min, balance))
      AND (balance <= COALESCE(:balance_max, balance))
      AND (year >= COALESCE(:year_min, year))
      AND (year <= COALESCE(:year_max, year))
      AND is_active = true;
"""
