from sqlalchemy import create_engine, text
# Testing Branch
user = 'sql12664669'
password = 'X6xTDuwSmr'
host = 'sql12.freesqldatabase.com'
database = 'sql12664669'
# Create an SQLAlchemy engine and start a transaction
connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)
connection = engine.connect()
transaction = connection.begin()



def lambda_handler(event, context):
    try:
        result = connection.execute(text("SELECT * FROM Destinations"))
        print(result);
        for row in result:
            print(row)
        transaction.commit();
        return result;
    except Exception as e:
        print(e);
        transaction.rollback()  # Roll back the transaction if an exception occurs
    finally:
        connection.close()
