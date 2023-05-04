from flask import Blueprint, request
import datetime


bp = Blueprint("schedule", __name__, url_prefix="/schedule")

USERS = {}


@bp.route("<int:user_id>",methods=["POST"])
def schedule(user_id):
    try:    
        user = request.get_json()

        start_schedule = user.get("start")
        end_schedule = user.get("end")

        available_time = start_schedule + " - " + end_schedule

        start_schedule = datetime.datetime.strptime(start_schedule,'%H:%M')
        end_schedule = datetime.datetime.strptime(end_schedule,'%H:%M')

        if user_id in USERS:
            if available_time not in USERS[user_id]:

                insert_index = -1
                
                start_schedule_list = [datetime.datetime.strptime(i.split(" - ")[0],'%H:%M')for i in USERS[user_id]]
                end_schedule_list = [datetime.datetime.strptime(i.split(" - ")[1],'%H:%M') for i in USERS[user_id]]

                for i in range(len(start_schedule_list)):
                    if start_schedule.time() < start_schedule_list[i].time():
                        insert_index = i
                        break
                    elif start_schedule.time() == start_schedule_list[i].time():
                        if end_schedule.time() < end_schedule_list[i].time():
                            insert_index = i
                            break
                
                if insert_index == -1:
                    USERS[user_id].append(available_time)
                else:
                    USERS[user_id].insert(insert_index,available_time)

        else:
            USERS[user_id] = [available_time]


        return {"user_id":user_id,"schedules":USERS[user_id]},200
    
    except:
        return {"message":"error"},500

@bp.route("<int:user_id>",methods=["GET"])
def merge_schedule(user_id):
    print("this")