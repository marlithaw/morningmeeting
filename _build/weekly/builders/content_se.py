# Selects the matching Spark/Ember content file (Spark/Ember week = Morning Meeting week - 8).
import os as _os, importlib as _il
_m = _il.import_module('content_se_w' + str(int(_os.environ.get('MMWEEK', '16')) - 8))
globals().update({k: v for k, v in vars(_m).items() if not k.startswith('__')})
