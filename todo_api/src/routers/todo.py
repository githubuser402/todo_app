from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from models import Task, TaskPydantic, TaskInPydantic, User, UserInPydantic, UserPydantic
from dependencies import get_user
from utils.logger import logger
from typing import List


router = APIRouter()


@router.get('/', response_model=List[TaskPydantic])
async def get_task_list(user: User = Depends(get_user)):
    tasks = await TaskPydantic.from_queryset(Task.filter(user=user).all())
    return tasks


@router.get('/{task_id}', response_model=TaskPydantic)
async def get_task(task_id: int, user: User = Depends(get_user)):
    try:
        task = await TaskPydantic.from_queryset_single(Task.filter(user=user).filter(id=task_id).first())
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Object not found"
        )
        
    return task


@router.post('/', response_model=TaskPydantic)
async def create_task(task_data: TaskInPydantic, user: User = Depends(get_user)):
    logger.debug(f'{task_data.dict(exclude_unset=True)}')
    task = Task(**task_data.dict(exclude_unset=True))
    task.user = user
    await task.save()
    return await TaskPydantic.from_tortoise_orm(task)


@router.get('/{task_id}/done', response_model=TaskPydantic)
async def change_task_done_status(user: User = Depends(get_user), task_id: int = None):
    task = await Task.filter(user=user).filter(id=task_id).first()
        
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Object not found"
        )
        
    task.done = not task.done
    await task.save()
    return await TaskPydantic.from_tortoise_orm(task)


@router.put('/{task_id}', response_model=TaskPydantic)
async def update_task(task_id:int, task_data: TaskInPydantic, user: User = Depends(get_user)):

    task = await Task.filter(user=user).get_or_none(id=task_id)
    print(f'\n\n\n\n\n\n{task} \n\n\n\n\n\n')
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Object not found"
        )
    
    # await task.update(**task_data.dict(exclude_unset=True, exclude={'done'}))
    return await TaskPydantic.from_tortoise_orm(task)


@router.delete('/{task_id}', response_model=TaskPydantic)
async def delete_task(task_id: int, user: User = Depends(get_user)):
    
    task = await Task.filter(user=user).filter(id=task_id).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Object not found"
        )

    task_json = await TaskPydantic.from_tortoise_orm(task) 
    await task.delete()
    
    return task_json