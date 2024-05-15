try:
    func()
except ValueError as exc:
    print("ValueError")
except TypeError as exc:
    print("TypeError")
except SystemError as exc:
    print("SystemError")
else:
    print("No Exceptions")
