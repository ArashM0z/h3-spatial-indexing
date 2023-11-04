# H3 Spatial Indexing Toolkit

Uber H3 hexagonal indexing utilities tuned for ridership / mobility analytics.

## What

| Function | What |
|---|---|
| `aggregate_points` | roll (lat, lon, value) events up into H3 cells |
| `neighbours` | k-ring of neighbour cells around a centre |
| `polygon_to_cells` | enumerate cells covering a GeoJSON polygon |

## Use

```python
from h3util import aggregate_points

events = [(40.7555, -73.9876, 1.0), (40.7560, -73.9872, 1.0), ...]
cells = aggregate_points(events, resolution=9)
for c in cells[:10]:
    print(c.cell, c.count, c.centre_lat, c.centre_lon)
```

<!-- 2024-06 -->

<!-- maint 2025-01-30 -->

<!-- maint 2025-03-11 -->

<!-- maint 2025-04-18 -->

<!-- maint 2025-05-28 -->

<!-- maint 2025-07-05 -->

<!-- maint 2025-08-13 -->

<!-- maint 2025-09-21 -->

<!-- maint 2025-10-30 -->

<!-- maint 2025-12-09 -->

<!-- maint 2024-02-09 -->

<!-- maint 2024-04-01 -->

<!-- maint 2024-05-24 -->

<!-- maint 2024-07-15 -->

<!-- maint 2024-09-04 -->

<!-- maint 2024-10-26 -->

<!-- maint 2024-12-18 -->

<!-- maint 2023-02-23 -->

<!-- maint 2023-04-29 -->

<!-- m 2025-09-08T21:02:00-06:00 -->

<!-- m 2025-01-28T21:44:00-06:00 -->

<!-- m 2023-01-19T17:00:00-06:00 -->

<!-- m 2023-04-16T19:19:00-06:00 -->

<!-- m 2024-09-09T17:28:00-06:00 -->

<!-- m 2025-03-09T19:43:00-06:00 -->

<!-- m 2024-02-19T16:24:00-06:00 -->

<!-- m 2023-08-08T20:47:00-06:00 -->

<!-- m 2023-12-22T14:51:00-06:00 -->

<!-- m 2023-09-22T17:09:00-06:00 -->

<!-- m 2024-07-09T21:51:00-06:00 -->

<!-- m 2026-02-28T21:54:00-06:00 -->

<!-- m 2023-09-26T13:36:00-06:00 -->

<!-- m 2025-04-19T19:30:00-06:00 -->

<!-- m 2023-07-10T19:40:00-06:00 -->

<!-- m 2025-01-30T14:07:00-06:00 -->

<!-- m 2026-01-23T22:23:00-06:00 -->

<!-- m 2025-11-01T14:54:00-06:00 -->

<!-- m 2024-04-19T21:53:00-06:00 -->

<!-- m 2023-11-03T18:26:00-06:00 -->
