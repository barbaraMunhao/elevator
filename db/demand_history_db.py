import sqlite3

# DB class


class DemandHistoryDB(object):
    def __init__(self, database_file):
       self._database_file = database_file

    def _connect(self):
        connection = None
        try:
            connection = sqlite3.connect(self._database_file)
        except sqlite3.Error as e:
            print(e)
        finally:
            return connection

    def save_demand(self, elevator_id, resting_floor, demanded_floor):
        connection = self._connect()
        query = ("INSERT INTO  demand(elevator_id, rest_floor, demanded_floor) "
                 "VALUES ({0}, {1}, {2})").format(elevator_id, resting_floor, demanded_floor)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def get_demand_history(self, elevator_id):
        connection = self._connect()

        query = "SELECT * FROM  demand WHERE elevator_id ={0}".format(elevator_id)
        cursor = connection.cursor()
        res = cursor.execute(query)
        rows = res.fetchall()
        connection.close()

        return rows
