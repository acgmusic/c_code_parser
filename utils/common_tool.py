import re
import json


class CmTool:
    @classmethod
    def pretty_print_dict(cls, dic, indent=4):
        print(json.dumps(dic, indent=indent))
