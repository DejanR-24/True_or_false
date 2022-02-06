CREATE DATABASE mydb;
CREATE USER mydb_admin WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
ALTER ROLE mydb_admin SET client_encoding TO 'utf8';
ALTER ROLE mydb_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydb_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydb TO mydb_admin;


sudo su postgres
psql
...