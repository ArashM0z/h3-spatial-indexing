"""H3 cell aggregator: roll point events up into hexagon cells."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

import h3


@dataclass
class CellAgg:
    cell: str
    count: int
    sum_value: float
    centre_lat: float
    centre_lon: float


def aggregate_points(
    points: Iterable[tuple[float, float, float]],
    resolution: int = 9,
) -> list[CellAgg]:
    """Aggregate (lat, lon, value) triples into H3 cells."""
    counts: dict[str, int] = defaultdict(int)
    sums: dict[str, float] = defaultdict(float)
    for lat, lon, value in points:
        cell = h3.latlng_to_cell(lat, lon, resolution)
        counts[cell] += 1
        sums[cell] += value
    out: list[CellAgg] = []
    for cell, n in counts.items():
        c_lat, c_lon = h3.cell_to_latlng(cell)
        out.append(CellAgg(cell=cell, count=n, sum_value=sums[cell],
                           centre_lat=c_lat, centre_lon=c_lon))
    return sorted(out, key=lambda c: c.count, reverse=True)


def neighbours(cell: str, k: int = 1) -> set[str]:
    return set(h3.grid_disk(cell, k))


def polygon_to_cells(geojson_polygon: dict, resolution: int = 9) -> set[str]:
    return set(h3.polygon_to_cells(geojson_polygon, resolution))
