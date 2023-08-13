from threading import Lock, Thread


class SingletonClass:

    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance =super().__new__(cls)
            return cls._instance
        


if __name__ == "__main__":
    instance_in_thread1 = None

    def create_instance_thread1():
        global instance_in_thread1
        instance_in_thread1 = SingletonClass()

    # Start thread1 to create the instance
    thread1 = Thread(target=create_instance_thread1)
    thread1.start()
    thread1.join()

    # Create the instance in thread2
    instance_in_thread2 = SingletonClass()

    # Compare the instances
    if instance_in_thread1 is instance_in_thread2:
        print("The instance in thread1 is equal to the instance in thread2")
    else:
        print("The instance in thread1 is not equal to the instance in thread2")

    