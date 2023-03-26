from c_code_parser.core.basic import *
from c_code_parser.utils.ut_tools import *


class TestBasicParser(BasicParser):
    def __init__(self):
        fp = "./data/example01.txt"
        super(TestBasicParser, self).__init__(fp)

        # ut_cases
        self.ut_cases = [
            self.test_get_parse_res_list_case_01,
            self.test_get_parse_res_list_case_02,
            self.test_get_parse_res_list_case_03,
            self.test_get_parse_res_list_case_04,
            self.test_get_char_pos_case_01,
            self.test_parse_define_case_01,
            self.test_parse_preprocessor_case_01,
            self.test_parse_parse_all_case_01,
        ]

    @UtClassTestTool()
    def test_get_parse_res_list_case_01(self):
        res = self.get_parse_res_list(RgxPattern.DEFINE)
        print(res)

    @UtClassTestTool()
    def test_get_parse_res_list_case_02(self):
        res = self.get_parse_res_list(RgxPattern.PREPROCESSOR)
        print(res)

    @UtClassTestTool()
    def test_get_parse_res_list_case_03(self):
        res = self.get_parse_res_list(RgxPattern.NOTE_TYPE_1)
        print(res)

    @UtClassTestTool()
    def test_get_parse_res_list_case_04(self):
        res = self.get_parse_res_list(RgxPattern.NOTE_TYPE_2)
        print(res)

    @UtClassTestTool()
    def test_get_char_pos_case_01(self):
        res = self.get_char_pos(35)
        print(res)

    @UtClassTestTool()
    def test_parse_define_case_01(self):
        test_txt = "#define ABC 123 \\ "
        res = self.parse_define(test_txt)
        print(res)

        test_txt = "#define ABC(x, y) 123"
        res = self.parse_define(test_txt)
        print(res)

    @UtClassTestTool()
    def test_parse_preprocessor_case_01(self):
        test_txt = "#include <stdlib>"
        res = self.parse_preprocessor(test_txt)
        print(res)

        test_txt = '#include "../core/file.h"'
        res = self.parse_preprocessor(test_txt)
        print(res)

        test_txt = '#ifdef ABC'
        res = self.parse_preprocessor(test_txt)
        print(res)

    @UtClassTestTool()
    def test_parse_parse_all_case_01(self):
        res = self.parse_all()
        print(res)
