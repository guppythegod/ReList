from flask import Flask, jsonify, request
import boto3
import jwt
import datetime

dynamodb = boto3.resource("dynamodb")
users = dynamodb.Table("relist-users")

app = Flask(__name__)


def find_and_verify_key(uid: str, post_request: dict):
    try:
        api_key: str = post_request.form["api_key"]
        auth_token: str: post_request.form["auth_token"]
    except KeyError as e:
        return {"status":403,"error":str(e)}
    else:
        try:
            decoded_key: dict = jwt.decode(api_key, auth_token, algorithms=["HS256"])
            permissions = decoded_key["permissions"]
            d_uid = decoded_key["uid"]
            if permissions == "*" and d_uid == uid:
                return True
            return {"status":401,"error":"invalid api key."}
        except Exception as e:
            return {"status":505,"error":str(e)


app.route("/api/register",methods=["POST"])
def register() -> dict:
    try:
        email: str = request.form["email"]
        password: str = request.form["password"]
        auth_token: str = jwt.encode({"user":email, {"actions":'"*'}}, password, algorithm=["HS256"])
        uid: str = jwt.encode("relist-user", email, algorithm=["HS256"])
        api_key: str = jwt.encode({"uid":uid,"permissions":"*", "datetime":datetime.datetime.now()}, auth_token, algorithm=["HS256"])
    except KeyError as e:
        return jsonify({"status":403,"error":str(e)})
    except Exception as e:
        return jsonify({"status":505,"error":str(e)})
    else:
        try:
            put_response: dict = users.put_item(
                Item={
                    "uid" : uid,
                    "email" : email,
                    "auth_token" : auth_token,
                    "projects" : [],
                    "todos" : []
                }
            )
        except Exception as e:
            return jsonify({"status":505,"error":str(e)})
        else:
            if put_response:
                return jsonify({"status":202,"data":{"uid":uid,"email":email,"api_key":api_key}})


app.route("/api/login", methods=["POST"])
def login() -> dict:
    try:
        email: str = request.form["email"]
        password: str = request.form["password"]
    except KeyError as e:
        return jsonify({"status":403,"error":str(e)})
    except Exception as e:
        return jsonify({"status":505,"error":str(e)})
    else:
        uid_attempt: str = jwt.encode("relist-user", email, algorithm=["HS256"])
        try:
            user_data: dict = users.get_item(Key={"uid":uid_attempt})
        except boto3.exceptions.Boto3Error as e:
            return jsonify({"status":506,"error":str(e)})
        except Exception as e:
            return jsonify({"status":505,"error":str(e)})
        else:
            decoded_payload: dict = jwt.decode(user_data["auth_token"], password, algorithms=["HS256"])
            if decoded_payload["email"] == email:
                new_api_key = jwt.encode({"uid":uid_attempt,"permissions":"*","datetime":datetime.datetime.now()}, user_data["auth_token"], algorithm=["HS256"])
                return jsonify({"status":202},"date":{"uid":uid_attempt,"email":email,"api_key":new_api_key})


app.route("/api/<string:uid>/todos", methods=["GET","POST","DELETE"])
def todos_resource(uid) -> dict:
    response = find_and_verify_key(uid, request.form)
    if response == True:
        if request.method == "GET":
            try:
                user_data: dict = users.get_item(Key={"uid":uid})
            except boto3.exceptions.Boto3Error as e:
                return jsonify({"status":506,"error":str(e)})
            except Exception as e:
                return jsonify({"status":505,"error":str(e)})
            else:
                try:
                    user_todos: list = user_data["todos"]
                except TypeError as e:
                    return jsonify({"status":505,"error":str(e)})
                else:
                    return jsonify({"status":202,"data":{"todos":user_todos},"meta":{"uid":uid}})
        elif request.method == "POST":
                try:
                    todo = request.form["todo"]
                    project_id = request.form["project_id"]
                except KeyError as e:
                    return jsonify({"status":403,"error":str(e)})
                except Exception as e:
                    return jsonify({"status":505,"error":str(e)})
                else:
                    todo_id = jwt.encode({"todo":todo}, uid, algorithm=["HS256"])
                    todo_item: dict = {"todo_id":todo_id,"description":todo,"project_id":project_id,"status":False}
                    try:
                        # put item in db
                        pass
                    except Exception as e:
                        return jsonify({"status":505,"error":str(e)})
        elif request.method == "DELETE":
            pass
    else:
        return jsonify(response)


app.route("/api/<string:uid>/todos/status", methods=["POST"])
def todos_status_resource(uid):
    response = find_and_verify_key(uid, request.form)
    if response == True:
        try:
            new_status: bool = request.form["new_status"]
            todo_id: str = request.form["todo_id"]
        except KeyError as e:
            return jsonify({"status":403,"error":str(e)})
        except Exception as e:
            return jsonify({"status":505,"error":str(e)})
        else:
            # change status here
    else:
        return jsonify(response)


app.route("/api/<string:uid>/projects", methods=["GET","POST","DELETE"])
def projects_resouce(uid) -> dict:
    reponse = find_and_verify_key(uid, request.form)
    if response == True:
        if request.method == "GET":
            try:
                user_data: dict = users.get_item(Key={"uid":uid})
            except boto3.exceptions.Boto3Error as e:
                return jsonify({"status":506,"error":str(e)})
            except Exception as e:
                return jsonify({"status":505,"error":str(e)})
            else:
                try:
                    user_projects: list = user_data["projects"]
                except TypeError as e:
                    return jsonify({"status":505,"error":str(e)})
                else:
                    return jsonify("status":202,"data":{"projects":user_projects},"meta":{"uid":uid})
        elif request.method == "POST":
                try:
                    project = request.form["project"]
                except KeyError as e:
                    return jsonify({"status":403,"error":str(e)})
                except Exception as e:
                    return jsonify({"status":505,"error":str(e)})
                else:
                    project_id = jwt.encode({"project":project}, uid, algorithm=["HS256"])
                    project_item = {"project_id":project_id,"name":project}
                    try:
                        response = users.update_item(
                            Key={"uid":uid},
                        )
                        pass
                    except Exception as e:
                        return jsonify({"status":505,"error":str(e)})
        elif request.method == "DELETE":
            try:
    else:
        return jsonify(response)

