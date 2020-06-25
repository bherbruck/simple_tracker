import sensor
import image
import time

from simple_tracker import Tracker


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
clock = time.clock()

orange_threshold = [(23, 79, 19, 54, 4, 57)]
green_threshold = [(10, 100, -67, -23, 2, 54)]
tracker = Tracker(max_distance=50)


def main():
    while(True):
        clock.tick()
        img = sensor.snapshot()
        find_blobs(img)
        print(clock.fps())


def find_blobs(img):
    blobs = img.find_blobs(green_threshold)
    tracker.update([(blob.cx(), blob.cy()) for blob in blobs])
    for blob in blobs:
        img.draw_rectangle(blob.rect())
    for id, point in tracker.points.items():
        img.draw_string(point[0], point[1], str(id), scale=2)


main()














