numMachines = 8
machines = [1, 2, 3, 4, 5, 6, 7, 8]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
processingTimes = {(1, 1): 4, (2, 1): 3, (3, 1): 2, (4, 1): 5, (5, 1): 5, (6, 1): 2, (7, 1): 3, (8, 1): 5, (1, 2): 6, (2, 2): 2, (3, 2): 2, (4, 2): 2, (5, 2): 6, (6, 2): 2, (7, 2): 6, (8, 2): 2, (1, 3): 4, (2, 3): 3, (3, 3): 3, (4, 3): 2, (5, 3): 4, (6, 3): 6, (7, 3): 5, (8, 3): 6, (1, 4): 2, (2, 4): 4, (3, 4): 3, (4, 4): 5, (5, 4): 2, (6, 4): 3, (7, 4): 6, (8, 4): 5, (1, 5): 3, (2, 5): 5, (3, 5): 2, (4, 5): 3, (5, 5): 3, (6, 5): 2, (7, 5): 3, (8, 5): 4, (1, 6): 3, (2, 6): 4, (3, 6): 2, (4, 6): 4, (5, 6): 6, (6, 6): 3, (7, 6): 4, (8, 6): 5, (1, 7): 3, (2, 7): 3, (3, 7): 3, (4, 7): 4, (5, 7): 5, (6, 7): 5, (7, 7): 4, (8, 7): 4, (1, 8): 3, (2, 8): 4, (3, 8): 5, (4, 8): 4, (5, 8): 4, (6, 8): 6, (7, 8): 5, (8, 8): 3, (1, 9): 2, (2, 9): 3, (3, 9): 3, (4, 9): 2, (5, 9): 3, (6, 9): 5, (7, 9): 3, (8, 9): 4, (1, 10): 6, (2, 10): 3, (3, 10): 5, (4, 10): 2, (5, 10): 4, (6, 10): 5, (7, 10): 2, (8, 10): 2, (1, 11): 3, (2, 11): 5, (3, 11): 2, (4, 11): 4, (5, 11): 4, (6, 11): 2, (7, 11): 4, (8, 11): 5, (1, 12): 6, (2, 12): 5, (3, 12): 2, (4, 12): 2, (5, 12): 5, (6, 12): 3, (7, 12): 4, (8, 12): 6, (1, 13): 5, (2, 13): 3, (3, 13): 4, (4, 13): 2, (5, 13): 3, (6, 13): 5, (7, 13): 3, (8, 13): 5, (1, 14): 5, (2, 14): 3, (3, 14): 6, (4, 14): 3, (5, 14): 3, (6, 14): 5, (7, 14): 5, (8, 14): 2, (1, 15): 5, (2, 15): 3, (3, 15): 4, (4, 15): 4, (5, 15): 2, (6, 15): 2, (7, 15): 5, (8, 15): 4, (1, 16): 2, (2, 16): 6, (3, 16): 2, (4, 16): 2, (5, 16): 3, (6, 16): 2, (7, 16): 3, (8, 16): 5, (1, 17): 3, (2, 17): 6, (3, 17): 5, (4, 17): 4, (5, 17): 3, (6, 17): 6, (7, 17): 4, (8, 17): 3, (1, 18): 2, (2, 18): 6, (3, 18): 6, (4, 18): 2, (5, 18): 4, (6, 18): 5, (7, 18): 6, (8, 18): 2, (1, 19): 4, (2, 19): 6, (3, 19): 5, (4, 19): 6, (5, 19): 2, (6, 19): 3, (7, 19): 4, (8, 19): 6, (1, 20): 3, (2, 20): 6, (3, 20): 3, (4, 20): 2, (5, 20): 3, (6, 20): 6, (7, 20): 6, (8, 20): 5, (1, 21): 5, (2, 21): 3, (3, 21): 2, (4, 21): 2, (5, 21): 5, (6, 21): 2, (7, 21): 2, (8, 21): 2, (1, 22): 3, (2, 22): 3, (3, 22): 2, (4, 22): 4, (5, 22): 3, (6, 22): 2, (7, 22): 6, (8, 22): 5, (1, 23): 5, (2, 23): 3, (3, 23): 2, (4, 23): 2, (5, 23): 4, (6, 23): 2, (7, 23): 2, (8, 23): 5, (1, 24): 2, (2, 24): 2, (3, 24): 6, (4, 24): 2, (5, 24): 5, (6, 24): 3, (7, 24): 2, (8, 24): 5, (1, 25): 2, (2, 25): 4, (3, 25): 5, (4, 25): 5, (5, 25): 4, (6, 25): 6, (7, 25): 6, (8, 25): 4, (1, 26): 4, (2, 26): 4, (3, 26): 2, (4, 26): 3, (5, 26): 2, (6, 26): 2, (7, 26): 2, (8, 26): 4, (1, 27): 3, (2, 27): 6, (3, 27): 6, (4, 27): 5, (5, 27): 3, (6, 27): 6, (7, 27): 2, (8, 27): 6, (1, 28): 5, (2, 28): 4, (3, 28): 6, (4, 28): 6, (5, 28): 6, (6, 28): 2, (7, 28): 5, (8, 28): 2, (1, 29): 6, (2, 29): 2, (3, 29): 2, (4, 29): 2, (5, 29): 3, (6, 29): 2, (7, 29): 6, (8, 29): 3, (1, 30): 5, (2, 30): 4, (3, 30): 2, (4, 30): 2, (5, 30): 4, (6, 30): 4, (7, 30): 2, (8, 30): 2}
