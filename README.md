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
