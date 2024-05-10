from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.generate_world import GenerateWorld

app = FastAPI()
# 允许所有来源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "Wirld"}

@app.post("/generateReport/")
def generateReport(data:dict):
    GenerateWorld().start_generate_world(data)
    return {"status": 'success'}