from pandas import DataFrame


def drop_col(df: DataFrame, key: str) -> DataFrame:
    """Drops the given column with name 'key' from the dataframe.

    Args:
        df (DataFrame): The dataframe.
        key (str): The given column name.

    Returns:
        DataFrame: dataframe without the column.
    """
    try:
        df = df.drop(key, axis=1)
    except KeyError as err:
        print(f"Key {key} not found in dump")
        print(err)

    return df


def chunker(seq: DataFrame, size: int) -> DataFrame:
    """Splits the given dataframe objects into a chunk of a given size.

    Args:
        seq (DataFrame): The given dataframe.
        size (int): The given size.

    Returns:
        DataFrame: The dataframe which has only 'size' amount of rows.
    """
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
