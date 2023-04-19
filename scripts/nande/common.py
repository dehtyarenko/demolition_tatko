import configparser

# methods defintion
def load_properties_files(*files):
    config = configparser.ConfigParser()

    for file in files:
        with open(file, 'r') as f:
            content = '[default]\n' + f.read()
        config.read_string(content)


    properties = {}
    for section in config.sections():
        for key, value in config.items(section):
            properties[key] = value

    return properties
