'''Running teh Xetra ETL application'''

import logging
import logging.config
import yaml 


def main():
    '''Entry point to Xetra ETL job'''
    #Parsing YAML file 
    config_path = 'C:/Users/patri/Desktop/Udemy/Data Engineer/dataengineer_training/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))  
    #configure logging 
    log_config = config['logging']
    logging.config.dictConfig(log_config) 
    logger = logging.getLogger(__name__)
    logger.info('this is a test')


if __name__ == '__main__':
    main()