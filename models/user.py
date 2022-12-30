from beanie import Document

class User(Document):
    user_name:str
    email:str
    password:str
    address:str
    position:str

    class settings:
        name:"user_info"

