CREATE TABLE public.admin
(
    id smallint NOT NULL DEFAULT nextval('admin_id_seq'::regclass),
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    password bytea,
    token character varying(40) COLLATE pg_catalog."default",
    last_login timestamp without time zone,
    last_password_change timestamp without time zone,
    email character varying(100) COLLATE pg_catalog."default",
    secret_key text COLLATE pg_catalog."default",
    role character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT admin_pkey PRIMARY KEY (id),
    CONSTRAINT admin_token_key UNIQUE (token),
    CONSTRAINT admin_username_key UNIQUE (username)
)

CREATE TABLE public.company_group
(
    id integer NOT NULL DEFAULT nextval('account_id_seq'::regclass),
    username character varying(100) COLLATE pg_catalog."default" NOT NULL,
    status character varying(20) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default",
    phone character varying(20) COLLATE pg_catalog."default",
    code character varying(8) COLLATE pg_catalog."default",
    password bytea,
    CONSTRAINT company_group_pkey PRIMARY KEY (id)
)
