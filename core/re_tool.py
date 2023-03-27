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

    # 判断字符串开头，是否在目标列表中
    @classmethod
    def is_prefixed_with(cls, text_line, prefix_lit):
        if type(prefix_lit) is not list:
            prefix_lit = [prefix_lit]
        for pref in prefix_lit:
            if text_line[:len(pref)] == pref:
                return True
        return False

    # 输入pos_start, pos_end，将对应区间内的文本全部换为空格
    @classmethod
    def reset_txt_btw_pos_range(cls, text, pos_start, pos_end):
        text_split = text.split("\n")
        if pos_start[0] == pos_end[0]:
            tmp = text_split[pos_start[0]]
            text_split[pos_start[0]] = tmp[:pos_start[1]] + " " * (pos_end[1] - pos_start[1]) + tmp[pos_end[1]:]
        else:
            for row in range(pos_start[0], pos_end[0]+1):
                tmp = text_split[row]
                if row == pos_start[0]:
                    text_split[row] = tmp[:pos_start[1]] + " " * (len(text_split[row]) - pos_start[1])
                elif row == pos_end[0]:
                    text_split[row] = " " * pos_end[1] + tmp[pos_end[1]:]
                else:
                    text_split[row] = " " * len(text_split[row])
        return "\n".join(text_split)


