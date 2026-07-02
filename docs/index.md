# 🗓️ The Ultimate Dolomites 2026 Itinerary


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

<div id="dolomites-map" style="height: 350px; width: 100%; border-radius: 8px; border: 1px solid #ccc; z-index: 1; margin-bottom: 20px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('dolomites-map').setView([46.55, 11.9], 10);
    L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        maxZoom: 17,
        attribution: '© OpenStreetMap contributors | Map style: © OpenTopoMap'
    }).addTo(map);
    Papa.parse('/assets/data/my_maps_import.csv', {
        download: true,
        header: true,
        complete: function(results) {
            var bounds = [];
            var excludedDays = ["Day 1", "Day 12-14", "Day 14-16", "Day 15"];
            results.data.forEach(function(row) {
                if (row.Lat && row.Lng && !excludedDays.includes(row.Day)) {
                    var lat = parseFloat(row.Lat);
                    var lng = parseFloat(row.Lng);
                    if (!isNaN(lat) && !isNaN(lng)) {
                        var markerColor = "blue";
                        if (row.Category === "Base") markerColor = "red";
                        if (row.Category === "Hike") markerColor = "green";
                        if (row.Category === "Activity") markerColor = "orange";
                        var customIcon = L.divIcon({
                            className: 'custom-icon',
                            html: `<div style="background-color: ${markerColor}; width: 12px; height: 12px; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 4px rgba(0,0,0,0.5);"></div>`,
                            iconSize: [12, 12],
                            iconAnchor: [6, 6]
                        });
                        var marker = L.marker([lat, lng], {icon: customIcon}).addTo(map);
                        marker.bindPopup(`<b>${row.Name}</b><br>${row.Category} | ${row.Day}`);
                        bounds.push([lat, lng]);
                    }
                }
            });
            if(bounds.length > 0) map.fitBounds(bounds, {padding: [10, 10]});
        }
    });
});
</script>

**📋 Immediate To-Dos (See the full [To-Do List](todo.md) & [Logistics](logistics.md))**:
- Book remaining outbound flights (Sunny & Kevin He)
- Book all inbound flights (Venice → Madrid)
- Book 3 Hotel Bases (Venice, Val Gardena, Cortina)
*(Note: Rental Car and ANYMA Concert are successfully booked!)*

---

### 🛬 Venice Arrival (Base: Mestre)
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 1**](day1_venice_val_gardena_arrival.md) | Arrival at VCE, settle in Mestre, optional cicchetti | ~4 hrs | ⭐ |

### ⛰️ Western Dolomites (Base: Val Gardena)
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 2**](day2_ortisei_acclimatization.md) | Pick up rental car, drive to Ortisei, explore town | ~5 hrs | ⭐⭐ |
| [**Day 3**](day3_val_di_funes.md) | Hike Adolf Munkel Weg, Santa Maddalena viewpoints | ~7 hrs | ⭐⭐⭐ |
| [**Day 4**](day4_alpe_di_siusi.md) | E-biking Alpe di Siusi plateau, Castelrotto village | ~8 hrs | ⭐⭐⭐⭐ |
| [**Day 5**](day5_seceda_ridge.md) | Seceda cable car, hike the postcard ridge | ~6 hrs | ⭐⭐⭐ |
| [**Day 6**](day6_west_split.md) | Gran Cir Via Ferrata (Thrill) OR Town/Spa (Relax) | ~8 hrs | ⭐⭐⭐⭐⭐ *(or ⭐)* |

### 🚗 The Epic Transit Day
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 7**](day7_val_gardena_cortina_transit.md) | Drive Sella Pass, Marmolada cable car, Lagazuoi tunnels | ~9 hrs | ⭐⭐ |

### 🏔️ Eastern Dolomites (Base: Cortina d'Ampezzo)
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 8**](day8_cinque_torri_passo_giau.md) | Cinque Torri WWI loop, Passo Giau sunset | ~7 hrs | ⭐⭐⭐ |
| [**Day 9**](day9_tre_cime_cadini.md) | Tre Cime di Lavaredo loop, Cadini di Misurina | ~8 hrs | ⭐⭐⭐⭐ |
| [**Day 10**](day10_east_split.md) | Alpini Via Ferrata (Thrill) OR Lago di Misurina (Relax) | ~8 hrs | ⭐⭐⭐⭐⭐ *(or ⭐)* |
| [**Day 11**](day11_lago_di_sorapis.md) | Hike to glacial Lago di Sorapis | ~7 hrs | ⭐⭐⭐⭐⭐ |

### 🛶 Venice Return (Base: Venice Island)
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 12**](day12_venice_arrival.md) | Drop car in Mestre, water taxi to Island, wandering | ~5 hrs | ⭐ |
| [**Day 13**](day13_venice_full_day.md) | St. Mark's Basilica, Doge's Palace, Rialto Bridge | ~8 hrs | ⭐⭐ |

### 🇪🇸 Madrid & Departure (Base: Madrid)
| Day | Core Activities | Est. Time Out | Intensity |
|-----|-----------------|---------------|-----------|
| [**Day 14**](day14_venice_madrid_transit.md) | Flight to MAD, Royal Palace, San Miguel Market | ~6 hrs | ⭐ |
| [**Day 15**](day15_madrid_anyma.md) | Rest morning, ANYMA presents ÆDEN Concert | ~6 hrs | ⭐⭐ |
| [**Day 16**](day16_madrid_toronto_departure.md) | Final breakfast, fly home to YYZ | ~3 hrs | 0 (Rest) |
