# test_with_pytest.py

def test_always_passes():
    assert True

# def test_always_fails():
#     assert False

def test_help():
    from toolbox.src.tasks import help
    help(None)