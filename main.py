from fastapi import FastAPI
import uvicorn

from client.run import start_app
from routers.calc_router.multifunctional import multi


app = FastAPI(lifespan=start_app)

app.include_router(multi)




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)