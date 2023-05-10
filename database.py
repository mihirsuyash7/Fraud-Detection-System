# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine

Base=declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    Id=Column(Integer, primary_key=True)        # Creating Column for ID
    Transaction_Type=Column(String(10), nullable=True)      # Creating Column for Transaction Type
    Transaction_Amount=Column(Float, nullable=True)         # Creating Column for Amount
    Source_Account=Column(String(15), nullable=True)  # Creating Column for Sender's Account Number
    SA_Old_Balance=Column(Float, nullable=True) # Creating Column for Old Balance of Sender's Account
    SA_New_Balance=Column(Float, nullable=True) # Creating Column for New Balance of Sender's Account
    Destination_Account=Column(String(15), nullable=True)  # Creating Column for Receiver's Account Number
    DA_Old_Balance=Column(Float, nullable=True) # Creating Column for Old Balance of Receiver's Account
    DA_New_Balance=Column(Float, nullable=True) # Creating Column for New Balance of Receiver's Account
    Date=Column(String(15), nullable=True)   # Creating Column for Date of Transaction
    Time=Column(String(15), nullable=True)   # Creating Column for Time of Transaction
    Prediction=Column(String(15), nullable=True)    # Creating Column for Fraudulent Transaction Prediction

    def __str__(self):
        return self.type

engine=create_engine('sqlite:///project.sqlite')
Base.metadata.create_all(engine)
