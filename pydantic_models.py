from pydantic import BaseModel, Field


class ChangeComponent(BaseModel):
    id_action: int
    id_component: int
    id_user: str = Field(
        ..., pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
    new_value: str
    old_value: str
    # date: str = Field(
    #     ..., pattern="^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})?$")
