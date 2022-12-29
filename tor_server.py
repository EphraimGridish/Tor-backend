from fastapi import FastAPI
import uvicorn
from database_managers.users_manager import UserManager
from sqlite3 import IntegrityError
import json

app = FastAPI()
user_manager = UserManager()

# try:
#     user_manager.add_user('Admin', 'admin')
# except IntegrityError:
#     print("User exists.")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/<username>/<password>")
def verify_user(username, password):
    return json.dumps(user_manager.verify_user(username, password))

@app.post("/users/<username>/<password>")
def create_user(username, password):
    pass

if __name__ == "__main__":
    uvicorn.run("tor_server:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
