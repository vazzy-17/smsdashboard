CREATE TABLE admin
(
    id smallint NOT NULL primary key,
    username varchar(30),
    password bytea,
    token varchar(40),
    last_login timestamp without time zone,
    last_password_change timestamp without time zone,
    email varchar(100),
    secret_key text,
    role varchar(30)
)

CREATE TABLE account_group
(
    id integer NOT NULL primary key,
    username varchar(100),
    status varchar(20),
    email varchar(50),
    phone varchar(20),
    code varchar(8),
    password bytea
)

create table suppliers 
(
    id integer primary key,
    name varchar(100) NOT NULL,
    host varchar(100) NOT NULL,
    port integer NOT NULL,
    system_id varchar(100) NOT NULL,
    password varchar(20) NOT NULL,
    status boolean DEFAULT true,
    priority integer default 1,
    created_at timestamp default now()
)

CREATE SEQUENCE admin_id_seq AS smallint START WITH 1;
CREATE SEQUENCE account_group_id_seq AS smallint START WITH 1;
create SEQUENCE suppliers_is_seq as integer start with 1;
