# https://omkarpathak.in/2018/04/11/python-getitem-and-setitem/
# TODO: please can we implement the error handling advised in the documentation?
# https://docs.python.org/3/reference/datamodel.html#object.__getitem__

class CustomList(object):
    def __init__(self, elements=0):
        self.my_custom_list = [0] * elements
    
    def __setitem__(self, index, value):
        self.my_custom_list[index] = value
    
    def __getitem__(self, index):
        return "The {} element has value {}".format(index, self.my_custom_list[index])

    def __str__(self):
        return str(self.my_custom_list)

    def __delitem__(self, index):
        del self.my_custom_list[index]

my_list = CustomList(5)
my_list[0] = 1
my_list[1] = 2
print(my_list[0])
print(my_list)
del my_list[1]
print(my_list)

    