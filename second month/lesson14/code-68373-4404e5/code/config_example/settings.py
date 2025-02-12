import configparser
# import argparse
# import pathlib

config = configparser.ConfigParser()
config.read(['config.ini', 'config-dev.ini'])
# config.read(['config.ini', 'config-prod.ini'])
print(config.sections())

for section in config.sections():
    print(section)
    for k, v in config[section].items():
        print(k, v, type(v))

# class Settings:
#     def __init__(self):
#         self.port = ....
