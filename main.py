from application.elevator_demander import ElevatorDemander
from application.demand_history_handler import DemandHistoryHandler
from model.elevator import Elevator
from db.demand_history_db import DemandHistoryDB
from db import database

from application.api_models import *

from fastapi import FastAPI

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


# Define the endpoint for the /demand
@app.post("/demand")
async def demand(request: DemandRequest):
    if request.elevator_id == elevator.id:
        elevator_demander.demand(request.demanded_floor)
        return {"message": "Elevator demanded successfully"}
    return {"message": "Elevator not found"}


# Define the endpoint for the /update_ideal_resting_floor
@app.patch("/update_ideal_resting_floor")
async def update_ideal_resting_floor(request: ElevatorIdealRestingFloorRequest):
    if request.elevator_id == elevator.id:
        elevator.ideal_floor = request.ideal_floor
        return {"message": "Ideal resting floor updated successfully"}
    return {"message": "Elevator not found"}


# Define the endpoint for the /complete_demand_history
@app.get("/complete_demand_history/{elevator_id}")
async def complete_demand_history(elevator_id: int):
    if elevator_id == elevator.id:
        demand_history = demand_history_handler.get_complete_demand_history(elevator.id)
        return demand_history
    return {"message": "Elevator not found"}
