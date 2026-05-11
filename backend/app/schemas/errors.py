from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: str
    message: str
    request_id: str | None = None
    fields: list[str] = Field(default_factory=list)


class ErrorResponse(BaseModel):
    error: ErrorDetail
