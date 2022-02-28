numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
processingTimes = {(1, 1): 16, (2, 1): 17, (3, 1): 12, (4, 1): 8, (5, 1): 12, (6, 1): 17, (7, 1): 18, (8, 1): 14, (9, 1): 11, (10, 1): 20, (1, 2): 18, (2, 2): 19, (3, 2): 8, (4, 2): 13, (5, 2): 12, (6, 2): 11, (7, 2): 17, (8, 2): 8, (9, 2): 14, (10, 2): 18, (1, 3): 10, (2, 3): 16, (3, 3): 18, (4, 3): 21, (5, 3): 11, (6, 3): 19, (7, 3): 10, (8, 3): 21, (9, 3): 24, (10, 3): 8, (1, 4): 13, (2, 4): 24, (3, 4): 10, (4, 4): 14, (5, 4): 22, (6, 4): 13, (7, 4): 8, (8, 4): 20, (9, 4): 23, (10, 4): 11, (1, 5): 21, (2, 5): 10, (3, 5): 14, (4, 5): 23, (5, 5): 17, (6, 5): 16, (7, 5): 23, (8, 5): 23, (9, 5): 19, (10, 5): 10, (1, 6): 14, (2, 6): 19, (3, 6): 12, (4, 6): 17, (5, 6): 15, (6, 6): 12, (7, 6): 20, (8, 6): 8, (9, 6): 15, (10, 6): 24, (1, 7): 15, (2, 7): 9, (3, 7): 9, (4, 7): 13, (5, 7): 14, (6, 7): 9, (7, 7): 8, (8, 7): 16, (9, 7): 9, (10, 7): 20, (1, 8): 16, (2, 8): 24, (3, 8): 15, (4, 8): 10, (5, 8): 15, (6, 8): 24, (7, 8): 16, (8, 8): 13, (9, 8): 21, (10, 8): 13, (1, 9): 9, (2, 9): 10, (3, 9): 17, (4, 9): 23, (5, 9): 8, (6, 9): 9, (7, 9): 17, (8, 9): 14, (9, 9): 15, (10, 9): 12, (1, 10): 17, (2, 10): 14, (3, 10): 23, (4, 10): 8, (5, 10): 11, (6, 10): 23, (7, 10): 15, (8, 10): 11, (9, 10): 21, (10, 10): 19, (1, 11): 21, (2, 11): 11, (3, 11): 11, (4, 11): 23, (5, 11): 20, (6, 11): 21, (7, 11): 15, (8, 11): 23, (9, 11): 15, (10, 11): 16, (1, 12): 18, (2, 12): 19, (3, 12): 12, (4, 12): 20, (5, 12): 16, (6, 12): 23, (7, 12): 22, (8, 12): 12, (9, 12): 10, (10, 12): 13, (1, 13): 10, (2, 13): 20, (3, 13): 23, (4, 13): 15, (5, 13): 23, (6, 13): 20, (7, 13): 19, (8, 13): 14, (9, 13): 24, (10, 13): 17, (1, 14): 12, (2, 14): 19, (3, 14): 10, (4, 14): 13, (5, 14): 23, (6, 14): 13, (7, 14): 23, (8, 14): 16, (9, 14): 12, (10, 14): 10, (1, 15): 24, (2, 15): 10, (3, 15): 20, (4, 15): 14, (5, 15): 21, (6, 15): 18, (7, 15): 14, (8, 15): 9, (9, 15): 12, (10, 15): 13, (1, 16): 22, (2, 16): 8, (3, 16): 10, (4, 16): 8, (5, 16): 10, (6, 16): 17, (7, 16): 8, (8, 16): 18, (9, 16): 11, (10, 16): 24, (1, 17): 13, (2, 17): 13, (3, 17): 24, (4, 17): 22, (5, 17): 17, (6, 17): 15, (7, 17): 23, (8, 17): 16, (9, 17): 17, (10, 17): 10, (1, 18): 24, (2, 18): 23, (3, 18): 17, (4, 18): 21, (5, 18): 18, (6, 18): 23, (7, 18): 21, (8, 18): 19, (9, 18): 12, (10, 18): 10, (1, 19): 8, (2, 19): 10, (3, 19): 17, (4, 19): 16, (5, 19): 9, (6, 19): 22, (7, 19): 22, (8, 19): 22, (9, 19): 15, (10, 19): 15, (1, 20): 24, (2, 20): 23, (3, 20): 14, (4, 20): 19, (5, 20): 20, (6, 20): 15, (7, 20): 21, (8, 20): 23, (9, 20): 23, (10, 20): 11, (1, 21): 16, (2, 21): 8, (3, 21): 12, (4, 21): 15, (5, 21): 22, (6, 21): 18, (7, 21): 21, (8, 21): 24, (9, 21): 21, (10, 21): 15, (1, 22): 23, (2, 22): 23, (3, 22): 15, (4, 22): 21, (5, 22): 8, (6, 22): 18, (7, 22): 20, (8, 22): 8, (9, 22): 22, (10, 22): 11, (1, 23): 16, (2, 23): 12, (3, 23): 21, (4, 23): 13, (5, 23): 14, (6, 23): 8, (7, 23): 11, (8, 23): 15, (9, 23): 17, (10, 23): 16, (1, 24): 21, (2, 24): 17, (3, 24): 17, (4, 24): 21, (5, 24): 18, (6, 24): 22, (7, 24): 17, (8, 24): 13, (9, 24): 17, (10, 24): 9, (1, 25): 16, (2, 25): 23, (3, 25): 22, (4, 25): 20, (5, 25): 19, (6, 25): 17, (7, 25): 22, (8, 25): 9, (9, 25): 19, (10, 25): 10, (1, 26): 21, (2, 26): 14, (3, 26): 16, (4, 26): 16, (5, 26): 21, (6, 26): 11, (7, 26): 15, (8, 26): 19, (9, 26): 22, (10, 26): 20, (1, 27): 15, (2, 27): 15, (3, 27): 24, (4, 27): 22, (5, 27): 20, (6, 27): 21, (7, 27): 22, (8, 27): 14, (9, 27): 10, (10, 27): 9, (1, 28): 15, (2, 28): 23, (3, 28): 23, (4, 28): 21, (5, 28): 20, (6, 28): 19, (7, 28): 12, (8, 28): 9, (9, 28): 22, (10, 28): 15, (1, 29): 18, (2, 29): 16, (3, 29): 18, (4, 29): 13, (5, 29): 18, (6, 29): 12, (7, 29): 19, (8, 29): 19, (9, 29): 20, (10, 29): 12, (1, 30): 17, (2, 30): 16, (3, 30): 9, (4, 30): 21, (5, 30): 8, (6, 30): 24, (7, 30): 13, (8, 30): 10, (9, 30): 15, (10, 30): 23}