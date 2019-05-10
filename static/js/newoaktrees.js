function loadtrees(){
    var regexloc=/POINT \((.+) (.+)\)/;
    var xhttp = new XMLHttpRequest();
    var geojson=[];
    var i=0;
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var trees = this.responseText.split(/\),/);
        for (i = 0; i < trees.length; i++){
            trees[i]=trees[i].split(",");
            var matchlotlang=regexloc.exec(trees[i][0]);
            var longitude= matchlotlang[1];
            var latitude= matchlotlang[2];
            var specie = trees[1][22];
            trees[i][0]=[latitude,longitude];
            geojson.push(
                {
                  "type": "Feature",
                  "geometry": {
                    "type": "Point",
                    "coordinates": [longitude,latitude ]
                  },
                  "properties": {
                    "specie": specie
                  }
                }
            )
        }
        //write tree data on page
        document.getElementById("trees").innerHTML = JSON.stringify(geojson);
        //plot trees in map
        map.addLayer({
            "id": "trees",
            "type": "symbol",
            "source": {
            "type": "geojson",
            "data": {
            "type": "FeatureCollection",
            "features":geojson}
            },
            "layout": {
                "icon-image": "circle-11",
                "icon-size":1.5
                }
        }
        )
          
          
          
          
      }
    };
    xhttp.open("GET", "/trees", true);
    xhttp.send();
}