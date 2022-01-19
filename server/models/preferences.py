"""
Preferences model
"""


from pydantic import BaseModel
from pydantic.fields import Field


class PreferenceResponseModel(BaseModel):
    """
    Response model for preferences
    """

    status: bool = Field(
        ..., title="Status", description="Status of preference submission"
    )


class PreferenceRequestModel(BaseModel):
    """
    Request Model for Preferences
    """

    preference_1: str = Field(
        ...,
        title="Preference 1",
        description="Preference 1 for the user",
    )
    preference_2: str = Field(
        ...,
        title="Preference 2",
        description="Preference 2 for the user",
    )
    preference_3: str = Field(
        ...,
        title="Preference 3",
        description="Preference 3 for the user",
    )
