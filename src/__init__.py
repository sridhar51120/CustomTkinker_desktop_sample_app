import json

def get_config(key):
    config_file = 'G:/GITHUB/GUI/config.json'
    with open(config_file, 'r') as file:
        config = json.loads(file.read())

    if key in config:
        return config[key]
    else:
        raise Exception("Key {} not found in config.json".format(key))
