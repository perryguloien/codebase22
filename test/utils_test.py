# directory must be called test
# each file must begin or end with test i.e. test_utils.py or utils_test.py

# this is the "tests/utils_test.py" file...



from app.utils import to_usd


# def test_answer():
    # assert inc(3) == 5



def test_to_usd():
    # it rounds to two decimal places and have dollar sign :
    assert to_usd(0.45555) == "$0.46"

    # if large numbers, should use comma separator:
    assert to_usd(123456789.98) == "$123,456,789.98"
