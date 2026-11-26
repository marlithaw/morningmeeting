# Selects the week's Morning Meeting content file: MMWEEK=16 python3 build_mm.py (default 16).
import os as _os, importlib as _il
_m = _il.import_module('content_mm_w' + _os.environ.get('MMWEEK', '16'))
globals().update({k: v for k, v in vars(_m).items() if not k.startswith('__')})
