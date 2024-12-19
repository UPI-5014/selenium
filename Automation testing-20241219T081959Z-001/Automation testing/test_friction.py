import pytest
@pytest.fixture
def fixturemethod():
 print("This is a fixture Method")

 def test_methodA():
     print("This is method A")

 def test_methodB(fixturemethod):
     print("This is method B")
     def test_methodC(fixturemethod):
         print("This is method c")
         def test_methodD(fixturemethod):
             print("This is method d")
