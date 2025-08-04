from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import price

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # یا ["http://localhost:3000"] برای امنیت بیشتر
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(price.router)

@app.get("/")
def root():
    return {"message": "CryptoRL Dashboard API is running."}