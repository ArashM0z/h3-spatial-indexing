from h3util.aggregator import aggregate_points, neighbours


def test_aggregate_co_located_points() -> None:
    points = [(40.7555, -73.9876, 1.0)] * 100 + [(40.0, -74.0, 2.0)]
    agg = aggregate_points(points, resolution=9)
    assert len(agg) == 2
    # Larger cell first
    assert agg[0].count == 100


def test_neighbours_nonempty() -> None:
    import h3
    cell = h3.latlng_to_cell(40.7555, -73.9876, 9)
    assert len(neighbours(cell, k=1)) >= 6
