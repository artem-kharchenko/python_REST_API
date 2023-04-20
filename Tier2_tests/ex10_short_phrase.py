class ShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        actual_sum = len(phrase)
        expected_sum = 15
        assert actual_sum < expected_sum, f"Phrase is more than {expected_sum}"

#run test using command: python -m pytest -s ex10_short_phrase.py