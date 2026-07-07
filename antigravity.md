# 🏔️ Trip Planning & Website Deployment: Antigravity Master Blueprint

This document serves as a complete, reusable blueprint for planning trips, building interactive travel websites, and deploying them to GitHub Pages using the Antigravity IDE workflow. You can copy this file into any future planning repository to establish the exact same structure and workflow.

---

## 🏗️ 1. Repository Architecture & Layout

An Antigravity trip planning project is structured as a static website using **MkDocs** with the **Material Theme**. 

```
├── .agents/
│   └── AGENTS.md               # Custom agent rules & styling enforcement
├── .github/
│   └── workflows/
│       └── main.yml            # CI/CD deployment workflow (GitHub Pages)
├── docs/
│   ├── assets/
│   │   ├── data/
│   │   │   └── my_maps_import.csv # Map pins database (Lat, Lng, Day, Category)
│   │   └── images/             # Static map graphics or photos
│   ├── day1_*.md               # Daily detailed itineraries
│   ├── index.md                # Site welcome page & overview table
│   ├── logistics.md            # Flight/Hotel/Car bookings status & information
│   ├── maps.md                 # Interactive Leaflet maps routing page
│   ├── potential_activities.md # Dropped/back-pocket activities vault
│   └── todo.md                 # Checked-off phase list & completed bookings
├── CNAME                       # GitHub Pages custom domain configuration
└── mkdocs.yml                  # Site navigation, layout, & markdown extensions
```

### 🗺️ Dynamic Leaflet.js Map Integration
The maps page (`docs/maps.md`) and index page (`docs/index.md`) feature interactive map integrations powered by **Leaflet.js** and **PapaParse**. This setup reads coordinates directly from `docs/assets/data/my_maps_import.csv`, meaning you only need to update the CSV to add pins to the maps:

* **Leaflet Setup**:
  ```html
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
  ```
* **Map Rendering script**:
  ```javascript
  L.map('map').setView([lat, lng], zoom);
  // Parse CSV and draw markers based on Category (Base/Hike/Activity)
  ```

---

## 🧳 2. Logistics & Privacy-First Tracking

To keep planning organized while keeping personal details secure on the public web:

1. **Booking Phases**: Group all to-dos into time-sensitive stages:
   * **Phase 1: Book ASAP** (Flights, Rental Car, Hotel Bases).
   * **Phase 2: Book 2-3 Months Out** (IDP, E-Bike rentals, Spas, key restaurant reservations).
   * **Phase 3: Book 30 Days Out** (Strict permit/parking windows like Tre Cime or Lago di Braies).
   * **Phase 4: Book 1 Week Out / On Arrival** (Cable car tickets, gear rentals, cash).
2. **Privacy Enforcement**: Never push sensitive booking data to the repository. Follow these conventions:
   * **Booking References**: Replace actual PNR codes (e.g., `KLEQPK`, `T4P9FG`) with `Confirmed` or `Confirmed (Matthew, Emma, etc.)`.
   * **Costs & Cards**: Completely omit transaction totals, cleaning fees, and card numbers (e.g., `Visa ending in 9196`). Use `Paid` or omit the cost lines.
   * **Completed bookings**: Move booked items into a `<details>` fold-out section at the bottom of `docs/todo.md` to keep the active section uncluttered.

---

## 🤖 3. Custom Agent Rules (`.agents/AGENTS.md`)

Equip the project with a workspace-scoped rules file in `.agents/AGENTS.md`. Antigravity will automatically discover and enforce these style guidelines:

* **Logistics Auto-Sync**: Whenever a change is made to an itinerary, the agent must automatically cross-check and synchronize `index.md`, `todo.md`, `logistics.md`, and the daily itinerary pages.
* **Dining Enforcements**: Every daily itinerary page (where location changes) must have a `"🍽️ Dining & Restaurant Options"` section at the bottom featuring 5–6 curated choices with: Drive distance, Food type, Typical price, Google Maps link, and recommendation details.
* **Deep Activity Research**: Activity descriptions must avoid generic placeholders and provide granular times (physical effort vs. lounging), trailhead parking fees, access restrictions, and direct URLs to specific guides (AllTrails or blog posts).
* **Auto-Push Policy**: Stage, commit, and push modifications to remote repository branches immediately to maintain live website builds without requiring separate prompts.

---

## 🔄 4. Step-by-Step Planning Workflow

1. **Step 1: Raw Schedule Skeleton**: Write down the date, day of week, base town, and draft activity in `sheet.csv` or a central table.
2. **Step 2: Initialize Docs**: Set up `mkdocs.yml` navigation and create daily markdown files (e.g., `docs/day1_*.md`).
3. **Step 3: Define Logistics & Checklists**: Populate `docs/logistics.md` and `docs/todo.md` with flights, accommodation requirements, and bookings checklist.
4. **Step 4: Draft Day Details**: Ask Antigravity to build detailed files for each day. Guide the agent to include:
   * Hour-by-hour schedules.
   * Drive times/distances (Google Maps link routes).
   * Detailed trail stats (km, elevation, difficulty).
5. **Step 5: Map Coordinates**: Extract latitudes and longitudes for each major stop and save them to `docs/assets/data/my_maps_import.csv` to populate the Leaflet map.
6. **Step 6: Build & Test Links**: Run the link-checker python script to resolve any broken URLs.

---

## 🛠️ 5. Development & Deployment

### Local Development
1. Install Python dependencies:
   ```bash
   pip install mkdocs mkdocs-material
   ```
2. Run the local dev server:
   ```bash
   mkdocs serve
   ```
3. Open `http://127.0.0.1:8000` in your browser to preview changes in real time.

### CI/CD Deployment to GitHub Pages
Any changes pushed to the `main` branch will automatically build and deploy the static site to the `gh-pages` branch using GitHub Actions (`.github/workflows/main.yml`):
```yaml
name: Deploy MkDocs
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```

*(Note: Ensure that GitHub Pages is set to deploy from the `gh-pages` branch in the settings of your repository on GitHub).*
