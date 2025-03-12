from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# engine = create_engine("sqlite:///pet_adoption.db")

from .owner import Owner
from .pet import Pet


