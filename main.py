from application.elevator_demander import ElevatorDemander
from application.demand_history_handler import DemandHistoryHandler
from model.elevator import Elevator
from db.demand_history_db import DemandHistoryDB
from db import database
from pydantic import BaseModel

from fastapi import FastAPI


class DemandRequest(BaseModel):
    demanded_floor: int


# Initialize the database
database_file = "database.db"
database.create_database(database_file)

# Create an instance of the Elevator class
elevator = Elevator(1, 0, 3)

# Create an instance of the DemandHistoryDB class
demand_history_db = DemandHistoryDB(database_file)

# Create an instance of the DemandHistoryHandler class
demand_history_handler = DemandHistoryHandler(demand_history_db)

# Create an instance of the ElevatorDemander class
elevator_demander = ElevatorDemander(elevator, demand_history_handler)

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Define the endpoint for the /demand
@app.post("/demand")
async def demand(request: DemandRequest):
    elevator_demander.demand(request.demanded_floor)
    return {"message": "Elevator demanded successfully"}


# Define the endpoint for the /complete_demand_history
@app.get("/complete_demand_history")
async def complete_demand_history():
    demand_history = demand_history_handler.get_complete_demand_history(elevator.id)
    return demand_history
