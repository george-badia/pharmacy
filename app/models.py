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


# Customer model
class Customer(Base):
    __tablename__ = 'customer'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
   
   #Add relationship to prescription
    prescriptions = relationship('Prescription', back_populates='customer')


   def __repr__(self):
      return f"<Customer:(name={self.name}, phone={self.phone}, email={self.email})>"


#  Medication Model
class Medication(Base):
    __tablename__ = 'medication'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

   #Add relationship to medication
    prescriptions = relationship('Prescription', back_populates='medication')


    def __repr__(self):
        return f'<Medication:(id={self.id}, name="{self.name}")>'


#  Prescription Model
class Prescription(Base):
    __tablename__ = 'prescription'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    medication_id = Column(Integer, ForeignKey('medication.id'))
    date_issued = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    prescriber_name = Column(String, nullable=False)
    instructions = Column(String, nullable=False)

    
   def __repr__(self):
         return f"<Prescription:(customer_id={self.customer_id}, medication_id={self.medication_id}, quantity={self.quantity}, date_issued={self.date_issued} instruction={self.instruction})>"

      