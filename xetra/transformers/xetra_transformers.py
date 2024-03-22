from typing import NamedTuple

from xetra.common.s3 import S3BucketConnector


class XetraSourceConfig(NamedTuple):
    '''
    Class for Source configuration data 

    src_first_extract_date: determines the date for extracting the source 
    src_columns: source column names 
    src_col_date: column name for date in source 
    src_col_isin: column name for isin in source
    src_col_time: column name for time in source 
    src_col_start_price: column name for strating price  in source
    src_col_min_price: column name for minimum price in source
    src_col_max_price: column name for maximum price in source
    src_col_traded_vol: column name for traded volume in source
    '''
    src_first_extract_date:str
    src_columns: list
    src_col_date:str
    src_col_isin:str
    src_col_time:str
    src_col_start_price:str
    src_col_min_price:str
    src_col_max_price:str
    src_col_traded_vol:str