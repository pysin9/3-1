var streets = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png',{
    maxZoom: 18,
    minZoom: 12,
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
var grayscale = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
    maxZoom: 18,
    minZoom: 12,
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
var latlng = L.latLng(1.3521, 103.8198);
var map = L.map('map', {
    center: latlng,
    zoom: 12,
    zoomControl: false,
    fullscreenControl: true,
    fullscreenControlOptions: { // optional
        title: "Show me the fullscreen !",
        titleCancel: "Exit fullscreen mode"
    },
    layers: [grayscale, streets ]
});

var markers = L.markerClusterGroup(),
    markers1 = L.featureGroup.subGroup(markers),
    markers2 = L.featureGroup.subGroup(markers),
    markers3 = L.featureGroup.subGroup(markers),
    markers4 = L.featureGroup.subGroup(markers),
    markers5 = L.featureGroup.subGroup(markers),
    markers6 = L.featureGroup.subGroup(markers),
    markers7 = L.featureGroup.subGroup(markers),
    markers8 = L.featureGroup.subGroup(markers),
    control = L.control.layers(null, null, { collapsed: false }),
    i, a, title, marker;
markers.addTo(map);

control.addOverlay(markers1, 'Spicy');
control.addOverlay(markers2, 'Halal');
control.addOverlay(markers3, 'Vegertarian');
control.addOverlay(markers4, 'Healthy');
control.addOverlay(markers5, 'Elder Friendly');
control.addOverlay(markers6, 'Desert');
control.addOverlay(markers7, 'Hawker');
control.addOverlay(markers8, 'Cafes')
control.addTo(map);



markers1.addTo(map);
markers2.addTo(map);
markers3.addTo(map);
markers4.addTo(map);
markers5.addTo(map);
markers6.addTo(map);
markers7.addTo(map);
markers8.addTo(map);




var markerList = [];
var controlSearch = new L.Control.Search({
    position: 'topleft',
    layer: markers,
    initial: false,
    zoom: 18,
    marker: false
});

$.ajax({
    url: '/api',
    type: 'POST',
    dataType: "json",
    success: function (map_data) {
        for (var i = 0; i < map_data.length; i++) {
            var title = map_data[i].Name;
            var location = map_data[i].Location;
            var selfIcon = L.divIcon({
                className: 'my-div-icon',
                iconSize: [50, 50],
                html: '<img  class="circle_img" src="' + map_data[i].Picture + '" style="border: 3px solid ' + map_data[i].Color + '" />'
            });
            var marker = L.marker(new L.LatLng(map_data[i].Latitude, map_data[i].Longitude), {
                title: title,
                icon: selfIcon
            }).setBouncingOptions({
                bounceHeight: 15,
                exclusive: true
            }).on('click', function () {
                this.bounce(2);
            }).addTo(markers);

            var content = title + "</br>" + "Location:" + map_data[i].Location + "</br>" +"Latitude:" + map_data[i].Latitude + "</br>" + "Longitude:" + map_data[i].Longitude;
            marker.bindPopup(content, {
                maxWidth: 600
            });
            markers.addLayer(marker);
            markerList.push(marker);
            if (map_data[i].Color === "#de2d26") {
                markers1.addLayer(marker);
            }
            if (map_data[i].Color === "#000000") {
                markers2.addLayer(marker);
            }
            if (map_data[i].Color === "#377eb8") {
                markers3.addLayer(marker);
            }
            if (map_data[i].Color === "#4daf4a") {
                markers4.addLayer(marker);
            }
            if (map_data[i].Color === "#984ea3") {
                markers5.addLayer(marker);
            }
            if (map_data[i].Color === "#fc8d59") {
                markers6.addLayer(marker);
            }
            if (map_data[i].Color === "#A0522D") {
                markers7.addLayer(marker);
            }
            if (map_data[i].Color === "#E4D03B") {
                markers8.addLayer(marker);
            }
        }
        controlSearch.on('search:locationfound', function (e) {
            if (e.layer._popup) {
                var index = markerList.map(function (e) {
                    return e.options.title;
                }).indexOf(e.text);
                var m = markerList[index];
                markers.zoomToShowLayer(m, function () {
                    m.openPopup();
                    m.bounce(2);
                });
            }
        });
        map.addControl(controlSearch);
        // map.addLayer(markers);
        // map.addLayer(markers1);
        // var all =L.layerGroup();
        // markers.addTo(all);
        // var groupedOverlays = {
        //         "Total": all,
        //         "Total1": all1,
        //
        //
        // };
//         var options = {
//         // Make the "Landmarks" group exclusive (use radio inputs)
//         exclusiveGroups: ["All"],
//         // Show a checkbox next to non-exclusive group labels for toggling all
//         groupCheckboxes: true
// };
        markers.addTo(markers);
        // L.control.layers(baseMaps,groupedOverlays,options).addTo(map);
        // var layerControl = L.control.groupedLayers(baseMaps, groupedOverlays, options);
        // map.addControl(layerControl);
        // map.addLayer(markers);
        //mini map
        lc = L.control.locate({
            position: 'topright',
            strings: {
                title: "Show me where I am, yo!",
                popup: "You are here"
            },
            drawCircle: true,
            showPopup: true
        }).addTo(map);


    },
});
 // Add our zoom control manually where we want to
var zoomControl = L.control.zoom({
    position: 'topright'
});
map.addControl(zoomControl);

// Add our loading control in the same position and pass the
// zoom control to attach to it
var loadingControl = L.Control.loading({
    position: 'topright',
    zoomControl: zoomControl
});
map.addControl(loadingControl);

function getColor(d) {
        return d === 'Spicy'  ? "#de2d26" :
               d === 'Halal' ? "#000000":
               d === 'Vegertarian'  ? "#377eb8" :
               d === 'Healthy' ? "#4daf4a" :
               d === 'Elder friendly' ? "#984ea3" :
               d === 'Desert' ? "#fc8d59":
               d === 'Hawker' ? "#A0522D":
                   "#E4D03B";

    }

    function style(feature) {
        return {
            weight: 1.5,
            opacity: 1,
            fillOpacity: 1,
            radius: 6,
            fillColor: getColor(feature.properties.TypeOfIssue),
            color: "grey"

        };
    }

var legend = L.control({position: 'bottomright'});
    legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend');
    labels = ['<strong>Legend</strong>'];
    categories = ['Spicy','Halal','Vegertarian','Healthy','Elder friendly','Desert','Hawker','Cafes'];

    for (var i = 0; i < categories.length; i++) {

            div.innerHTML +=
            labels.push(
                '<i class="circle" style="background:' + getColor(categories[i]) + '"></i> ' +
            (categories[i] ? categories[i] : '+'));

        }
        div.innerHTML = labels.join('<br>');
    return div;
    };
    legend.addTo(map);
