#test file to be used by pytest
import pytest
from my_package import MyClass

def test_class():
	assert MyClass(value="Endris").attribute =="Endris"