import pytest


class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)



def test_generic():                        ## The test case name should always start with test_ or else it won't execute.
    a=100
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange

def test_example():
    a=20
    b=20
    assert a==b