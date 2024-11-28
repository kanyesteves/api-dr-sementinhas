from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/events",
    tags=['Events Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllEvents():
    print('getAllEvents')


@router.get('/{event_id}', status_code=HTTPStatus.OK)
def getEventById():
    print('getEventById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createEvent():
    print('createEvent')

@router.put('/update/{event_id}', status_code=HTTPStatus.OK)
def updateEvent():
    print('updateEvent')

@router.delete('/remove/{event_id}', status_code=HTTPStatus.OK)
def deleteEvent():
    print('deleteEvent')