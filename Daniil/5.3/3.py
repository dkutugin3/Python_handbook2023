class A:
    def __repr__(self) -> str:
        raise Exception


func(A())
