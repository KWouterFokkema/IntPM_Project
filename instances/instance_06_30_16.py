numMachines = 6
machines = [1, 2, 3, 4, 5, 6]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
processingTimes = {(1, 1): 9, (2, 1): 14, (3, 1): 14, (4, 1): 15, (5, 1): 10, (6, 1): 10, (1, 2): 22, (2, 2): 24, (3, 2): 13, (4, 2): 24, (5, 2): 18, (6, 2): 21, (1, 3): 20, (2, 3): 14, (3, 3): 22, (4, 3): 10, (5, 3): 14, (6, 3): 11, (1, 4): 19, (2, 4): 13, (3, 4): 17, (4, 4): 14, (5, 4): 14, (6, 4): 21, (1, 5): 23, (2, 5): 14, (3, 5): 18, (4, 5): 12, (5, 5): 19, (6, 5): 17, (1, 6): 12, (2, 6): 15, (3, 6): 8, (4, 6): 11, (5, 6): 17, (6, 6): 16, (1, 7): 23, (2, 7): 13, (3, 7): 11, (4, 7): 10, (5, 7): 22, (6, 7): 12, (1, 8): 24, (2, 8): 13, (3, 8): 10, (4, 8): 14, (5, 8): 20, (6, 8): 16, (1, 9): 23, (2, 9): 16, (3, 9): 20, (4, 9): 15, (5, 9): 15, (6, 9): 22, (1, 10): 15, (2, 10): 16, (3, 10): 11, (4, 10): 20, (5, 10): 23, (6, 10): 18, (1, 11): 22, (2, 11): 21, (3, 11): 10, (4, 11): 24, (5, 11): 21, (6, 11): 12, (1, 12): 14, (2, 12): 10, (3, 12): 21, (4, 12): 21, (5, 12): 13, (6, 12): 16, (1, 13): 14, (2, 13): 13, (3, 13): 20, (4, 13): 16, (5, 13): 13, (6, 13): 23, (1, 14): 16, (2, 14): 9, (3, 14): 14, (4, 14): 17, (5, 14): 23, (6, 14): 14, (1, 15): 21, (2, 15): 11, (3, 15): 24, (4, 15): 16, (5, 15): 21, (6, 15): 9, (1, 16): 19, (2, 16): 18, (3, 16): 20, (4, 16): 13, (5, 16): 14, (6, 16): 23, (1, 17): 11, (2, 17): 10, (3, 17): 17, (4, 17): 21, (5, 17): 19, (6, 17): 17, (1, 18): 23, (2, 18): 22, (3, 18): 15, (4, 18): 21, (5, 18): 13, (6, 18): 8, (1, 19): 19, (2, 19): 23, (3, 19): 14, (4, 19): 21, (5, 19): 17, (6, 19): 24, (1, 20): 12, (2, 20): 16, (3, 20): 23, (4, 20): 21, (5, 20): 17, (6, 20): 19, (1, 21): 8, (2, 21): 20, (3, 21): 22, (4, 21): 16, (5, 21): 19, (6, 21): 15, (1, 22): 11, (2, 22): 16, (3, 22): 11, (4, 22): 14, (5, 22): 14, (6, 22): 14, (1, 23): 20, (2, 23): 23, (3, 23): 16, (4, 23): 14, (5, 23): 20, (6, 23): 20, (1, 24): 13, (2, 24): 11, (3, 24): 9, (4, 24): 13, (5, 24): 14, (6, 24): 15, (1, 25): 10, (2, 25): 19, (3, 25): 11, (4, 25): 13, (5, 25): 18, (6, 25): 21, (1, 26): 11, (2, 26): 14, (3, 26): 14, (4, 26): 23, (5, 26): 9, (6, 26): 15, (1, 27): 24, (2, 27): 16, (3, 27): 23, (4, 27): 23, (5, 27): 8, (6, 27): 14, (1, 28): 16, (2, 28): 16, (3, 28): 17, (4, 28): 16, (5, 28): 16, (6, 28): 21, (1, 29): 8, (2, 29): 10, (3, 29): 15, (4, 29): 20, (5, 29): 16, (6, 29): 23, (1, 30): 8, (2, 30): 20, (3, 30): 11, (4, 30): 18, (5, 30): 9, (6, 30): 14}