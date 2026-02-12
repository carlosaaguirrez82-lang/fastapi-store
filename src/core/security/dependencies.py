from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from src.core.settings import settings
#from src.infrastructure.db.session import get_db
from sqlalchemy.orm import Session
from src.infrastructure.db.models.user import User

def get_current_user(token: str, db: Session):

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user = db.get(User, int(user_id))

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def require_admin(user = Depends(get_current_user)):
    if user.role.name != "MANAGER":
        raise HTTPException(status_code=403, detail="MANAGER required")
    return user