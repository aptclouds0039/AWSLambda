from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
import json

user = 'sql12664669'
password = 'X6xTDuwSmr'
host = 'sql12.freesqldatabase.com'
database = 'sql12664669'

connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string, poolclass=QueuePool, pool_size=5, max_overflow=10)

def lambda_handler(event, context):
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM Destinations"))
            allresults = result.mappings().all();
            finalResults = [dict(row) for row in allresults]
            return {
                'statusCode': 200,
                'body': finalResults
            }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
