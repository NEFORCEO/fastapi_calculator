from pydantic import BaseModel


class ReturnCalculator(BaseModel):
    status: int 
    result: int | float
    

    