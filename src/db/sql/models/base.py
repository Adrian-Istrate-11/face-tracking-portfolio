from sqlalchemy.orm import declarative_base

# base class for SQL objects
SQL_Base = declarative_base()

# Creates an instance of the declarative base class and assigns it to the variable SQL_Base.
# Any model class you define (representing a database table) will inherit from SQL_Base.
# SQL_Base contains metadata about all the models you define (e.g., table names, columns, relationships).
# This metadata is used to manage the database schema or reflect existing schemas.
