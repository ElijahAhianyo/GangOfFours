"""
This code defines a `SingletonClass` that implements the Singleton pattern using the `__new__` method. 
The Singleton pattern ensures that there's only one instance of a class, and subsequent calls to create
instances return the same instance. Here's an explanation of the code step by step:

1. `SingletonClass` is defined with a class attribute `_instance` initialized to `None`. 
This attribute will hold the single instance of the class.

2. The `__new__` method is overridden in the `SingletonClass`. This method is responsible for 
creating new instances of the class. However, in this case, it's modified to ensure that only one instance is created and returned.

3. Inside the `__new__` method:
   - It checks if the `_instance` attribute of the class (`cls`) is `None`. If it's `None`, it means no instance has been created yet.
   - If no instance exists, it creates a new instance using `super().__new__(cls)`. 
   This line creates the instance without invoking the `__init__` method, which is typical for a Singleton.
   - It then sets an attribute `val` on the class (`cls`) with the initial value of 0. 
   This is done to demonstrate that changes to this attribute persist across all instances since there's only one instance.
   - Finally, it sets the `_instance` attribute of the class (`cls`) to the newly created instance.

4. The code in the `__main__` block demonstrates the behavior of the `SingletonClass`:
   - It creates the first object `first_object` using `SingletonClass()`. Since it's the first instance, 
   the `__new__` method is called, and the `val` attribute is set to 0. The reference to this instance is stored in `_instance`.
   - It prints the value of `first_object.val`, which is 0.
   - It sets the `val` attribute of `first_object` to 40.
   - It creates a second object `second_object` using `SingletonClass()`. Since an instance already exists, 
   the `__new__` method is not called again. Instead, the existing instance (created during the creation of `first_object`) is returned.
   - It prints the value of `second_object.val`, which is also 40 because both `first_object` and `second_object` 
   refer to the same instance, and the changes made to the `val` attribute are shared between them.

In summary, this code demonstrates a simple implementation of the Singleton pattern using the `__new__` method, 
where only one instance of `SingletonClass` is created, and any changes made to shared attributes are visible across all instances.
"""



class SingletonClass:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance =super().__new__(cls)
            setattr(cls, "val", 0)
            
        return cls._instance



if __name__ == "__main__":
    first_object = SingletonClass()
    print(f"val: {first_object.val}")
    first_object.val = 40
    second_object = SingletonClass()
    print(f"val: {second_object.val}")
            