from pydantic import BaseModel


class DemandRequest(BaseModel):
    elevator_id: int
    demanded_floor: int


class ElevatorIdealRestingFloorRequest(BaseModel):
    elevator_id: int
    ideal_floor: int


class Demand(BaseModel):
    resting_floor: int
    demanded_floor: int
