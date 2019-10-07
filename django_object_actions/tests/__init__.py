# HACK to get factoryboy logging to shut up
import logging

logging.getLogger("factory").setLevel(logging.WARN)
