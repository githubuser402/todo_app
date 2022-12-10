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


class Task(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=150)
    description = fields.TextField(null=True)
    created = fields.DatetimeField(auto_now=True)
    do_till = fields.DatetimeField(null=True)
    user = fields.ForeignKeyField('models.User', related_name='tasks')
    done = fields.BooleanField(default=False)

    def __repr__(self) -> str:
        return f'<{self.id} {self.title[:20]}>'

    class PydanticMeta:
        pass
    

TaskPydantic = pydantic_model_creator(Task, name="Task")
TaskInPydantic = pydantic_model_creator(Task, name="TaskIn", exclude_readonly=True)
