import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def checker(func):
    def new_func(a, b):
        if not isinstance(a,str):
            return "File name is not string."
        if not a:
            return "File name is empty."
        if not b:
            return "Writing contents are empty."
        return func(a, b)
    return new_func

@checker
def writingparquetfile(filename,content):
    try:
        df = pd.DataFrame(content)
        table = pa.Table.from_pandas(df)
        try:
            pq.write_table(table, filename)
            return df
        except:
            return "File name error"
    except:
        return "DataFrame constructor not properly called!"
    
