from flask import Flask, jsonify, request
import datetime
from pytz import timezone
from datetime import datetime


app = Flask(__name__)
#now = datetime.now()

print("Please choose time and date of which zone do you want to get: 1) Asia_Kolkata, 2) US_Central, 3) Africa_Johannesburg")
print("You need to add this zone to the end of the URL address, that you get as the result of the program ")

@app.route('/<string:endpoint>', methods=['GET'])      # we are using method GET
def returnOne(endpoint):
    if  endpoint == 'Asia_Kolkata':     # If the user enters /Asia_Kolkata at the end of the received URL, he will get the date and time in this time zone
        place_timezone = timezone('Asia/Kolkata')
        time_in_this_zone = datetime.now(place_timezone)
        result = time_in_this_zone.strftime("%Y-%b-%A %H:%M:%S")
        return jsonify({'Data_time' : result})

    if endpoint == 'US_Central':       # If the user enters /US_Central at the end of the received URL, he will get the date and time in this time zone
        place_timezone = timezone('US/Central')
        time_in_this_zone = datetime.now(place_timezone)
        result = time_in_this_zone.strftime("%Y-%b-%A %H:%M:%S")
        return jsonify({'Data_time': result})

    if endpoint == 'Africa_Johannesburg':     # If the user enters /Africa_Johannesburg at the end of the received URL, he will get the date and time in this time zone
        place_timezone = timezone('Africa/Johannesburg')
        time_in_this_zone = datetime.now(place_timezone)
        result = time_in_this_zone.strftime("%Y-%b-%A %H:%M:%S")
        return jsonify({'Data_time': result})

if __name__ == '__main__':
    app.run(debug=True, port=8080)   # run app