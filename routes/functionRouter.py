from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/functions",
    tags=['Functions Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllFunctions():
    print('getAllFunctions')


@router.get('/{function_id}', status_code=HTTPStatus.OK)
def getFunctionById():
    print('getFunctionById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createFunction():
    print('createFunction')


@router.put('/update/{function_id}', status_code=HTTPStatus.OK)
def updateFunction():
    print('updateFunction')


@router.delete('/remove/{function_id}', status_code=HTTPStatus.OK)
def deleteFunction():
    print('deleteFunction')