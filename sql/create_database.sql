/*
This file is used to bootstrap development database.

Note: ONLY development database;
*/

CREATE USER multi_tenant SUPERUSER;
CREATE DATABASE multi_tenant OWNER multi_tenant ENCODING 'utf-8';
