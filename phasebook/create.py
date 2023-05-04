from flask import Blueprint, request

bp = Blueprint("Create Data",__name__,url_prefix="/create")

@bp.route("/data",methods=["GET"])
def get_data():
    
    try:    
        index = int(request.get_json().get("text"))

        file = open("./new_data.txt","r")
        print("\n\n\n\n\n")
        data_list = file.read()
        data_list = data_list.split("\n")
        print(data_list)
        print("\n\n\n\n\n")
        
        
        print(data_list)
        print("\n\n\n\n\nLUL")

        return {"message":"success","data":data_list[index]},200
    
    except:
        return {"message":"error"},500

@bp.route("/data",methods=["POST"])
def create():

    new_data = request.get_json()
    text = new_data.get("text")

    new_file = open("./new_data.txt","a")
    
    new_file.write(text+"\n")


    new_file.close()

    

    return {"message":"success","data":text},201