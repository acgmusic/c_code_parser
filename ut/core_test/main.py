from c_code_parser.ut.core_test.basic_test import TestBasicParser


test_class_list = [
    TestBasicParser,
]


def run_all_class_cases(class_list):
    for cls in class_list:
        cls_inst = cls()
        for func in cls_inst.ut_cases:
            func()


if __name__ == '__main__':
    run_all_class_cases(test_class_list)
