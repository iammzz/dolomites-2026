---
name: Review Sync
description: Triggers when the user asks to review, audit, verify, or check that all trip planning files (itinerary, todo, logistics, index, maps, packing list) are fully synchronized and aligned.
---

# Review Sync: Trip Planning Alignment Audit

When this skill is triggered, you must perform a comprehensive synchronization audit across all planning documentation files to ensure no day, booking, gear item, or map pin has fallen out of alignment.

Follow this exact audit checklist:

## 🔍 Alignment Checklist

1. **Daily Detail vs. Master Welcome (docs/index.md)**:
   * Verify that every day number (Day 1 to Day 16), date, activity overview, and base town listed in the master overview table in [index.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/index.md) matches the corresponding daily itinerary file exactly.

2. **Daily Detail vs. Logistics (docs/logistics.md)**:
   * Cross-reference accommodation bases. Ensure that the check-in and check-out dates and base towns listed in [logistics.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/logistics.md) correspond to the base towns and check-in/out schedules in the daily detail files.
   * Verify that flight arrival and transit details (e.g., flight times and VCE/MAD airport departures) match the timelines in Day 1, Day 12, Day 14, and Day 16.

3. **Logistics vs. Checklist (docs/todo.md)**:
   * Verify that the booking status indicator (Green/Yellow/Red) in [logistics.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/logistics.md) matches the checkmark status ([x] or [ ]) in the active to-do list and the completed bookings section of [todo.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/todo.md).
   * Update the danger status banner at the top of [todo.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/todo.md) and [index.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/index.md) if any bookings have changed status.

4. **Itineraries vs. Packing List (docs/packing_list.md)**:
   * Scan all daily itineraries for specialty equipment (e.g., via ferrata harnesses, helmets, lanyards, trekking poles, headlamps, cold weather layers, cash requirements).
   * Verify that these items are present in [packing_list.md](file:///c:/Users/Matt/Projects/dolomites_2026/docs/packing_list.md). Add any missing items.

5. **Itineraries vs. Map Database (docs/assets/data/my_maps_import.csv)**:
   * Extract all base locations, hiking trailheads, and activity locations from the daily itineraries.
   * Verify that they are represented in the CSV with correct names, categories, and coordinates.

## 📋 Reporting Format

After completing the audit, output your findings in a clear markdown table:

| Document / Area | Audit Check | Status | Action Required / Notes |
|---|---|---|---|
| Index vs. Daily Detail | Check dates, bases, and overview activities | Align / Out of sync | [Details of mismatches or confirmation] |
| Logistics vs. Daily Timeline | Check check-in/out dates and airport times | Align / Out of sync | [Details] |
| To-Do vs. Booking Status | Check checkboxes match logistics status | Align / Out of sync | [Details] |
| Gear Scanning vs. Packing List | Check all specialty gear is on the list | Align / Out of sync | [Details] |
| CSV Database vs. Itinerary | Check all coordinates match stops | Align / Out of sync | [Details] |

*If any mismatches are found, propose the exact changes required to sync them, ask the user for confirmation, and update them.*
