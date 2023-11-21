-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;

CREATE TABLE IF NOT EXISTS public.supply
(
    id bigserial NOT NULL,
    is_active boolean NOT NULL DEFAULT true,
    name character varying(128) NOT NULL,
    unit_cost double precision NOT NULL,
    unit_type character varying(16) NOT NULL DEFAULT 'unit',
    norm_unit_count_day double precision NOT NULL DEFAULT 1.0,
    PRIMARY KEY (id),
    UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.availability
(
    id bigserial NOT NULL,
    is_active boolean NOT NULL DEFAULT true,
    supply_id bigint NOT NULL,
    unit_count bigint NOT NULL,
    expiration_datetime timestamp without time zone NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.budget
(
    id bigserial NOT NULL,
    is_active boolean NOT NULL DEFAULT true,
    balance double precision NOT NULL,
    year smallint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (year)
);

CREATE TABLE IF NOT EXISTS public."user"
(
    id bigserial NOT NULL,
    is_active boolean NOT NULL DEFAULT true,
    login character varying(64) NOT NULL,
    password character varying(512) NOT NULL,
    creation_datetime timestamp without time zone NOT NULL,
    last_login_datetime timestamp without time zone NOT NULL,
    role_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (login)
);

CREATE TABLE IF NOT EXISTS public.user_role
(
    id bigserial NOT NULL,
    role character varying(16) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.action
(
    id bigserial NOT NULL,
    user_id bigint NOT NULL,
    type bigint NOT NULL,
    description text NOT NULL,
    start_datetime timestamp without time zone NOT NULL,
    execution_status bigint NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.action_type
(
    id bigserial NOT NULL,
    type character varying(16) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.action_execution_status
(
    id bigserial NOT NULL,
    status character varying(16) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.supply_action
(
    id bigserial NOT NULL,
    supply_id bigint,
    action_id bigint NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.availability_action
(
    id bigserial NOT NULL,
    availability_id bigint,
    action_id bigint NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.budget_action
(
    id bigserial NOT NULL,
    budget_id bigint,
    action_id bigint NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.availability
    ADD FOREIGN KEY (supply_id)
    REFERENCES public.supply (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."user"
    ADD FOREIGN KEY (role_id)
    REFERENCES public.user_role (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.action
    ADD FOREIGN KEY (user_id)
    REFERENCES public."user" (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.action
    ADD FOREIGN KEY (type)
    REFERENCES public.action_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.action
    ADD FOREIGN KEY (execution_status)
    REFERENCES public.action_execution_status (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.supply_action
    ADD FOREIGN KEY (supply_id)
    REFERENCES public.supply (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.supply_action
    ADD FOREIGN KEY (action_id)
    REFERENCES public.action (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.availability_action
    ADD FOREIGN KEY (availability_id)
    REFERENCES public.availability (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.availability_action
    ADD FOREIGN KEY (action_id)
    REFERENCES public.action (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.budget_action
    ADD FOREIGN KEY (budget_id)
    REFERENCES public.budget (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.budget_action
    ADD FOREIGN KEY (action_id)
    REFERENCES public.action (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;