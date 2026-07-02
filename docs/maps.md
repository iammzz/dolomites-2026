# 🗺️ Maps & Routing

To make navigation on the ground as easy as possible, here are click-to-open Google Maps routing links for all of your major driving days. You can open these directly on your phone when you get in the rental car.

---

## 🚗 Daily Driving Routes

### [Day 2: Mestre to Val Gardena](https://www.google.com/maps/dir/Venezia+Mestre/Ortisei,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/)
* **Route**: Venice Mestre Station $\rightarrow$ Ortisei
* **Drive Time**: ~3 hours

### [Day 3: Val di Funes](https://www.google.com/maps/dir/Ortisei,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/Zanser+Alm,+Funes,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/Santa+Maddalena,+Funes,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/Ortisei,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/)
* **Route**: Ortisei $\rightarrow$ Zanser Alm (Parking) $\rightarrow$ Santa Maddalena $\rightarrow$ Ortisei
* **Drive Time**: ~50 mins each way

### [Day 7: The Epic Transit Day](https://www.google.com/maps/dir/Ortisei,+Autonomous+Province+of+Bolzano+-+South+Tyrol,+Italy/Passo+Sella/Malga+Ciapela/Passo+Falzarego/Cortina+d'Ampezzo,+Belluno,+Italy/)
* **Route**: Ortisei $\rightarrow$ Passo Sella $\rightarrow$ Malga Ciapela (Marmolada) $\rightarrow$ Passo Falzarego (Lagazuoi) $\rightarrow$ Cortina d'Ampezzo
* **Drive Time**: ~2.5 to 3 hours total driving (split up by cable car stops)

### [Day 8: Cinque Torri & Passo Giau](https://www.google.com/maps/dir/Cortina+d'Ampezzo/Baita+Bai+de+Dones/Passo+Giau/Cortina+d'Ampezzo/)
* **Route**: Cortina $\rightarrow$ Baita Bai de Dones (Cinque Torri chairlift) $\rightarrow$ Passo Giau $\rightarrow$ Cortina
* **Drive Time**: ~25 mins to Cinque Torri, ~20 mins to Passo Giau, ~30 mins back to Cortina.

### [Day 9: Tre Cime di Lavaredo](https://www.google.com/maps/dir/Cortina+d'Ampezzo/Rifugio+Auronzo/)
* **Route**: Cortina $\rightarrow$ Rifugio Auronzo (Toll Road Parking)
* **Drive Time**: ~45 mins each way

### [Day 11: Lago di Sorapis](https://www.google.com/maps/dir/Cortina+d'Ampezzo/Passo+Tre+Croci/)
* **Route**: Cortina $\rightarrow$ Passo Tre Croci (Trailhead)
* **Drive Time**: ~15 mins each way

### [Day 12: Return to Venice](https://www.google.com/maps/dir/Cortina+d'Ampezzo/Venezia+Mestre/)
* **Route**: Cortina $\rightarrow$ Venice Mestre Station (Car Drop-off)
* **Drive Time**: ~2 hours

---

## 🌍 Interactive Trip Map
*This map automatically syncs with the itinerary data repository!*

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

<div id="map" style="height: 600px; width: 100%; border-radius: 8px; border: 1px solid #ccc; z-index: 1;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initialize the map, centered roughly on the Dolomites
    var map = L.map('map').setView([46.4, 11.8], 9);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Fetch and parse the CSV
    Papa.parse('/assets/data/my_maps_import.csv', {
        download: true,
        header: true,
        complete: function(results) {
            var bounds = [];
            results.data.forEach(function(row) {
                if (row.Lat && row.Lng) {
                    var lat = parseFloat(row.Lat);
                    var lng = parseFloat(row.Lng);
                    
                    if (!isNaN(lat) && !isNaN(lng)) {
                        var marker = L.marker([lat, lng]).addTo(map);
                        
                        // Create popup content
                        var popupContent = `
                            <div style="font-family: sans-serif;">
                                <h3 style="margin-bottom: 5px; color: #333;">${row.Name}</h3>
                                <strong>${row.Day}</strong><br>
                                <span style="color: #666;">${row.Description}</span>
                            </div>
                        `;
                        marker.bindPopup(popupContent);
                        bounds.push([lat, lng]);
                    }
                }
            });
            // Automatically fit the map to show all pins (excluding Madrid to not zoom out too far)
            var italyBounds = bounds.filter(b => b[1] > 0); 
            if(italyBounds.length > 0) {
                map.fitBounds(italyBounds, {padding: [50, 50]});
            }
        }
    });
});
</script>
