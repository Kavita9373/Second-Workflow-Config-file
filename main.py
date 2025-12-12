# Import the module
from configparser import ConfigParser
import sys

# File path
try:
    file = sys.argv[1]
except:
    file = "config.ini"
    
# Creating object
config = ConfigParser()

# Read config file
config.read(file)


def read_values(config):
    for section in config.sections():
        print(f"--------{section}--------:")
        for key, value in config[section].items():
            print(f"{key} : {value}")

read_values(config)
