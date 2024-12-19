import pytest
@pytest.fixture()
def loginapplication():
    print("This is login Application")
    def searching_product():
        print("searching the product")
        def add_to_the_cart():
            print("this is login application")