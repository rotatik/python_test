import uvicorn
from app import app


def main() -> None:
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()