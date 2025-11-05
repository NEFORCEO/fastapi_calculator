from fastapi import APIRouter, HTTPException

from calculator.caclulator import Calculator
from schemas.calc_schema import ReturnCalculator
from schemas.param_cacluclator import Param

multi = APIRouter(
    prefix="/calc",
    tags=["Сложение/Вычитание"]
)

@multi.post("/plus", response_model=ReturnCalculator)
async def plus_func(param: Param):
    if param.oper == Calculator.Addition:
        result = param.num1 + param.num2 
        return {
            "status": 200,
            "result": result
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Нужно использовать операцию +"
        )
        
@multi.post("/subtraction", response_model=ReturnCalculator)
async def subtraction(param: Param):
    if param.oper == Calculator.Subtraction:
        result = param.num1 - param.num2
        return {
            "status": 200,
            "result": result
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Неверная операция используйте -"
        )
    
@multi.post("/division", response_model=ReturnCalculator)
async def division(param: Param):
    if param.oper == Calculator.Division:
        if param.num2 != 0:
            return {
                "status": 200,
                "result": param.num1 / param.num2
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="На ноль делить нельзя"
            )
    else:
        raise HTTPException(
            status_code=400,
            detail="Нужно выбрать операцию /"
        )