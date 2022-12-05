from flask import Flask, render_template
from get_distance import dist
#import everything

app = Flask('app')

@app.route('/')
def iss_data():
  data = []
  #connect to each module, download and return data
  #send data to flask page (connect to jinja)
  
  #distance from the iss
  distance = dist(46.474529,-80.945824,6,7) #your location and the location of the ISS in lat/lon
  dist_ = f"You are {distance}km from the ISS"
  data.append(dist_)

  return render_template("index.html",data=data)

app.run(host='0.0.0.0', port=8080)
