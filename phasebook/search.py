from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_id(arg,id_list):
    if arg[1] == None:
        return
    match arg[0]:
        case "id":
            id_list[:] += [d["id"] for d in USERS if d.get(arg[0]) == arg[1]]
        case "name":
            id_list[:] += [d["id"] for d in USERS if arg[1].lower() in d.get(arg[0]).lower()]
        case "age":
            id_list[:] += [d["id"] for d in USERS if int(d.get(arg[0])) in range(int(arg[1])-1,int(arg[1])+2)]
        case "occupation":
            id_list[:] += [d["id"] for d in USERS if arg[1].lower() in d.get(arg[0]).lower()]
    return
    

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    if args == {}:
        return USERS

    id_list = []

    search_id(('id',args.get('id',None)),id_list)
    search_id(('name',args.get('name',None)),id_list) 
    search_id(('age',args.get('age',None)),id_list)
    search_id(('occupation',args.get('occupation',None)),id_list)

    id_list = list(dict.fromkeys(id_list))

    search_result =[]

    for id in id_list:
        search_result += [d for d in USERS if d["id"] == id]
        
    return search_result
