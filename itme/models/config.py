import tomli


class Config:
    """
    Configurations for the application
    """

    def __init__(self, filename):
        """
        Initialize the configurations
        """
        self.filename = filename
        self.config = tomli.loads(open(filename).read())

    def get(self, key):
        """
        Get a configuration value
        """
        return self.config.get(key)
