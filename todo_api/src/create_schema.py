from tortoise import Tortoise, run_async
from pathlib import Path


async def connectToDatabase():
    await Tortoise.init(
        db_url=f'sqlite://{Path(__name__).parent}/db.sqlite3',
        modules={'models': ['models']}
    )


async def main():
    await connectToDatabase()
    await Tortoise.generate_schemas()
    
    
if __name__ == '__main__':
    run_async(main())
