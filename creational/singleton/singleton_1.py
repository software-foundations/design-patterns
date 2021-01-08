class AppSettings(object):
# class AppSettings:
    """
    object can be ommited
    """
    _instance = None

    # https://www.concentricsky.com/articles/detail/pythons-hidden-new#:~:text=Controlling%20New%20with%20__new,__new__%20magic%20method.&text=__new__%20takes%20a,super(NewedClass%2C%20cls)
    # __new__ takes a class instead of an instance as the first argument.
    # Since it creates an instance, that makes sense.
    # super(NewedClass, cls).__new__(cls) is very important.
    # We don't want to call object.__new__ directly; again, you'll see why later.
    # Why is from_base_class defined in __new__ instead of __init__? It's metadata about object creation, which makes more semantic sense in __new__. However, if you really wanted to, you could place define _from_base_class
    def __new__(cls, *args, **kwargs):

        # None      -> False
        # not None  -> True 
        if not cls._instance:
            # this super() acces the __new__ from the object class            
            # *args     -> sequence of args with underfined names storage in arg parameter
            # **kwargs  -> sequence of keyword args (like dictionaries) storage in kwargs parameter
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self) -> None:
        """ The init method will be called whenever instantiate
        the class, even when the object have already been made """
        self.theme = 'Dark theme'
        self.font = '18px'


if __name__ == "__main__":

    as1 = AppSettings()         # as1 instantiate the class
    as1.theme = 'Bright theme'  # create the theme attribute
    print(as1.theme)            # checking the theme attribute

    as2 = AppSettings()         # as2 receive the memmory position of as1, but AppSettings() runs the __ini__method and override the theme variable from 'Bright theme' to 'Dark theme'
    print(as1.theme)            # checking the theme attribute

    # checking if is the same object
    print('is the same object')
    print(as1)
    print(as2)
    print(as1 == as2)
    print(id(as1) == id(as2)) # checking the memory position