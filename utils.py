from pygris import states
from pygris.utils import shift_geometry
import pandas as pd

def check_completeness(df:pd.DataFrame)-> None:
    if df.isnull().values.any():
        print('DataFrame misses values...!')
    else:
        print('DataFrame is complete!')

def count_in_year(names_df:pd.DataFrame,year:int,rename_count=False) -> pd.DataFrame:
    #Returns name dataframe filtered by year
    columns=['Name','Count']
    if 'State' in names_df.keys():
        columns.append('State')
    df = names_df[names_df['Year']==year][columns]
    return df.rename(columns={'Count':f'Count_{year}'}) if rename_count else df

def pretty_us_df() -> pd.DataFrame:
    #Returns dataframe with prepared data for pretty plot of US map
    return shift_geometry(states(cb = True, resolution = "20m"))

def top_names_map(top_names:pd.DataFrame) -> pd.DataFrame:
    #Enriches given dataframe with data for pretty plot of US map
    top_names.rename(columns={'State':'STUSPS','Name':'PopName'},inplace=True)
    return pretty_us_df().merge(top_names,on='STUSPS')