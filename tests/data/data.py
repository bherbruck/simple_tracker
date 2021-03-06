import json
data = {
    'tracker': {'timeout': 40, 'max_distance': 50},
    'data': [
        {'frame': 1, 'test_data': [(265, 217)], 'assertations': {0: (265, 217, 0, 0)}, 'counts': []},
        {'frame': 2, 'test_data': [(267, 219)], 'assertations': {0: (267, 219, 2.828427, 1)}, 'counts': []},
        {'frame': 3, 'test_data': [(273, 214)], 'assertations': {0: (273, 214, 10.63868, 2)}, 'counts': []},
        {'frame': 4, 'test_data': [(267, 214)], 'assertations': {0: (267, 214, 16.63868, 3)}, 'counts': []},
        {'frame': 5, 'test_data': [(287, 183)], 'assertations': {0: (287, 183, 53.53041, 4)}, 'counts': []},
        {'frame': 6, 'test_data': [(301, 181)], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 7, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 8, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 9, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 10, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 11, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 12, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 13, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 14, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 15, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 16, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 17, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 18, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 19, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 20, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5)}, 'counts': []},
        {'frame': 21, 'test_data': [(39, 186)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (39, 186, 0, 20)}, 'counts': []},
        {'frame': 22, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (39, 186, 0, 20)}, 'counts': []},
        {'frame': 23, 'test_data': [(23, 224)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (23, 224, 41.23106, 22)}, 'counts': []},
        {'frame': 24, 'test_data': [(17, 223)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (17, 223, 47.31382, 23)}, 'counts': []},
        {'frame': 25, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (17, 223, 47.31382, 23)}, 'counts': []},
        {'frame': 26, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (17, 223, 47.31382, 23)}, 'counts': []},
        {'frame': 27, 'test_data': [(10, 195)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (10, 195, 76.17556, 26)}, 'counts': []},
        {'frame': 28, 'test_data': [(16, 205)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (16, 205, 87.83747, 27)}, 'counts': []},
        {'frame': 29, 'test_data': [(19, 220)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (19, 220, 103.1345, 28)}, 'counts': []},
        {'frame': 30, 'test_data': [(18, 218)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (18, 218, 105.3706, 29)}, 'counts': []},
        {'frame': 31, 'test_data': [(16, 215)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (16, 215, 108.9761, 30)}, 'counts': []},
        {'frame': 32, 'test_data': [(12, 206)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 206, 118.825, 31)}, 'counts': []},
        {'frame': 33, 'test_data': [(12, 185)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 34, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 35, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 36, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 37, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 38, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (12, 185, 139.825, 32)}, 'counts': []},
        {'frame': 39, 'test_data': [(5, 213)], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 40, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 41, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 42, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 43, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 44, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 45, 'test_data': [], 'assertations': {0: (301, 181, 67.67255, 5), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 46, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': [{'last_frame': 5, 'id': 0, 'x': 301, 'y': 181, 'distance': 67.67255}]},
        {'frame': 47, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 48, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 49, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 50, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 51, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 52, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 53, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 54, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 55, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 56, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 57, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 58, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 59, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 60, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 61, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 62, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 63, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 64, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 65, 'test_data': [], 'assertations': {1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 66, 'test_data': [(8, 122)], 'assertations': {2: (8, 122, 0, 65), 1: (5, 213, 168.6867, 38)}, 'counts': []},
        {'frame': 67, 'test_data': [(257, 107)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (257, 107, 0, 66)}, 'counts': []},
        {'frame': 68, 'test_data': [(252, 100)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (252, 100, 8.602325, 67)}, 'counts': []},
        {'frame': 69, 'test_data': [(249, 90)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (249, 90, 19.04263, 68)}, 'counts': []},
        {'frame': 70, 'test_data': [(245, 81)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (245, 81, 28.89149, 69)}, 'counts': []},
        {'frame': 71, 'test_data': [(241, 76)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (241, 76, 35.29462, 70)}, 'counts': []},
        {'frame': 72, 'test_data': [(238, 73)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (238, 73, 39.53726, 71)}, 'counts': []},
        {'frame': 73, 'test_data': [(234, 73)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (234, 73, 43.53726, 72)}, 'counts': []},
        {'frame': 74, 'test_data': [(233, 74)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (233, 74, 44.95147, 73)}, 'counts': []},
        {'frame': 75, 'test_data': [(234, 76)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (234, 76, 47.18754, 74)}, 'counts': []},
        {'frame': 76, 'test_data': [(233, 78)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (233, 78, 49.42361, 75)}, 'counts': []},
        {'frame': 77, 'test_data': [(233, 80)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (233, 80, 51.42361, 76)}, 'counts': []},
        {'frame': 78, 'test_data': [(232, 84)], 'assertations': {1: (5, 213, 168.6867, 38), 2: (8, 122, 0, 65), 3: (232, 84, 55.54672, 77)}, 'counts': []},
        {'frame': 79, 'test_data': [(231, 87)], 'assertations': {2: (8, 122, 0, 65), 3: (231, 87, 58.70899, 78)}, 'counts': [{'last_frame': 38, 'id': 1, 'x': 5, 'y': 213, 'distance': 168.6867}]},
        {'frame': 80, 'test_data': [(229, 89)], 'assertations': {2: (8, 122, 0, 65), 3: (229, 89, 61.53742, 79)}, 'counts': []},
        {'frame': 81, 'test_data': [(226, 91)], 'assertations': {2: (8, 122, 0, 65), 3: (226, 91, 65.14297, 80)}, 'counts': []},
        {'frame': 82, 'test_data': [(223, 93)], 'assertations': {2: (8, 122, 0, 65), 3: (223, 93, 68.74852, 81)}, 'counts': []},
        {'frame': 83, 'test_data': [(220, 95)], 'assertations': {2: (8, 122, 0, 65), 3: (220, 95, 72.35407, 82)}, 'counts': []},
        {'frame': 84, 'test_data': [(219, 97)], 'assertations': {2: (8, 122, 0, 65), 3: (219, 97, 74.59014, 83)}, 'counts': []},
        {'frame': 85, 'test_data': [(219, 98)], 'assertations': {2: (8, 122, 0, 65), 3: (219, 98, 75.59014, 84)}, 'counts': []},
        {'frame': 86, 'test_data': [(219, 99)], 'assertations': {2: (8, 122, 0, 65), 3: (219, 99, 76.59014, 85)}, 'counts': []},
        {'frame': 87, 'test_data': [(219, 101)], 'assertations': {2: (8, 122, 0, 65), 3: (219, 101, 78.59014, 86)}, 'counts': []},
        {'frame': 88, 'test_data': [(218, 103)], 'assertations': {2: (8, 122, 0, 65), 3: (218, 103, 80.82622, 87)}, 'counts': []},
        {'frame': 89, 'test_data': [(217, 103)], 'assertations': {2: (8, 122, 0, 65), 3: (217, 103, 81.82621, 88)}, 'counts': []},
        {'frame': 90, 'test_data': [(215, 103)], 'assertations': {2: (8, 122, 0, 65), 3: (215, 103, 83.82621, 89)}, 'counts': []},
        {'frame': 91, 'test_data': [(214, 103)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 103, 84.82621, 90)}, 'counts': []},
        {'frame': 92, 'test_data': [(213, 103)], 'assertations': {2: (8, 122, 0, 65), 3: (213, 103, 85.82622, 91)}, 'counts': []},
        {'frame': 93, 'test_data': [(213, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (213, 104, 86.82621, 92)}, 'counts': []},
        {'frame': 94, 'test_data': [(213, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (213, 104, 86.82621, 93)}, 'counts': []},
        {'frame': 95, 'test_data': [(214, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 104, 87.82621, 94)}, 'counts': []},
        {'frame': 96, 'test_data': [(214, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 104, 87.82621, 95)}, 'counts': []},
        {'frame': 97, 'test_data': [(214, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 104, 87.82621, 96)}, 'counts': []},
        {'frame': 98, 'test_data': [(214, 104)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 104, 87.82621, 97)}, 'counts': []},
        {'frame': 99, 'test_data': [(214, 105)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 105, 88.82621, 98)}, 'counts': []},
        {'frame': 100, 'test_data': [(214, 105)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 105, 88.82621, 99)}, 'counts': []},
        {'frame': 101, 'test_data': [(214, 106)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 106, 89.82621, 100)}, 'counts': []},
        {'frame': 102, 'test_data': [(214, 107)], 'assertations': {2: (8, 122, 0, 65), 3: (214, 107, 90.82622, 101)}, 'counts': []},
        {'frame': 103, 'test_data': [(213, 107)], 'assertations': {2: (8, 122, 0, 65), 3: (213, 107, 91.82621, 102)}, 'counts': []},
        {'frame': 104, 'test_data': [(213, 107)], 'assertations': {2: (8, 122, 0, 65), 3: (213, 107, 91.82621, 103)}, 'counts': []},
        {'frame': 105, 'test_data': [(212, 109)], 'assertations': {2: (8, 122, 0, 65), 3: (212, 109, 94.06228, 104)}, 'counts': []},
        {'frame': 106, 'test_data': [(210, 111)], 'assertations': {3: (210, 111, 96.89071, 105)}, 'counts': [{'last_frame': 65, 'id': 2, 'x': 8, 'y': 122, 'distance': 0}]},
        {'frame': 107, 'test_data': [(209, 111)], 'assertations': {3: (209, 111, 97.89071, 106)}, 'counts': []},
        {'frame': 108, 'test_data': [(207, 112)], 'assertations': {3: (207, 112, 100.1268, 107)}, 'counts': []},
        {'frame': 109, 'test_data': [(206, 112)], 'assertations': {3: (206, 112, 101.1268, 108)}, 'counts': []},
        {'frame': 110, 'test_data': [(204, 112)], 'assertations': {3: (204, 112, 103.1268, 109)}, 'counts': []},
        {'frame': 111, 'test_data': [(202, 113)], 'assertations': {3: (202, 113, 105.3628, 110)}, 'counts': []},
        {'frame': 112, 'test_data': [(201, 114)], 'assertations': {3: (201, 114, 106.7771, 111)}, 'counts': []},
        {'frame': 113, 'test_data': [(201, 114)], 'assertations': {3: (201, 114, 106.7771, 112)}, 'counts': []},
        {'frame': 114, 'test_data': [(202, 114)], 'assertations': {3: (202, 114, 107.7771, 113)}, 'counts': []},
        {'frame': 115, 'test_data': [(202, 113)], 'assertations': {3: (202, 113, 108.7771, 114)}, 'counts': []},
        {'frame': 116, 'test_data': [(202, 113)], 'assertations': {3: (202, 113, 108.7771, 115)}, 'counts': []},
        {'frame': 117, 'test_data': [(202, 112)], 'assertations': {3: (202, 112, 109.7771, 116)}, 'counts': []},
        {'frame': 118, 'test_data': [(202, 113)], 'assertations': {3: (202, 113, 110.7771, 117)}, 'counts': []},
        {'frame': 119, 'test_data': [(203, 113)], 'assertations': {3: (203, 113, 111.7771, 118)}, 'counts': []},
        {'frame': 120, 'test_data': [(203, 114)], 'assertations': {3: (203, 114, 112.7771, 119)}, 'counts': []},
        {'frame': 121, 'test_data': [(203, 114)], 'assertations': {3: (203, 114, 112.7771, 120)}, 'counts': []},
        {'frame': 122, 'test_data': [(204, 113)], 'assertations': {3: (204, 113, 114.1913, 121)}, 'counts': []},
        {'frame': 123, 'test_data': [(205, 113)], 'assertations': {3: (205, 113, 115.1913, 122)}, 'counts': []},
        {'frame': 124, 'test_data': [(206, 114)], 'assertations': {3: (206, 114, 116.6055, 123)}, 'counts': []},
        {'frame': 125, 'test_data': [(207, 114)], 'assertations': {3: (207, 114, 117.6055, 124)}, 'counts': []},
        {'frame': 126, 'test_data': [(207, 115)], 'assertations': {3: (207, 115, 118.6055, 125)}, 'counts': []},
        {'frame': 127, 'test_data': [(208, 115)], 'assertations': {3: (208, 115, 119.6055, 126)}, 'counts': []},
        {'frame': 128, 'test_data': [(208, 115)], 'assertations': {3: (208, 115, 119.6055, 127)}, 'counts': []},
        {'frame': 129, 'test_data': [(208, 115)], 'assertations': {3: (208, 115, 119.6055, 128)}, 'counts': []},
        {'frame': 130, 'test_data': [(208, 115)], 'assertations': {3: (208, 115, 119.6055, 129)}, 'counts': []},
        {'frame': 131, 'test_data': [(207, 115)], 'assertations': {3: (207, 115, 120.6055, 130)}, 'counts': []},
        {'frame': 132, 'test_data': [(207, 114)], 'assertations': {3: (207, 114, 121.6055, 131)}, 'counts': []},
        {'frame': 133, 'test_data': [(206, 112)], 'assertations': {3: (206, 112, 123.8416, 132)}, 'counts': []},
        {'frame': 134, 'test_data': [(205, 111)], 'assertations': {3: (205, 111, 125.2558, 133)}, 'counts': []},
        {'frame': 135, 'test_data': [(204, 110)], 'assertations': {3: (204, 110, 126.67, 134)}, 'counts': []},
        {'frame': 136, 'test_data': [(203, 110)], 'assertations': {3: (203, 110, 127.67, 135)}, 'counts': []},
        {'frame': 137, 'test_data': [(200, 109)], 'assertations': {3: (200, 109, 130.8323, 136)}, 'counts': []},
        {'frame': 138, 'test_data': [(199, 109)], 'assertations': {3: (199, 109, 131.8323, 137)}, 'counts': []},
        {'frame': 139, 'test_data': [(196, 110)], 'assertations': {3: (196, 110, 134.9946, 138)}, 'counts': []},
        {'frame': 140, 'test_data': [(192, 110)], 'assertations': {3: (192, 110, 138.9946, 139)}, 'counts': []},
        {'frame': 141, 'test_data': [(201, 108)], 'assertations': {3: (201, 108, 148.2141, 140)}, 'counts': []},
        {'frame': 142, 'test_data': [(207, 113)], 'assertations': {3: (207, 113, 156.0244, 141)}, 'counts': []},
        {'frame': 143, 'test_data': [(225, 102)], 'assertations': {3: (225, 102, 177.1194, 142)}, 'counts': []},
        {'frame': 144, 'test_data': [(255, 91)], 'assertations': {3: (255, 91, 209.0725, 143)}, 'counts': []},
        {'frame': 145, 'test_data': [(286, 84)], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 146, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 147, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 148, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 149, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 150, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 151, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 152, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 153, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 154, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 155, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 156, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 157, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 158, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 159, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 160, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 161, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 162, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 163, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 164, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 165, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 166, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 167, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 168, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 169, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 170, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 171, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 172, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 173, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 174, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 175, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 176, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 177, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 178, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 179, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 180, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 181, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 182, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 183, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 184, 'test_data': [], 'assertations': {3: (286, 84, 240.853, 144)}, 'counts': []},
        {'frame': 185, 'test_data': [], 'assertations': {}, 'counts': [{'last_frame': 144, 'id': 3, 'x': 286, 'y': 84, 'distance': 240.853}]},
        {'frame': 186, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 187, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 188, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 189, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 190, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 191, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 192, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 193, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 194, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 195, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 196, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 197, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 198, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 199, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 200, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 201, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 202, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 203, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 204, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 205, 'test_data': [], 'assertations': {}, 'counts': []},
        {'frame': 206, 'test_data': [(311, 133)], 'assertations': {4: (311, 133, 0, 205)}, 'counts': []},
        {'frame': 207, 'test_data': [(304, 135)], 'assertations': {4: (304, 135, 7.28011, 206)}, 'counts': []},
        {'frame': 208, 'test_data': [(296, 128)], 'assertations': {4: (296, 128, 17.91026, 207)}, 'counts': []},
        {'frame': 209, 'test_data': [(284, 121)], 'assertations': {4: (284, 121, 31.8027, 208)}, 'counts': []},
        {'frame': 210, 'test_data': [(268, 116)], 'assertations': {4: (268, 116, 48.56575, 209)}, 'counts': []},
        {'frame': 211, 'test_data': [(254, 111)], 'assertations': {4: (254, 111, 63.43183, 210)}, 'counts': []},
        {'frame': 212, 'test_data': [(241, 107)], 'assertations': {4: (241, 107, 77.0333, 211)}, 'counts': []},
        {'frame': 213, 'test_data': [(231, 102)], 'assertations': {4: (231, 102, 88.21364, 212)}, 'counts': []},
        {'frame': 214, 'test_data': [(229, 101)], 'assertations': {4: (229, 101, 90.44971, 213)}, 'counts': []},
        {'frame': 215, 'test_data': [(233, 111)], 'assertations': {4: (233, 111, 101.22, 214)}, 'counts': []},
        {'frame': 216, 'test_data': [(240, 114)], 'assertations': {4: (240, 114, 108.8358, 215)}, 'counts': []},
        {'frame': 217, 'test_data': [(243, 115)], 'assertations': {4: (243, 115, 111.9981, 216)}, 'counts': []},
        {'frame': 218, 'test_data': [(246, 115)], 'assertations': {4: (246, 115, 114.9981, 217)}, 'counts': []},
        {'frame': 219, 'test_data': [(247, 116)], 'assertations': {4: (247, 116, 116.4123, 218)}, 'counts': []},
        {'frame': 220, 'test_data': [(248, 116)], 'assertations': {4: (248, 116, 117.4123, 219)}, 'counts': []},
        {'frame': 221, 'test_data': [(248, 115)], 'assertations': {4: (248, 115, 118.4123, 220)}, 'counts': []},
        {'frame': 222, 'test_data': [(251, 116)], 'assertations': {4: (251, 116, 121.5746, 221)}, 'counts': []},
        {'frame': 223, 'test_data': [(250, 122)], 'assertations': {4: (250, 122, 127.6573, 222)}, 'counts': []},
        {'frame': 224, 'test_data': [(270, 159)], 'assertations': {4: (270, 159, 169.7168, 223)}, 'counts': []},
        {'frame': 225, 'test_data': [(263, 168)], 'assertations': {4: (263, 168, 181.1186, 224)}, 'counts': []},
        {'frame': 226, 'test_data': [(260, 175)], 'assertations': {4: (260, 175, 188.7343, 225)}, 'counts': []},
        {'frame': 227, 'test_data': [(253, 166)], 'assertations': {4: (253, 166, 200.1361, 226)}, 'counts': []},
        {'frame': 228, 'test_data': [(254, 156)], 'assertations': {4: (254, 156, 210.186, 227)}, 'counts': []},
        {'frame': 229, 'test_data': [(251, 154)], 'assertations': {4: (251, 154, 213.7915, 228)}, 'counts': []},
        {'frame': 230, 'test_data': [(245, 158)], 'assertations': {4: (245, 158, 221.0026, 229)}, 'counts': []},
        {'frame': 231, 'test_data': [(230, 149)], 'assertations': {4: (230, 149, 238.4955, 230)}, 'counts': []},
        {'frame': 232, 'test_data': [(218, 141)], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 233, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 234, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 235, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 236, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 237, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 238, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 239, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 240, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 241, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 242, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 243, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 244, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 245, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 246, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 247, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 248, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 249, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 250, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 251, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 252, 'test_data': [], 'assertations': {4: (218, 141, 252.9177, 231)}, 'counts': []},
        {'frame': 253, 'test_data': [(252, 124)], 'assertations': {4: (252, 124, 290.9308, 252)}, 'counts': []},
        {'frame': 254, 'test_data': [(252, 125)], 'assertations': {4: (252, 125, 291.9308, 253)}, 'counts': []},
        {'frame': 255, 'test_data': [(253, 127)], 'assertations': {4: (253, 127, 294.1669, 254)}, 'counts': []},
        {'frame': 256, 'test_data': [(252, 127)], 'assertations': {4: (252, 127, 295.1669, 255)}, 'counts': []},
        {'frame': 257, 'test_data': [(254, 127)], 'assertations': {4: (254, 127, 297.1669, 256)}, 'counts': []},
        {'frame': 258, 'test_data': [(253, 126)], 'assertations': {4: (253, 126, 298.5811, 257)}, 'counts': []},
        {'frame': 259, 'test_data': [], 'assertations': {4: (253, 126, 298.5811, 257)}, 'counts': []},
        {'frame': 260, 'test_data': [(256, 127)], 'assertations': {4: (256, 127, 301.7434, 259)}, 'counts': []},
        {'frame': 261, 'test_data': [(257, 127)], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 262, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 263, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 264, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 265, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 266, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 267, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 268, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 269, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 270, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 271, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 272, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 273, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 274, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 275, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 276, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 277, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 278, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 279, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 280, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 281, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 282, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
        {'frame': 283, 'test_data': [], 'assertations': {4: (257, 127, 302.7434, 260)}, 'counts': []},
    ]
}
with open('data.json', 'w') as file:
    json.dump(data, file)
