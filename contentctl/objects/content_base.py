from pydantic import BaseModel, Extra


class ContentBase(BaseModel):
    class Config:
        extra = Extra.forbid
        validate_assignment = True