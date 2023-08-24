import pandas as pd
import pymysql

def get_data_from_mysql(stock_id, page=1, per_page=10):
    # MySQL connection settings
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="0505",
        database="database1",
    )


    # Logic to get data
    offset = (page - 1) * per_page
    query = f"SELECT * FROM final_news_data WHERE stock_id = {stock_id} LIMIT {per_page} OFFSET {offset}"
    df = pd.read_sql(query, connection)
   

    connection.close()

    return df

