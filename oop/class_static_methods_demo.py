class Calculator:
    """
    A class demonstrating the differences between static methods and class methods.
    """
    # 1. Class Attribute: Accessible by the class method via the 'cls' parameter
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static Method: Performs addition. 
        It does not need access to the class (cls) or the instance (self).
        It's essentially a regular function logically grouped within the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class Method: Performs multiplication. 
        It takes the class itself (cls) as the first argument, allowing it 
        to access and display the class attribute 'calculation_type'.
        """
        # Accessing the class attribute via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b