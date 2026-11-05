from backend import app

if __name__ == "__main__":
    print("pictures microservice.")
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )