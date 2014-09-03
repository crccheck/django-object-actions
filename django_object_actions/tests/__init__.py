# HACK to get factoryboy logging to shut up
import logging
logging.getLogger("factory").setLevel(logging.WARN)

# DJANGO 1.4 DJANGO 1.5
from .test_utils import *
from .tests import *
