"""
In the provided code below, the `__call__` magic method is defined in the `SingletonMeta` metaclass. 
The purpose of this `__call__` method in the metaclass is to control the instantiation of classes that use this metaclass,
enforcing the Singleton pattern. The code ensures that there is only one instance of each class created using this metaclass.
In the `Singleton` class, you don't directly invoke the instance as a function (i.e., `s1()` or `s2()`), 
which would trigger the `__call__` method. Instead, the `__call__` method in the metaclass is called implicitly when 
you create an instance of `Singleton` using the regular class instantiation syntax (`s1 = Singleton()`).

Here's a breakdown of what happens in the code:
1. `Singleton` is defined with the metaclass `SingletonMeta`, so the `SingletonMeta` metaclass controls 
the instantiation behavior of the `Singleton` class.

2. When you create the first instance `s1 = Singleton()`, it triggers the `__call__` method in the `SingletonMeta` 
metaclass because the metaclass controls the behavior of class instantiation.

3. The `__call__` method in the metaclass checks if an instance of the `Singleton` 
class already exists in the `_instances` dictionary. Since there's no existing instance, a new instance 
is created using `super().__call__(*args, **kwargs)`. This instance is then stored in the `_instances` dictionary.

4. The same instance is returned for subsequent calls to create an instance of the `Singleton` class,
which ensures the Singleton pattern is maintained.
In the provided code, the `__call__` method is called in the metaclass during class instantiation,
not because you explicitly invoked the instance as a function. The metaclass's `__call__` method allows you 
to customize the behavior of class instantiation and enforce the Singleton pattern without the need for 
explicitly calling the instance as a function. 
"""

from typing import Any


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:

        if not cls in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    pass


if __name__ == "__main__":
    s1 = Singleton()
    setattr(s1, "val", 20)
    s2 = Singleton()
    print(f"s2 val: {s2.val}")