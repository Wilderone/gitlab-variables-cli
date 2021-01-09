import configparser

config = configparser.ConfigParser()

c = config.read("./test.ini")
print(c)
