import openpyxl
import pytest

class ExcelTestSelector:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_selected_tests(self):
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active
        selected_tests = []

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
            test_name, execute_flag = row
            if execute_flag and execute_flag.strip().upper() == "Y":
                selected_tests.append(test_name.strip())

        return selected_tests


if __name__ == "__main__":
    selector = ExcelTestSelector("TestExecutor.xlsx")  # put your file path
    tests_to_run = selector.get_selected_tests()

    for test_case in tests_to_run:
        # ✅ Run test with exact match only
        pytest.main([f"-k ^{test_case}$"])
