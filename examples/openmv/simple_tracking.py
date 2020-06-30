import sensor
import image
import time
import json

from simple_tracker import Tracker


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

green_threshold = [(44, 88, -50, 18, 9, 66)]
tracker = Tracker(max_distance=50)
record = True
tracker_file = 'tracker.txt'
data_file = 'data.txt'

def main():
    if record:
        data = {'tracker': {'max_distance': tracker.max_distance,
                            'timeout': tracker.timeout}}
        write_file(tracker_file, data)
        write_file(data_file, '')

    while(True):
        clock.tick()
        img = sensor.snapshot()
        find_blobs(img)
        print(clock.fps())


def find_blobs(img):
    blobs = img.find_blobs(green_threshold, pixels_threshold=500)
    centroids = [(blob.cx(), blob.cy()) for blob in blobs]
    lost_tracking = tracker.update(centroids)
    for blob in blobs:
        img.draw_rectangle(blob.rect())
    for id, point in tracker.points.items():
        img.draw_string(point[0], point[1], str(id), scale=2)

    if record:
        # ujson isn't the best... so record like this
        data = {
            'frame': tracker.frame,
            'test_data': centroids,
            'assertations': tracker.points,
            'counts': lost_tracking
        }
        append_file(data_file, data)


def write_file(path, data):
    with open(path, 'w') as file:
        file.write(str(data))

def append_file(path, data):
    with open(path, 'a') as file:
        file.write(str(data) + ',\n')


main()














