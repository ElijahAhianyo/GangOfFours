
class SingletonClass:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            setattr(cls, "val", 0)
            
        return cls._instance



if __name__ == "__main__":
    first_object = SingletonClass()
    print(f"val: {first_object.val}")
    first_object.val = 40
    second_object = SingletonClass()
    print(f"val: {second_object.val}")
            