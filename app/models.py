from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an SQLite database engine and initialize the database schema
engine = create_engine('sqlite:///pharmacy.db')
Base.metadata.create_all(engine)
# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)
session = Session()

# Define the declarative base class
Base = declarative_base()

# Define the Medication class
class Medication(Base):
    __tablename__ = 'medication'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


      