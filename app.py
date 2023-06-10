from flask import Flask, request, make_response, jsonify
import dbhelpers, apihelpers

app = Flask(__name__)

@app.post("/api/client")
def post_client():
    error = apihelpers.check_endpoint_info(request.json, ["username", "password", "is_premium"])
    if(error != None):
        return make_response(jsonify(error), 400)

    results = dbhelpers.run_procedure("call insert_client(?,?,?)", [request.json.get("username"),request.json.get("password"),request.json.get("is_premium")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong!"), 500)

@app.patch("/api/client")
def patch_client():
    error = apihelpers.check_endpoint_info(request.json, ["username", "old_password", "new_password"])
    if(error != None):
        return make_response(jsonify(error), 400)
    
    results = dbhelpers.run_procedure("call update_password(?,?,?)", [request.json.get("username"),request.json.get("old_password"),request.json.get("new_password")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong!"), 500)
    
@app.get("/api/client")
def get_clients():
    results = dbhelpers.run_procedure("call get_all_clients()", [])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong!"), 500)


app.run(debug=True)