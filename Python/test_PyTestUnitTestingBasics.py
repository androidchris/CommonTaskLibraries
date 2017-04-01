# Unit testing w/ pytest example:
# Run python3 -m pytest in directory of this file to test.

# Create function to add 1 to number passed in:
def func(x):
    return x + 1

def test_answer():
    # This test should pass:
    assert func(3) == 4

    # 7 + 1 is 8 so this test should fail.
    assert func(7) == 7



