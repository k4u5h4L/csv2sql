import re
from pandas import DataFrame


def generate(df: DataFrame, table_name: str, rules: dict) -> str:
    sql = f"INSERT INTO {table_name}"
    reg = re.compile(r'(nan|NULL|null)')

    sql += f" ({', '.join(df.columns)}) "
    sql += "VALUES"

    for index, row in df.iterrows():
        r = []
        for col in df.columns:

            # traverse through rules to substitute values
            continue_loop = False
            for key, value in rules.items():
                if col == key and str(row[col]) == value.get('from'):
                    r.append(value.get('to'))
                    continue_loop = True
                    break

            if continue_loop:
                continue

            val = row[col] if not reg.match(str(row[col])) else ""

            if isinstance(val, str):
                r.append(repr(val))
            elif isinstance(val, float):
                if val == int(val):
                    r.append(str(int(val)))
                else:
                    r.append(str(val))
            else:
                r.append(str(repr(val)))

        sql += f" ({', '.join(r)}) "
        sql += ", "

    sql = sql[:-3]
    sql += ";"
    return sql
