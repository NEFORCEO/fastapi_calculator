from pydantic import BaseModel
from calculator.caclulator import Calculator

class Param(BaseModel):
    num1: int 
    num2: int 
    oper: Calculator