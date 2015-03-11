__author__ = 'rakesh'

from django.shortcuts import render
import sqlite3 as lite
import sys

def home(request):
    context = []
    open('/home/rakesh/Desktop/twitter/Source/templates/home1.html', 'w').close()
    if request.method == 'GET': #database fetch values based on database #how to set attributes in request
        text = request.GET["id"]
        text = str(text)
        con = lite.connect('/home/rakesh/Desktop/twitter/Source/twitter/user.db')
        with con:
            cur = con.cursor()
            cur.execute( "select latitude, longitude from tweet where tweet LIKE ?", ("%" + text + "%", ))

            rows = cur.fetchall()

            for row in rows:
                x = row[0]
                y = row[1]
                x = str(x)
                y = str(y)
                coordinate = 'new google.maps.LatLng' + '(' + x + "," + y + ')' + ','
                context.append(coordinate)

    y = open("/home/rakesh/Desktop/twitter/Source/templates/home1.html", 'a')
    first = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>   </title>
<style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
      #panel {
        position: absolute;
        top: 5px;
        left: 50%;
        margin-left: -180px;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
      }
       #panel1 {
        position: absolute;
        top: 5px;
        left: 50%;
        margin-left: -370px;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
      }
    </style>

    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true&libraries=visualization"></script>
 <script>

 var map, pointarray, heatmap;

var taxiData = [
    '''
    y.write(first)
    for i in range(0, len(context)):
        y.write(context[i])
        y.write('\n')

    second = '''
    ];

 function initialize() {
   var mapOptions = {
     zoom: 2,
     center: new google.maps.LatLng(32.00000, 6.000000),
     mapTypeId: google.maps.MapTypeId.SATELLITE
   };

   map = new google.maps.Map(document.getElementById('map-canvas'),
       mapOptions);

   var pointArray = new google.maps.MVCArray(taxiData);

   heatmap = new google.maps.visualization.HeatmapLayer({
     data: pointArray
   });

   heatmap.setMap(map);
 }

 function toggleHeatmap() {
   heatmap.setMap(heatmap.getMap() ? null : map);
 }

 function changeGradient() {
   var gradient = [
     'rgba(0, 255, 255, 0)',
     'rgba(0, 255, 255, 1)',
     'rgba(0, 191, 255, 1)',
     'rgba(0, 127, 255, 1)',
     'rgba(0, 63, 255, 1)',
     'rgba(0, 0, 255, 1)',
     'rgba(0, 0, 223, 1)',
     'rgba(0, 0, 191, 1)',
     'rgba(0, 0, 159, 1)',
     'rgba(0, 0, 127, 1)',
     'rgba(63, 0, 91, 1)',
     'rgba(127, 0, 63, 1)',
     'rgba(191, 0, 31, 1)',
     'rgba(255, 0, 0, 1)'
   ]
   heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
 }

 function changeRadius() {
   heatmap.set('radius', heatmap.get('radius') ? null : 20);
 }

 function changeOpacity() {
   heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
 }

 google.maps.event.addDomListener(window, 'load', initialize);

     </script>

</head>
<body>
     <div id="panel">
      <button onclick="toggleHeatmap()">Toggle Heatmap</button>
      <button onclick="changeGradient()">Change gradient</button>
      <button onclick="changeRadius()">Change radius</button>
      <button onclick="changeOpacity()">Change opacity</button>
 </div>
     <div id="map-canvas"></div>
     <div id="panel1">
     <form action="?">
  <select name="id" id="id" >
   <option value="snow">Snow</option>
   <option value="birthday">Happy Birthday</option>
   <option value="worldcup">World Cup</option>
   <option value="iphone">IPhone</option>
   <option value="cricket">Cricket</option>
  </select>
  <input type="submit" value="submit"/>
   </form>
   </div>
  </body>
</html>
'''
    y.write(second)
    template = index()
    #template = "home.html"
    print context
    return render(request, template)  #request lega, template is already defined, context

    #render function will get the request and give back template

def index():
    #template = 'index.html'
    return 'home.html'

#select * from tweet where tweet LIKE '%car%'




#cur.execute("INSERT INTO tweet (time, tweet, latitude, longitude) VALUES (?,?,?,?)", (time.time(), tweet,
                                                                                                #latitude, longitude))

