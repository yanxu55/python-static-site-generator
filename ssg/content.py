import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = __class__.__regex.split(string, 2)
        fm = load(fm, Loader=FullLoader)
        return cls(fm, content)
    
    