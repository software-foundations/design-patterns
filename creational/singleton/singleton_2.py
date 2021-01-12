"""
Solve the innit have been executed whenever AppSettings() "instantiate",
even when the object already exists
"""

def singleton(the_class):
    # {the_class: the_class(*args, **kwargs)}
    instances = {} # storage the object

    def get_class(*args, **kwargs):
        print('instances: ', instances)
        if the_class not in instances: # check exists a key of the class in the dictionary
            instances[the_class] = the_class(*args, **kwargs) # instantiate
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        """
        Executed only when instantiate the class
        """
        print('executing __init__ of the AppSettings class')
        self.tema = 'O tema escuro'
        self.font = '18px'


@singleton
class Test:
    def __init__(self) -> None:
        print('executing __init__ of the Test class')
        pass


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)

    t1 = Test()
    t2 = Test()
    print(t1 == t2)
