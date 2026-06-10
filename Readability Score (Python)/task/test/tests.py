from typing import List, Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TestStage1(StageTest):

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin="This text is simple to read!"),
            TestCase(stdin="This text is hard to read. "
                           "It contains a lot of sentences as well as a lot of words in each sentence."),
            TestCase(stdin="1" * 99),
            TestCase(stdin=" " * 100),
            TestCase(stdin="q" * 101),
            TestCase(stdin="This! text! is! hard to read.")
        ]

        for test in list_tests:
            test.attach = test.input

        return list_tests

    def solve(self, att):
        if len(att) > 100 or len(att.split("!")) > 3:
            return "Difficulty: HARD"
        else:
            return "Difficulty: EASY"

    def check(self, reply: str, attach) -> CheckResult:
        if self.solve(attach).lower() not in reply.strip().lower():
            return CheckResult.wrong(f"Incorrect or empty output. "
                                     f"The output of your program for this text should be \"{self.solve(attach)}\".")
        return CheckResult.correct()


if __name__ == '__main__':
    TestStage1("readability.readability").run_tests()
