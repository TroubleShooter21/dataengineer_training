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


class XetraTargetConfig(NamedTuple):
    '''
    Class for Target  configuration 


    '''
    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_clos_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_dail_trad_vol:str
    trg_col_ch_prev_clos:str
    trg_key:str
    trg_key_date_format:str
    trg_format:str


class XetraETL():
    '''
    reads the Xetra data, transforms and writes tranformed to target '''
    def __init__(self, s3_bucket_src: S3BucketConnector, s3_bucket_trg:S3BucketConnector, meta_key:str ,src_args: XetraSourceConfig, trg_args: XetraTargetConfig) -> None:
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg= s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date = 
        self.extract_date_list = 
        self.meta_update_list = 

    def extract(self):
        pass

    def tranform_report1(self):
        pass
    
    def load(self):
        pass

    def etl_report1(self):
        pass
