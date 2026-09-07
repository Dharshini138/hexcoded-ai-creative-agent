from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.agents.creative_director import create_creative_plan

router = APIRouter()


class CreativeBrief(BaseModel):
    brief: str


@router.post("/generate")
def generate_creative_plan(request: CreativeBrief):

    if not request.brief.strip():
        raise HTTPException(
            status_code=400,
            detail="Creative brief cannot be empty."
        )

    try:
        result = create_creative_plan(request.brief)

        return {
            "success": True,
            "workflow": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )