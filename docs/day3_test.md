# Day 3 — Monday, Sept 14 🏔️
## Val di Funes & The Geisler Peaks
**Base:** Val Gardena (Ortisei/Selva)


---

## ✅ Main Activity: The Iconic Postcard Valley

**Expectation & Rationale:** 
Val di Funes is arguably the most picturesque valley in the entire Dolomites. This is where you get the famous views of the jagged Geisler/Odle peaks rising vertically behind rolling green pastures and tiny chapels. You will hike the Adolf Munkel Weg, which takes you directly to the base of the massive rock walls, before visiting the viewpoints that made this region famous. 

### 1. Adolf Munkel Weg (Adolf Munkel Trail)
* **Distance**: 9.2 km loop
* **Elevation Change**: ~400m
* **Difficulty**: ⭐⭐ Moderate
* **Duration**: 3–4 hrs
* **Extensions**: Stop at Geisler Alm (Rifugio delle Odle) for lunch — an absolute must.
* **Resources**: 
  * [Earth Trekkers: Adolf Munkel Weg](https://www.google.com/search?q=site:earthtrekkers.com+adolf+munkel+weg+hike+val+di+funes)
  * [AllTrails: Adolf Munkel Trail](https://www.alltrails.com/search?q=adolf%20munkel%20weg%20rifugio%20delle%20odle)
* **Notes**: The trail starts in the forest and emerges right at the foot of the dramatic north faces of the Geisler group. Geisler Alm is widely considered one of the best rifugios in the Dolomites for food and atmosphere.

### 2. Santa Maddalena Viewpoints (The Postcard Shots)
* **Distance**: Short walks from parking areas
* **Elevation Change**: Minimal
* **Difficulty**: ⭐ Easy
* **Duration**: 1 hour total
* **Resources**: [Earth Trekkers: Val di Funes](https://www.google.com/search?q=site:earthtrekkers.com+best+things+to+do+val+di+funes)
* **Notes**: There are two main photo spots: the Church of St. John (San Giovanni in Ranui) and the Santa Maddalena viewpoint. They are heavily photographed for a reason!

---

## 📌 Logistics & Drive Breakdown

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

<div id="day3-map" style="height: 400px; width: 100%; border-radius: 8px; border: 1px solid #ccc; z-index: 1;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('day3-map').setView([46.6, 11.7], 11);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Day 3 Route Coordinates
    var routePoints = [
        [46.5734, 11.6742], // Ortisei
        [46.6358, 11.7671], // Zanser Alm
        [46.6433, 11.7167], // Santa Maddalena
        [46.5734, 11.6742]  // Back to Ortisei
    ];

    // Draw the route line
    var polyline = L.polyline(routePoints, {color: '#ff5722', weight: 4, opacity: 0.8}).addTo(map);

    // Add Markers
    L.marker([46.5734, 11.6742]).addTo(map).bindPopup("<b>Ortisei</b><br>Start & End");
    L.marker([46.6358, 11.7671]).addTo(map).bindPopup("<b>Zanser Alm</b><br>Hike Trailhead");
    L.marker([46.6433, 11.7167]).addTo(map).bindPopup("<b>Santa Maddalena</b><br>Photo Viewpoint");

    // Fit map to route
    map.fitBounds(polyline.getBounds(), {padding: [30, 30]});
});
</script>

| # | From | To | Distance | Drive Time | Road | Notes |
|---|------|----|----------|------------|------|-------|
| 1 | Ortisei | Zanser Alm (Malga Zannes) | 33 km | ~50 min | SS242, SP163, SP162 | Zanser Alm is the trailhead for the hike. |
| 2 | Zanser Alm | Santa Maddalena | 7 km | ~15 min | SP162 | Short drive down into the valley. |
| 3 | Santa Maddalena | Ortisei | 30 km | ~45 min | SP162, SS242 | Return to base. |

### 🕐 Hour-by-Hour Schedule

| Time | Location | Activity | Detail |
|------|----------|----------|--------|
| 8:30 am | Ortisei | 🚗 Depart | Enjoy your first morning in Val Gardena! |
| 9:20 am | Zanser Alm | 🅿️ Park & Pay | Trailhead parking (requires fee). |
| 9:30 am | Zanser Alm | 🥾 Begin Hike | Follow signs for Adolf Munkel Weg (Trail 35). |
| 11:30 am | Geisler Alm | 🍽️ Lunch | Have an early lunch at Geisler Alm to beat the rush. |
| 1:30 pm | Zanser Alm | ✅ Finish Hike | Arrive back at the car. |
| 1:45 pm | Santa Maddalena | 📸 Viewpoints | Drive to the valley town. Walk to the Church of St. John. |
| 3:00 pm | Santa Maddalena | 🚗 Drive Back | Head back to Ortisei. |
| 4:00 pm | Ortisei | 🍷 Explore Town | Walk the pedestrian center of Ortisei. |

### Key Logistics Notes
* **Toll Parking**: The Zanser Alm parking lot costs ~€8 per day. Have cash ready just in case. 
* **Church of St. John (Ranui)**: There is a small turnstile fee (~€4) to walk up to the famous fence for the church photo.
* **Geisler Alm**: Seriously, eat here. It has a massive playground, deck chairs facing the peaks, and incredible Tyrolean food.

---

### 🛑 Optional Drive Stops (Back-Pocket Options)
Since the drive out to Val di Funes takes you out of Val Gardena and into the main Eisacktal (Valle Isarco) valley, you pass by some incredible historic towns. If you finish your hike early or just want to break up the drive, consider these supplements:

* **Chiusa (Klausen)**: Right on the route back to Ortisei. It's officially listed as one of the "Most Beautiful Villages in Italy" (I Borghi più belli d'Italia). It has a stunning medieval center with colorful facades.
* **Sabiona Monastery (Kloster Säben)**: Perched on a massive rock cliff looming over Chiusa. It requires a steep 45-minute walk up from town, but the views are commanding.
* **Bressanone (Brixen)**: About 15 minutes north of the Funes exit. It's the oldest town in South Tyrol, famous for its grand Cathedral (Duomo di Bressanone) and beautiful piazza. Great place for a late afternoon coffee.
