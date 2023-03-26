# 用于处理字符串
from c_code_parser.utils.log import logger
from enum import Enum
import re


class ReTool:
    @classmethod
    def remove_space(cls, text_line, flag=0):
        # 去除行首、尾空格
        if flag == 0:
            res = re.sub(r"^\s*", "", text_line)
            res = re.sub(r"\s*$", "", res)
            return res
        # 去除行首
        if flag == 1:
            res = re.sub(r"^\s*", "", text_line)
            return res
        # 去除行尾
        if flag == 2:
            res = re.sub(r"\s*$", "", text_line)
            return res
        # 去除所有空格
        if flag == 3:
            res = re.sub(r"\s", "", text_line)
            return res
        # 去除行首、尾，去除中间多余的空格
        if flag == 4:
            res = re.sub(r"^\s*", "", text_line)
            res = re.sub(r"\s*$", "", res)
            res = re.sub(r"\s+", " ", res)
            return res

    # 去除define语句末尾的'\'
    @classmethod
    def remove_end_slash(cls, text_line):
        res = cls.remove_space(text_line, flag=2)
        if res[-1:] == "\\":
            res = res[:-1]
        res = cls.remove_space(res, flag=2)
        return res

    # 获取第一个空格后面的内容
    @classmethod
    def get_content_after_first_space(cls, text_line):
        assert " " in text_line, "find no space in %s" % (text_line, )
        return re.search(r"(?<=\s)(\S|$).*", text_line).group()
