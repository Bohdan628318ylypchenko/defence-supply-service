BEGIN;

INSERT INTO public.user_role (role)
VALUES
    ('regular'),
    ('db_administrator'),
    ('accountant'),
    ('commander'),
    ('auditor');

INSERT INTO public.action_type (type)
VALUES
    ('create'),
    ('get'),
    ('delete'),

INSERT INTO public.action_execution_status (status)
VALUES
    ('success'),
    ('fail')

END;