from typing import List

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post(
    "/",
    response_model=SummaryResponseSchema,
    summary="Create a summary",
    description="Add created summaries to database",
    status_code=201,
)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object


@router.get(
    "/{id}/",
    response_model=SummarySchema,
    summary="Read particular summary with given id",
)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.get(
    "/", response_model=List[SummarySchema], summary="Read all summaries in database"
)
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()
