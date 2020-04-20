DB_USER = 'root'
DB_PASS = 'admin1234'
DB_NAME = 'iot'
DB_LOCALHOST = 'localhost'

FACTOR = 10
BOTTOM_HEART_RATE = 60

def create_insert_query(user):
    query = f"""
    INSERT INTO iot.runner(id,name,device,activity_level)
    VALUES("{user['id']}","{user['name']}","{ user['device']}","{user['activity_level']}");
    """
    return query

def generate_select_runners_query():
    query = """SELECT id FROM iot.runner;"""
    return query

def generate_get_runner_query(runner_id):
    query = f"""SELECT * FROM iot.runner WHERE iot.runner.id="{runner_id}";"""
    return query