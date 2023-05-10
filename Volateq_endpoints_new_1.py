import pytz
from flask import Flask, jsonify, request
import datetime
from pytz import timezone
from datetime import datetime

app = Flask(__name__)   # creating your web application with the name of the running program

print("Please choose time and date of which zone do you want to get")


def return_time_zone(zone : str, type_of_format : str) -> str:
    place_timezone = timezone(zone)
    time_in_this_zone = datetime.now(place_timezone)
    result_time_in_this_zone = time_in_this_zone.strftime(type_of_format)
    return result_time_in_this_zone



def return_possible_utc_zones():
    list_of_possible_utc_zones = []
    for time_zone in pytz.all_timezones:
        list_of_possible_utc_zones.append(time_zone)
    return list_of_possible_utc_zones

@app.route('/list_of_possible_timezones', methods=['GET'])
def return_all_time_zones():
    all_list_of_possible_utc_zones = return_possible_utc_zones()
    return jsonify({'All possible utc zones': all_list_of_possible_utc_zones})

#  several possible examples of 'data_format_user' :  "%m/%d/%Y" "%Y/%m/%d"   "%d-%m-%Y %H:%M"   "%d.%m.%Y"

@app.route('/params', methods=['GET'])
def return_one():
    time_zone_user = request.args['time_zone_user']
    data_format_user = request.args['data_format_user']
    data_time = return_time_zone(time_zone_user, data_format_user)
    return jsonify({'Data_time': data_time})


if __name__ == '__main__':
    app.run(debug=True, port=8080)   # run app