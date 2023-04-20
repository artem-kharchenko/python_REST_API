class TestExample:
    def test_check_math(self):
        a = 8
        b = 2
        expected_sum = 10
        assert a + b == expected_sum, f"Sum of variables a and b is not equals to {expected_sum}"