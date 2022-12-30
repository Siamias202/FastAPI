import bcrypt

class hasher:
    @staticmethod
    def hash_the_password(password:str)->str:
        hashed=bcrypt.hashpw(password,bcrypt.gensalt(rounds=15))
        return hashed

    @staticmethod
    def match_the_password(password:str,user_name:str)->bool:
        pass
