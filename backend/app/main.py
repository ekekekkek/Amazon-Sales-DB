from fastapi import FastAPI
from .routers import products, users, reviews

app = FastAPI(title="Amazon Sales API", version="1.0.0")

# Include the products router
app.include_router(products.router)
app.include_router(users.router)
app.include_router(reviews.router)

@app.get("/")
def read_root():
    return {"message": "Amazon Sales API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
