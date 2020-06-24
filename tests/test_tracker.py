import json
import pytest

from simple_tracker import Tracker


test_data = [
    [(10, 0), (50, 0)],
    [(10, 5), (50, 10)]
]


def test_update():
    tracker = Tracker(max_distance=5, timeout=2)
    tracker.update(test_data[0])
    assert tracker.points == {0: (10, 0, 0, 0), 1: (50, 0, 0, 0)}
    tracker.update(test_data[1])
    assert tracker.points == {
        0: (10, 5, 5, 1), 1: (50, 0, 0, 0), 2: (50, 10, 0, 1)}
    assert tracker.update([(10, 10), (50, 10)]) == [
        {'id': 1, 'x': 50, 'y': 0, 'distance': 0, 'last_frame': 0}]
    assert tracker.points == {0: (10, 10, 10.0, 2), 2: (50, 10, 0.0, 2)}
    tracker.update([])



def test_real_data():
    with open('tests/data/data.json', 'r') as file:
        data = json.load(file)
    tracker = Tracker(max_distance=data['tracker']['max_distance'],
                      timeout=data['tracker']['timeout'])
    tracker.frame = data['data'][0]['frame']
    
    def tracking_found_cb(point):
        return (
            point[1] < 140 or
            tracker.frame == 0
        )

    def tracking_lost_cb(point):
        return (
            point['y'] >= 140 and
            point['distance'] >= 30
        )

    for frame in data['data']:
        tracker.update(frame['test_data'], tracking_found_cb=tracking_found_cb,
                       tracking_lost_cb=tracking_lost_cb)
        
        points = [int(k) for k in frame['assertations'].keys()]
        assert sorted(tracker.points.keys()) == sorted(points)
    
