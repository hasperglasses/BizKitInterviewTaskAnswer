from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_id(arg):
    match arg[0]:
        case "id":
            return [d["id"] for d in USERS if d.get(arg[0]) == arg[1]]
        case "name":
            return [d["id"] for d in USERS if arg[1].lower() in d.get(arg[0]).lower()]
        case "age":
            return [d["id"] for d in USERS if int(d.get(arg[0])) in range(int(arg[1])-1,int(arg[1])+2)]
        case "occupation":
            return [d["id"] for d in USERS if arg[1].lower() in d.get(arg[0]).lower()]
    return None
    

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
    id_list = []
    for arg in args.items():
        id_list += search_id(arg)

    id_list = list(dict.fromkeys(id_list))

    search_result =[]

    for id in id_list:
        search_result += [d for d in USERS if d["id"] == id]
    return search_result
