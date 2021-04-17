from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Persisted = declarative_base()


class Survey(Persisted):
    __tablename__ = 'survey'
    survey_id = Column(Integer, primary_key=True)
    timestamp = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(256), nullable=False)
    state = Column(String(256), nullable=False)
    country = Column(String(256), nullable=False)
    selfEmployed = Column(String(256), nullable=False)
    familyHistory = Column(String(256), nullable=False)
    treatment = Column(String(256), nullable=False)
    workInterfere = Column(String(256), nullable=False)
    noEmployees = Column(String(256), nullable=False)
    remoteWork = Column(String(256), nullable=False)
    techCompany = Column(String(256), nullable=False)
    benefits = Column(String(256), nullable=False)
    careOptions = Column(String(256), nullable=False)
    wellnessProgram = Column(String(256), nullable=False)
    seekHelp = Column(String(256), nullable=False)
    anonymity = Column(String(256), nullable=False)
    workLeave = Column(String(256), nullable=False)
    mentalHealthConsequence = Column(String(256), nullable=False)
    physHealthConsequence = Column(String(256), nullable=False)
    coworkers = Column(String(256), nullable=False)
    supervisor = Column(String(256), nullable=False)
    mentalHealthInterview = Column(String(256), nullable=False)
    physHealthInterview = Column(String(256), nullable=False)
    mentalVsPhysical = Column(String(256), nullable=False)
    obsConsequence = Column(String(256), nullable=False)
    comments = Column(String(256), nullable=False)


class SurveyDatabase(object):
    @staticmethod
    def construct_mysql_url(authority, port, database, username, password):
        return f'mysql+mysqlconnector://{username}:{password}@{authority}:{port}/{database}'

    @staticmethod
    def construct_in_memory_url():
        return 'sqlite:///'

    def __init__(self, url):
        self.engine = create_engine(url)
        self.Session = sessionmaker()  # pylint: disable=invalid-name
        self.Session.configure(bind=self.engine)

    def get_engine(self):
        return self.engine

    def ensure_tables_exist(self):
        Persisted.metadata.create_all(self.engine)

    def create_session(self):
        return self.Session()
