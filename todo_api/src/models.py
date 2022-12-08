from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from passlib.hash import pbkdf2_sha256 as  sha256


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True, null=False)
    password = fields.CharField(max_length=100, null=False)
    
    @staticmethod
    def generate_hash(password: str) -> bool:
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(hash: str, password: str) -> bool:
        return sha256.verify(password, hash)

    def __repr__(self) -> str:
        return f"<{self.id} {self.nickname}>" 

    class PydanticMeta:
        pass

UserPydantic = pydantic_model_creator(User, name="User")
UserInPydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)