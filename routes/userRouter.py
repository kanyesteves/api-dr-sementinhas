from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/users",
    tags=['Users Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllUsers():
    print('getAllUsers')


@router.get('/{user_id}', status_code=HTTPStatus.OK)
def getUserById():
    print('getUserById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createUser():
    print('createUser')


@router.put('/update/{user_id}', status_code=HTTPStatus.OK)
def updateUser():
    print('updateUser')


@router.delete('/remove/{user_id}', status_code=HTTPStatus.OK)
def deleteUser():
    print('deleteUser')