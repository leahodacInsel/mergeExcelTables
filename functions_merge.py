from pathlib import Path
from glob import glob
import datetime


def write_excel(df, path, fileName):
    output_name = Path(fileName + '.xlsx')
    i = glob(path + "\\" + output_name.stem + "_[0-9]*" + output_name.suffix)
    new_output_name = f"{output_name.stem}_{len(i)+1}{output_name.suffix}"
    df.to_excel((path + '\\' + new_output_name), index=False)


def strip_df(df):
    # remove all whitespaces at beginning or end of string in the entire df
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df


def datetime2date(df):
    # transform all the datetime of a table into date --> watch out if important time information, apply only on selected columns
    df = df.applymap(lambda x: x.date() if isinstance(x, datetime.datetime) else x)
    return df