import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:app",
        host="localhost",
        port=8000
    )
