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

def generate_get_runners_path_query(runner_id):
    query = f"""
    SELECT * FROM iot.path 
    WHERE iot.path.runner_id="{runner_id}" 
    ORDER BY path_x ASC;
    """
    return query

def create_insert_path_query(current_x, current_y,current_distance, speed):
    global cur_email, path_name
    query = f"""
    INSERT INTO iot.path (id, runner_id,path_x,path_y,speed,heart_rate,distance,path_name) 
    VALUES
    ( "{uuid.uuid4()}",(SELECT id from iot.runner WHERE id='{cur_email}'),
    {current_x},{current_y},{speed},{speed*FACTOR+BOTTOM_HEART_RATE},{round(current_distance/M_TO_KM, 2)},"{path_name}");
    """
    return query