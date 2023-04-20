phrase = input("Set a phrase: ")
actual_sum = len(phrase)
expected_sum = 15
assert actual_sum < expected_sum, f"Phrase is more or equals to {expected_sum}"

#run test using command: python -m pytest -s ex10_short_phrase.py