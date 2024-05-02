from flask import Flask,render_template,request,redirect

webapp = Flask(__name__)

# <!--const xValues = [10,2030,40,90,100,110,120,130,140,150];-->
# <!--const yValues = [7,8,8,9,9,9,10,11,14,14,15];-->
data_today  = {"Current Water Level" : "Medium",
        "Overall Run Duration" : "1hr",
        "Electricity Consumption": "1kW"}

xValues = [1,2,3,4,5]
yValues = [1,2,3,4,5]

data_hist  = { "Mon" : { "Current Water Level" : "Medium",
                        "Overall Run Duration(hr)" : 2,
                        "Electricity Consumption(kW)": 10},
                "Tue" : { "Current Water Level" : "high",
                        "Overall Run Duration(hr)" : 5,
                        "Electricity Consumption(kW)": 20},
                "Wed" : { "Current Water Level" : "Low",
                        "Overall Run Duration(hr)" : 7,
                        "Electricity Consumption(kW)": 30},
                "Thu" : { "Current Water Level" : "Medium",
                        "Overall Run Duration(hr)" : 4,
                        "Electricity Consumption(kW)": 10},
                "Fri" : { "Current Water Level" : "high",
                        "Overall Run Duration(hr)" : 9,
                        "Electricity Consumption(kW)": 20},
                "Sat" : { "Current Water Level" : "Low",
                        "Overall Run Duration(hr)" : 5,
                        "Electricity Consumption(kW)": 30},
               "Sun": {"Current Water Level": "Low",
                       "Overall Run Duration(hr)": 10,
                       "Electricity Consumption(kW)": 10}
               }


@webapp.route("/")
@webapp.route("/login")
def login():
    return render_template("login.html")


@webapp.route("/mode" ,methods = ["GET","POST"])
def mode():

    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]

        if uname == "shakil" and pwd == "1234":
            return render_template("mode.html" )
        else:
            return render_template("invalid.html" )
    else:
        return redirect("/")

@webapp.route("/stats" ,methods = ["GET","POST"])
def stats():

    if request.method == "POST":
        mode = request.form["Mode"]
        return render_template("stats.html",mode=mode,data_today=data_today)
    else:
        return redirect("/")

@webapp.route("/history" ,methods = ["GET","POST"])
def history():
    x_values = []
    y_run_time = []
    y_elect = []
    for key,value in data_hist.items():
        x_values.append(key)
        y_run_time.append(value["Overall Run Duration(hr)"])
        y_elect.append(value["Electricity Consumption(kW)"])

    return render_template("history.html", x_values = x_values, y_run_time = y_run_time, y_elect = y_elect)

webapp.run(debug=True)