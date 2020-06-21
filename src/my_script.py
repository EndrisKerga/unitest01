# importing the my_package.utils if the my_package is not imported in __inii__.py 
'''import my_package.utils

my_package.utils.we_need_to_talk(break_up=True)'''

# importing the my_package directly if the my_package is already imported in __inii__.py 
import my_package

my_package.we_need_to_talk(break_up=True)

# MyClass is instantialed here from my_class.py package 

my_instance = my_package.MyClass(value='I love you Endris')
print(my_instance.attribute)