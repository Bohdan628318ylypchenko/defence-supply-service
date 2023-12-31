CREATE_ACTION = """
    INSERT INTO "action" (
        user_id,
        type,
        description,
        start_datetime,
        execution_status
    ) VALUES (
        :user_id,
        :type,
        :description,
        :start_datetime,
        :execution_status
    ) RETURNING id
"""

CREATE_SUPPLY_ACTION = """
    INSERT INTO "supply_action" (
        supply_id,
        action_id
    ) VALUES (
        :supply_id,
        :action_id
    ) RETURNING id
"""

CREATE_AVAILABILITY_ACTION = """
    INSERT INTO "availability_action" (
        availability_id,
        action_id
    ) VALUES (
        :availability_id,
        :action_id
    ) RETURNING id
"""

CREATE_BUDGET_ACTION = """
    INSERT INTO "budget_action" (
        budget_id,
        action_id
    ) VALUES (
        :budget_id,
        :action_id
    ) RETURNING id
"""

SET_STATUS = """
    UPDATE "action"
    SET execution_status = :execution_status
    WHERE id = :action_id
"""

GET_EXECUTION_STATUS_ID = """
    SELECT id FROM "action_execution_status" WHERE status = :status
"""

GET_ACTION_TYPE_ID = """
    SELECT id FROM "action_type" WHERE type = :type
"""
