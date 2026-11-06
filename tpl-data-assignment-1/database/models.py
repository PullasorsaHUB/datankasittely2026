from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    # Tämä on uusi tapa tehdä SQLAlcemyssä
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Tämä tapa on taas vanhempi mutta helpompi lukea
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String)
    company_name = Column(String)
    phone = Column(String)
    website = Column(String)