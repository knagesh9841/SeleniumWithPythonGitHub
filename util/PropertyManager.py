import os

from jproperties import Properties

from util import Logger

path = os.getcwd()

projectroot = os.path.dirname(path)

path = projectroot+"\\resources\config\configuration.properties"


def getconfigdata(propertyname):
    log = Logger.getlogger()
    try:
        configs = Properties()
        with open(path, 'rb') as config_file:
            configs.load(config_file)

        return configs.get(propertyname).data
    except Exception as e:
        log.exception("Exception Occurred", exc_info=True)
