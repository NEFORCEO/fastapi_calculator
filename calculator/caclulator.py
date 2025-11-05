from enum import StrEnum


class Calculator(StrEnum):
    Addition: str = "+"
    Subtraction: str = "-"
    Multiplication: str = "*"
    Division: str = "/"
    Int_division: str = "//"
    Modulus: str = "%"
    Exponentiation: str = "**"