import yaml


class Config(object):
    def __init__(self, location: str):
        self.config_location = location
        loader = yaml.safe_load(open(location, 'rb').read())
        self.file_location = loader["file_location"]
