from flask import Flask, request
import json, dbhelpers, apihelpers

app = Flask(__name__)

@app.post("/api/client")
def post_client():
    error = apihelpers.check_endpoint_info(request.json, ["username", "password", "is_premium"])
    if(error != None):
        return error

    results = dbhelpers.run_procedure("call insert_client(?,?,?)", [request.json.get("username"),request.json.get("password"),request.json.get("is_premium")])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Sorry, something went wrong!"

@app.patch("/api/client")
def patch_client():
    error = apihelpers.check_endpoint_info(request.json, ["username", "old_password", "new_password"])
    if(error != None):
        return error
    
    results = dbhelpers.run_procedure("call update_password(?,?,?)", [request.json.get("username"),request.json.get("old_password"),request.json.get("new_password")])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Sorry, something went wrong!"


app.run(debug=True)