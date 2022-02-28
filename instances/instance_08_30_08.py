numMachines = 8
machines = [1, 2, 3, 4, 5, 6, 7, 8]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
processingTimes = {(1, 1): 11, (2, 1): 7, (3, 1): 5, (4, 1): 4, (5, 1): 8, (6, 1): 10, (7, 1): 12, (8, 1): 8, (1, 2): 4, (2, 2): 6, (3, 2): 6, (4, 2): 11, (5, 2): 8, (6, 2): 7, (7, 2): 9, (8, 2): 8, (1, 3): 6, (2, 3): 11, (3, 3): 6, (4, 3): 7, (5, 3): 6, (6, 3): 7, (7, 3): 5, (8, 3): 5, (1, 4): 7, (2, 4): 6, (3, 4): 11, (4, 4): 8, (5, 4): 8, (6, 4): 10, (7, 4): 10, (8, 4): 6, (1, 5): 11, (2, 5): 7, (3, 5): 9, (4, 5): 12, (5, 5): 5, (6, 5): 4, (7, 5): 4, (8, 5): 8, (1, 6): 6, (2, 6): 4, (3, 6): 10, (4, 6): 12, (5, 6): 5, (6, 6): 12, (7, 6): 7, (8, 6): 12, (1, 7): 4, (2, 7): 10, (3, 7): 6, (4, 7): 8, (5, 7): 5, (6, 7): 6, (7, 7): 9, (8, 7): 7, (1, 8): 10, (2, 8): 5, (3, 8): 8, (4, 8): 8, (5, 8): 4, (6, 8): 12, (7, 8): 7, (8, 8): 6, (1, 9): 10, (2, 9): 4, (3, 9): 6, (4, 9): 8, (5, 9): 11, (6, 9): 11, (7, 9): 8, (8, 9): 12, (1, 10): 5, (2, 10): 12, (3, 10): 5, (4, 10): 8, (5, 10): 8, (6, 10): 6, (7, 10): 12, (8, 10): 5, (1, 11): 5, (2, 11): 9, (3, 11): 12, (4, 11): 11, (5, 11): 8, (6, 11): 6, (7, 11): 6, (8, 11): 12, (1, 12): 10, (2, 12): 9, (3, 12): 7, (4, 12): 4, (5, 12): 12, (6, 12): 8, (7, 12): 12, (8, 12): 10, (1, 13): 8, (2, 13): 8, (3, 13): 11, (4, 13): 12, (5, 13): 11, (6, 13): 10, (7, 13): 11, (8, 13): 10, (1, 14): 7, (2, 14): 8, (3, 14): 7, (4, 14): 9, (5, 14): 9, (6, 14): 8, (7, 14): 6, (8, 14): 9, (1, 15): 7, (2, 15): 11, (3, 15): 11, (4, 15): 9, (5, 15): 11, (6, 15): 7, (7, 15): 10, (8, 15): 5, (1, 16): 7, (2, 16): 11, (3, 16): 8, (4, 16): 11, (5, 16): 9, (6, 16): 12, (7, 16): 10, (8, 16): 5, (1, 17): 7, (2, 17): 9, (3, 17): 7, (4, 17): 10, (5, 17): 4, (6, 17): 10, (7, 17): 8, (8, 17): 5, (1, 18): 10, (2, 18): 12, (3, 18): 7, (4, 18): 9, (5, 18): 12, (6, 18): 11, (7, 18): 8, (8, 18): 6, (1, 19): 7, (2, 19): 6, (3, 19): 6, (4, 19): 6, (5, 19): 6, (6, 19): 10, (7, 19): 12, (8, 19): 5, (1, 20): 4, (2, 20): 9, (3, 20): 10, (4, 20): 11, (5, 20): 5, (6, 20): 10, (7, 20): 7, (8, 20): 5, (1, 21): 12, (2, 21): 11, (3, 21): 7, (4, 21): 9, (5, 21): 9, (6, 21): 8, (7, 21): 8, (8, 21): 12, (1, 22): 5, (2, 22): 12, (3, 22): 10, (4, 22): 11, (5, 22): 7, (6, 22): 6, (7, 22): 5, (8, 22): 4, (1, 23): 4, (2, 23): 9, (3, 23): 9, (4, 23): 9, (5, 23): 7, (6, 23): 9, (7, 23): 6, (8, 23): 10, (1, 24): 8, (2, 24): 4, (3, 24): 7, (4, 24): 10, (5, 24): 12, (6, 24): 5, (7, 24): 6, (8, 24): 11, (1, 25): 6, (2, 25): 9, (3, 25): 11, (4, 25): 11, (5, 25): 10, (6, 25): 12, (7, 25): 7, (8, 25): 10, (1, 26): 11, (2, 26): 10, (3, 26): 11, (4, 26): 5, (5, 26): 4, (6, 26): 6, (7, 26): 4, (8, 26): 10, (1, 27): 11, (2, 27): 4, (3, 27): 11, (4, 27): 7, (5, 27): 9, (6, 27): 7, (7, 27): 5, (8, 27): 6, (1, 28): 10, (2, 28): 10, (3, 28): 9, (4, 28): 8, (5, 28): 9, (6, 28): 9, (7, 28): 4, (8, 28): 9, (1, 29): 11, (2, 29): 12, (3, 29): 6, (4, 29): 7, (5, 29): 5, (6, 29): 9, (7, 29): 12, (8, 29): 6, (1, 30): 7, (2, 30): 12, (3, 30): 9, (4, 30): 12, (5, 30): 8, (6, 30): 12, (7, 30): 10, (8, 30): 5}