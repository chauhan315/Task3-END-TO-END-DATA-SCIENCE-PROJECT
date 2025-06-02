from pydantic import BaseModel, Field

class PersonalityInput(BaseModel):
    Time_spent_Alone: float = Field(..., ge=0, le=10, description="Time spent alone between 0 and 10")
    Stage_fear: str = Field(..., pattern="^(yes|no)$", description="Stage fear as 'yes' or 'no'")
    Social_event_attendance: float = Field(..., ge=0, le=10, description="Social event attendance between 0 and 10")
    Going_outside: float = Field(..., ge=0, le=10, description="Going outside frequency between 0 and 10")
    Drained_after_socializing: str = Field(..., pattern="^(yes|no)$", description="Drained after socializing as 'yes' or 'no'")
    Friends_circle_size: int = Field(..., ge=0, le=50, description="Friends circle size between 0 and 50")
    Post_frequency: float = Field(..., ge=0, le=10, description="Post frequency between 0 and 10")
