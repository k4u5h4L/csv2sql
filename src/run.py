import pandas as pd
import os

from .generate import generate
from .utils import drop_col, chunker
from .config import config


def run() -> None:
    """Runs the CSV2SQL generator function.
    """

    print("Starting CSV to SQL dump...")

    for conf in config:
        table_name = conf.get('table_name')

        df = pd.read_csv(f'./data/{table_name}.csv')

        # skip columns which are auto generated
        for ignore_column_name in conf.get('ignore_columns'):
            df = drop_col(df, ignore_column_name)

        final_sql = ""

        for df_chunk in chunker(df, 10):
            final_sql += "\n" + \
                generate(df_chunk, table_name, conf.get('substitute_column'))

        path = './out'
        file_name = f'{path}/{table_name}.sql'

        if not os.path.exists(path):
            print(f"Creating new path: {path}")
            os.makedirs(path)

        with open(file_name, "w") as file:
            file.write(final_sql)

        print(f'Saved SQL file of table {table_name} to {file_name}\n\n')
