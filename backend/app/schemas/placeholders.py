from pydantic import BaseModel, Field


class PlaceholderInfoResponse(BaseModel):
    resource: str
    status: str = "placeholder"
    phase: str = "phase_1_mvp"
    message: str
    implemented: bool = False


class PlaceholderValidationRequest(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    notes: str | None = Field(default=None, max_length=500)


class PlaceholderValidationResponse(BaseModel):
    resource: str
    accepted: bool
    received_name: str
    notes: str | None = None
