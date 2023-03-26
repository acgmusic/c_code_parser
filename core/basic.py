# 用于解析基本信息
from c_code_parser.utils.log import logger
from enum import Enum
import re
from c_code_parser.core.re_tool import ReTool


class RgxPattern(Enum):
    DEFINE = r"#define([^\\\n]*?\\\s*?\n)*.*"
    PREPROCESSOR = r"#(include|undef|ifdef|ifndef|if|elif|else|endif|line|error|warning|region|endregion).*"
    NOTE_TYPE_1 = r"/\*(([^\*].*?\**([^/]|$).*)*?\n)*?.*?\*/"
    NOTE_TYPE_2 = r"//.*"


class BasicParser:
    def __init__(self, text):
        self.text = text
        self.text_split = self.text.split("\n")
        self.char_num_list = [len(line)+1 for line in self.text_split]

    # 获取第n个字符，在第几行第几个字符
    def get_char_pos(self, n):
        row = 0
        while n >= self.char_num_list[row]:
            n -= self.char_num_list[row]
            row += 1
            if row >= len(self.char_num_list):
                logger.error("%d is out of range, cannot find position" % (n, ))
                return -1, -1
        return row, n

    def get_parse_res_iter(self, ptn):
        if not isinstance(ptn, RgxPattern):
            raise ValueError(f"not a valid pattern: {str(ptn)}")
        for search_res in re.finditer(ptn.value, self.text):
            yield search_res

    def get_parse_res_list(self, ptn):
        return list(self.get_parse_res_iter(ptn))

    # 解析define信息
    @staticmethod
    def parse_define(txt):
        txt_used = txt.split("\n")[0]
        txt_used = ReTool.remove_end_slash(txt_used)
        txt_used = ReTool.remove_space(txt_used, flag=4)
        search_res = re.search(r"#define\s+\w+", txt_used)
        if search_res is None:
            logger.error("this is not a define code line: %s" % (txt, ))
            return None
        right_pos = search_res.span()[1]
        name_re = re.search(r"(?<=\s)\w+$", txt_used[:right_pos])
        if name_re is None:
            logger.error("this is not a define code line: %s" % (txt, ))
            return None
        name = name_re.group()
        value = ReTool.remove_space(txt_used[right_pos:], flag=4).split(" ")[-1]
        if not value:
            logger.error("this is not a define code line: %s" % (txt, ))
            return None
        info = {'name': name, 'args': [], 'value': value, 'full_text': txt}
        # 如果是宏定义函数
        if len(txt_used) > right_pos and txt_used[right_pos] == '(':
            args_info_re = re.search(r".*?(?=\))", txt_used[right_pos+1:])
            if args_info_re is None:
                logger.error("bracket is not match in first line: %s" % (txt, ))
            info['args'] = ReTool.remove_space(args_info_re.group(), flag=3).split(',')
        return info

    # 解析预编译指令信息
    @staticmethod
    def parse_preprocessor(txt):
        txt = ReTool.remove_space(txt, flag=4)
        if not txt or txt[0] != "#":
            logger.error("invalid preprocessor: %s" % (txt, ))
            return None
        # 只需解析include
        if re.search(r"#include", txt) is None:


    # 将基础代码分离，并返回基础代码的信息
    def parse_all(self):
        parse_res = {}
        for ptn in RgxPattern:
            for search_res in self.get_parse_res_iter(ptn):
                info = {

                }


if __name__ == '__main__':
    pass

