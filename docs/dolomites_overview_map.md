# 🏔️ Dolomites Overview Map

This map filters out the transit cities (Venice & Madrid) to give you a highly focused, interactive overview of every single hike, cable car, and base camp throughout your time in the Dolomites (Days 2–11).

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

<div id="dolomites-map" style="height: 700px; width: 100%; border-radius: 8px; border: 1px solid #ccc; z-index: 1; margin-top: 20px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initialize map centered on the Dolomites
    var map = L.map('dolomites-map').setView([46.55, 11.9], 10);
    
    // Add OpenStreetMap tiles with a slightly more topographical look if possible, or standard OSM
    L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        maxZoom: 17,
        attribution: 'Map data: © OpenStreetMap contributors, SRTM | Map style: © OpenTopoMap'
    }).addTo(map);

    // Fetch and parse the CSV
    Papa.parse('assets/data/my_maps_import.csv', {
        download: true,
        header: true,
        complete: function(results) {
            var bounds = [];
            results.data.forEach(function(row) {
                // Filter: We only want Dolomites points. 
                // A reliable way is to filter by Latitude (Dolomites are ~46.4 to 46.7).
                // Or we can exclude Day 1, 12-16.
                var excludedDays = ["Day 1", "Day 12-14", "Day 14-16", "Day 15"];
                
                if (row.Lat && row.Lng && !excludedDays.includes(row.Day)) {
                    var lat = parseFloat(row.Lat);
                    var lng = parseFloat(row.Lng);
                    
                    if (!isNaN(lat) && !isNaN(lng)) {
                        // Custom Marker Colors based on Category
                        var markerColor = "blue"; // Default
                        if (row.Category === "Base") markerColor = "red";
                        if (row.Category === "Hike") markerColor = "green";
                        if (row.Category === "Activity") markerColor = "orange";
                        
                        var customIcon = L.divIcon({
                            className: 'custom-icon',
                            html: `<div style="background-color: ${markerColor}; width: 16px; height: 16px; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 4px rgba(0,0,0,0.5);"></div>`,
                            iconSize: [16, 16],
                            iconAnchor: [8, 8]
                        });

                        var marker = L.marker([lat, lng], {icon: customIcon}).addTo(map);
                        
                        var popupContent = `
                            <div style="font-family: sans-serif; min-width: 150px;">
                                <h3 style="margin: 0 0 5px 0; color: #333; font-size: 16px;">${row.Name}</h3>
                                <strong style="color: ${markerColor}; text-transform: uppercase; font-size: 11px;">${row.Category}</strong> | <span style="font-size: 12px;">${row.Day}</span><br>
                                <p style="color: #666; font-size: 13px; margin: 5px 0 0 0;">${row.Description}</p>
                            </div>
                        `;
                        marker.bindPopup(popupContent);
                        bounds.push([lat, lng]);
                    }
                }
            });
            
            // Fit bounds to the Dolomites pins
            if(bounds.length > 0) {
                map.fitBounds(bounds, {padding: [40, 40]});
            }
        }
    });
});
</script>
