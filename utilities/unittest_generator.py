"""
Module to generate unit tests.
"""
class UnitTestGenerator():
    """
    A class to generate unit tests for a given unittest class name.
    """
    def __init__(self, unittest_class_name: str):
        """
        Initialize the UnitTestGenerator with a unittest class name.

        Args:
        unittest_class_name (str): The name of the unittest class.
        """
        self.unittest_class_name = unittest_class_name

    def _format_unit_test(self, test_case: str) -> str:
        """
        Format a single unit test case.

        Args:
        test_case (str): The test case string.

        Returns:
        strL The formatted test case.
        """
        test_case = test_case.replace("\n", "").replace("test.assert_equals", "  self.assertEqual")
        return test_case

    def _wrap_in_test_function(self, input_string: str, function_name: str) -> str:
        """
        Wrap a test case string in a test function.

        Args:
        input_string (str): The test case string.
        function_name (str): The name of the test function.

        Returns:
        str: The test function string.
        """
        function_template = f"    def {function_name}(self):\n      {input_string}"
        return function_template


    def generate_unit_tests(self) -> str:
        """
        Generate unit tests from a file.

        Returns:
        str: The generated unit tests.
        """
        test_cases = []
        with open("./utilities/codewars_tests.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            test_cases.append(f"class {self.unittest_class_name}(unittest.TestCase):")

            for i, line in enumerate(lines):
                line = self._format_unit_test(line)
                test_case = self._wrap_in_test_function(line, f"test_case_{i+1}")
                test_cases.append(test_case)

            test_cases.append('if __name__ == "__main__":\n    unittest.main()')
            result = "\n\n".join(test_cases)
            return result

    def output_unit_tests(self, unit_tests: str) -> None:
        """
        Output the generated unit tests to a file.

        Args:
        unit_tests (str): The generated unit tests.
        """
        with open("./output/unittests.txt", "w", encoding="utf-8") as f:
            f.write(unit_tests)

# Example usage
tests = UnitTestGenerator("TestRemoveNthElement")
unittests = tests.generate_unit_tests()
tests.output_unit_tests(unittests)