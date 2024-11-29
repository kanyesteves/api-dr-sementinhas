from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/presences",
    tags=['Presences Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllPresences():
    print('getAllPresences')


@router.get('/{presence_id}', status_code=HTTPStatus.OK)
def getPresenceById():
    print('getPresenceById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createPresence():
    print('createPresence')


@router.put('/update/{presence_id}', status_code=HTTPStatus.OK)
def updatePresence():
    print('updatePresence')


@router.delete('/remove/{presence_id}', status_code=HTTPStatus.OK)
def deletePresence():
    print('deletePresence')