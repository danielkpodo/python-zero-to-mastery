# We name classes with capital letter
# We use CamelCalse
# class names have to be singular
# define the class
class BigObject:
    pass


# instantiate the class
obj1 = BigObject()


# __init__ is a special method called a dunder method or a magic method
# The init method is called anytime we instantiate our class
# In some languages, like js, think of it as a constructor
# self always refer to the classname, so that when it is instantiated all attributes are available to it
# we can also access attr directly from our class using classname.anything -> this accesses our variables
# self needs to pass to all our methods so as to make the attributes directly available to them
