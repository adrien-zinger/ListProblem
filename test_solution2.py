import pytest

def test_zip_trick():
    h = ['123', '456', '789']
    v = [''.join(x) for x in zip(*h)] # *h will create three lists that we can zip
    assert v == ['147', '258', '369']