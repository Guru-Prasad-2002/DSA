class Sample_Class:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")

obj=Sample_Class()
del obj