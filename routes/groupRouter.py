from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/groups",
    tags=['Groups Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllGroups():
    print('getAllGroups')


@router.get('/{group_id}', status_code=HTTPStatus.OK)
def getGroupById():
    print('getGroupById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createGroup():
    print('createGroup')


@router.put('/update/{group_id}', status_code=HTTPStatus.OK)
def updateGroup():
    print('updateGroup')


@router.delete('/remove/{group_id}', status_code=HTTPStatus.OK)
def deleteGroup():
    print('deleteGroup')