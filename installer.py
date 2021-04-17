from datetime import datetime
from sys import stderr
import pandas as pd
from numpy import genfromtxt
from sqlalchemy import create_engine, engine
from sqlalchemy.exc import SQLAlchemyError

from database import Survey, SurveyDatabase


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


def add_starter_data(session):
    with open("survey.csv", 'r') as file:
        data_df = pd.read_csv(file)
    data_df.to_sql('survey', con=session, index=True, index_label='id', if_exists='replace')


def main():
    try:
        url = SurveyDatabase.construct_mysql_url('localhost', 3306, 'surveys', 'root', 'cse1208')
        manufacturer_database = SurveyDatabase(url)

        manufacturer_database.ensure_tables_exist()
        print('Tables created.')
        session = manufacturer_database.get_engine()

        add_starter_data(session)
        print('Records created.')
    except SQLAlchemyError as exception:
        print('Database setup failed!', file=stderr)
        print(f'Cause: {exception}', file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
