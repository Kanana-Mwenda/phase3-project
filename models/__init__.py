from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#relative imports
from .owner import Owner
from .pet import Pet


