from pydantic import BaseModel


class BaseChema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True
