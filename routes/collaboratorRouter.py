from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(
    prefix="/collaborators",
    tags=['Collaborators Endpoints']
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllCollaborators():
    print('getAllCollaborators')


@router.get('/{collaborator_id}', status_code=HTTPStatus.OK)
def getCollaboratorById():
    print('getCollaboratorById')


@router.post('/register', status_code=HTTPStatus.CREATED)
def createCollaborator():
    print('createCollaborator')

@router.put('/update/{collaborator_id}', status_code=HTTPStatus.OK)
def updateCollaborator():
    print('updateCollaborator')

@router.delete('/remove/{collaborator_id}', status_code=HTTPStatus.OK)
def deleteCollaborator():
    print('deleteCollaborator')