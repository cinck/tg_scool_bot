from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os


class DataBase:

    ModelBase = declarative_base()    # Base class for DB Models

    def __init__(self, db_path):
        self.db_path = db_path
        self.db_engine = create_engine(f"sqlite:///{db_path}")
        self.session = sessionmaker(bind=self.db_engine)()

    def create_db(self):
        if not os.path.exists(self.db_path):
            self.ModelBase.metadata.create_all(self.db_engine)

