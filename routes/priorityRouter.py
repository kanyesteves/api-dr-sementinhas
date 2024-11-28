from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/prioritys",
    tags=['Prioritys Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllPrioritys():
    print('getAllPrioritys')


@router.get('/{priority_id}', status_code=HTTPStatus.OK)
def getPriorityById():
    print('getPriorityById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createPriority():
    print('createPriority')


@router.put('/update/{priority_id}', status_code=HTTPStatus.OK)
def updatePriority():
    print('updatePriority')


@router.delete('/remove/{priority_id}', status_code=HTTPStatus.OK)
def deletePriority():
    print('deletePriority')