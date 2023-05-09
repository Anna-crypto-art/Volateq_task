import pytz
from flask import Flask, jsonify, request
import datetime
from pytz import timezone
from datetime import datetime


app = Flask(__name__)   # creating your web application with the name of the running program




print("Please choose time and date of which zone do you want to get")
print("You need to add this zone to the end of the URL address and add _Y_b_A or Y_m_d or Y_b_d, that you get as the result of the program ")

def return_time_zone(zone : str, type_of_format : str) -> str:
    place_timezone = timezone(zone)
    time_in_this_zone = datetime.now(place_timezone)
    if type_of_format == "Y_b_A":
        result_time_in_this_zone = time_in_this_zone.strftime("%Y-%b-%A %H:%M:%S")
    if type_of_format == "Y_m_d":
        result_time_in_this_zone = time_in_this_zone.strftime("%Y-%m-%d %H:%M:%S")
    if type_of_format == "Y_b_d":
        result_time_in_this_zone = time_in_this_zone.strftime("%Y-%b-%d %H:%M:%S")
    return result_time_in_this_zone



def return_possible_utc_zones():
    list_of_possible_utc_zones = []
    for timeZone in pytz.common_timezones:
        list_of_possible_utc_zones.append(timeZone)
    return list_of_possible_utc_zones

@app.route('/list_of_possible_timezones', methods=['GET'])
def return_all_time_zones():
    all_list_of_possible_utc_zones = return_possible_utc_zones()
    return jsonify({'All possible utc zones': all_list_of_possible_utc_zones})



@app.route('/<string:endpoint>', methods=['GET'])
def return_one(endpoint : str) -> str:
    if  endpoint == 'Asia_Kolkata_Y_b_A':
        data_time = return_time_zone('Asia/Kolkata', 'Y_b_A')
        return jsonify({'Data_time': data_time})

    if endpoint == 'Asia_Kolkata_Y_m_d':
        data_time = return_time_zone('Asia/Kolkata', 'Y_m_d')
        return jsonify({'Data_time': data_time})

    if endpoint == 'Asia_Kolkata_Y_b_d':
        data_time = return_time_zone('Asia/Kolkata', 'Y_b_d')
        return jsonify({'Data_time': data_time})

    if endpoint == 'US_Central_Y_b_A':
        data_time = return_time_zone('US/Central', 'Y_b_A')
        return jsonify({'Data_time': data_time})

    if  endpoint == 'US_Central_Y_m_d':
        data_time = return_time_zone('US/Central', 'Y_m_d')
        return jsonify({'Data_time': data_time})

    if endpoint == 'US_Central_Y_b_d':
        data_time = return_time_zone('US/Central', 'Y_b_d')
        return jsonify({'Data_time': data_time})

    if endpoint == 'Africa_Johannesburg_Y_b_A':
        data_time = return_time_zone('Africa/Johannesburg', 'Y_b_A')
        return jsonify({'Data_time': data_time})

    if endpoint == 'Africa_Johannesburg_Y_m_d':
        data_time = return_time_zone('Africa/Johannesburg', 'Y_m_d')
        return jsonify({'Data_time': data_time})

    if  endpoint == 'Africa_Johannesburg_Y_b_d':
        data_time = return_time_zone('Africa/Johannesburg', 'Y_b_d')
        return jsonify({'Data_time': data_time})

if __name__ == '__main__':
    app.run(debug=True, port=8080)   # run app