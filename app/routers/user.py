from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password - user.password
    check_email = db.query(models.User).filter(models.User.email == user.email).first()
    
    if check_email:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"user with {user.email} already exists")

    hashed_pasword = utils.hash(user.password)
    user.password = hashed_pasword
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} does not exists')

    return user