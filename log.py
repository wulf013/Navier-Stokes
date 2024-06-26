#written by Enrique Castro
#boiler plate for accessing the logging format yaml file
'''
Just a simple log module that reads the YAML configuration file, nothing fancy here.
'''

#when building this up, the configuration in the yaml files asks that you
#have a folder in the same directory as the code, named 'logs'. Make sure the 'log' files have the ending of '.log' instead of '.txt'. 
#the system will recognize the directory and populate log messages there

import yaml
import logging
import logging.config

class console(logging.Filter): #this just controls some aspects of the log messagess as they are given to the log handlers
    def filter(self, record):
        if(record.name == '__main__'): #check to see if the log record is coming from main
            return record
        elif(record.levelname == 'ERROR' or record.levelname == 'CRITICAL'): #only allow critical & Error messages out to console should they arise
            return record    
        else: #if not coming from main, or critical level, then don't show in console. 
            return not record #this log will sitll populate to the log files, just not the console.

def setup_logging(default_path = 'log.yaml', default_level = logging.INFO):
    path = default_path
    with open(path, 'rt') as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception as e:
            print(e)
            print('Error in Logging Configuration. Using default configs')
            logging.basicConfig(level=default_level)