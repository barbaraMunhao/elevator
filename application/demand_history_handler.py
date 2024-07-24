from db.demand_history_db import DemandHistoryDB


class DemandHistoryHandler(object):

    def __init__(self, demand_history_db):
        self._demand_history_db = demand_history_db

    def save_demand(self, elevator_id, resting_floor, demanded_floor):
        self._demand_history_db.save_demand(elevator_id, resting_floor, demanded_floor)

    #todo - definir se terá mais algum serviço
    def get_complete_demand_history(self, elevator_id):
        demand_history = self._demand_history_db.get_demand_history(elevator_id)
        return demand_history

