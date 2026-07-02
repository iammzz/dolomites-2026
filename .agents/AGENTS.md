# Agent Behavioral Rules

*   When a user marks tasks as done or provides evidence of completed tasks (like receipts), always cross-check against the project's to-do list (`docs/todo.md` and/or `TODO.md`) and automatically update it to reflect the completion status.
*   When new logistics or bookings (like car rentals, flights, or activities) are provided, do not just update the logistics summary. Always identify the relevant daily itinerary files (e.g., `docs/dayX_*.md`) and recalibrate the timeline, start times, and events for those days to match the exact booking details.
*   Whenever a change is made to the itinerary (e.g., adding a new leg or shifting days), ensure that the overarching documentation files (`docs/index.md`, `docs/todo.md`, `docs/logistics.md`, `docs/potential_activities.md`, `questions.md`, and the daily activities files) are all kept in sync.
