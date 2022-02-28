numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
processingTimes = {(1, 1): 4, (2, 1): 3, (3, 1): 2, (4, 1): 3, (5, 1): 2, (6, 1): 2, (7, 1): 3, (8, 1): 2, (9, 1): 2, (10, 1): 4, (1, 2): 4, (2, 2): 4, (3, 2): 3, (4, 2): 5, (5, 2): 3, (6, 2): 5, (7, 2): 3, (8, 2): 5, (9, 2): 4, (10, 2): 2, (1, 3): 5, (2, 3): 3, (3, 3): 3, (4, 3): 3, (5, 3): 2, (6, 3): 2, (7, 3): 2, (8, 3): 3, (9, 3): 6, (10, 3): 4, (1, 4): 2, (2, 4): 2, (3, 4): 6, (4, 4): 2, (5, 4): 5, (6, 4): 5, (7, 4): 2, (8, 4): 4, (9, 4): 6, (10, 4): 4, (1, 5): 6, (2, 5): 5, (3, 5): 5, (4, 5): 4, (5, 5): 5, (6, 5): 4, (7, 5): 5, (8, 5): 6, (9, 5): 5, (10, 5): 5, (1, 6): 3, (2, 6): 6, (3, 6): 3, (4, 6): 5, (5, 6): 5, (6, 6): 2, (7, 6): 2, (8, 6): 6, (9, 6): 3, (10, 6): 2, (1, 7): 5, (2, 7): 4, (3, 7): 2, (4, 7): 4, (5, 7): 6, (6, 7): 3, (7, 7): 3, (8, 7): 5, (9, 7): 6, (10, 7): 2, (1, 8): 6, (2, 8): 6, (3, 8): 4, (4, 8): 3, (5, 8): 5, (6, 8): 4, (7, 8): 2, (8, 8): 4, (9, 8): 5, (10, 8): 5, (1, 9): 4, (2, 9): 5, (3, 9): 2, (4, 9): 3, (5, 9): 5, (6, 9): 2, (7, 9): 5, (8, 9): 3, (9, 9): 4, (10, 9): 4, (1, 10): 5, (2, 10): 3, (3, 10): 3, (4, 10): 5, (5, 10): 2, (6, 10): 2, (7, 10): 5, (8, 10): 6, (9, 10): 4, (10, 10): 5, (1, 11): 4, (2, 11): 5, (3, 11): 4, (4, 11): 5, (5, 11): 6, (6, 11): 2, (7, 11): 5, (8, 11): 6, (9, 11): 2, (10, 11): 4, (1, 12): 4, (2, 12): 4, (3, 12): 2, (4, 12): 6, (5, 12): 4, (6, 12): 3, (7, 12): 6, (8, 12): 2, (9, 12): 2, (10, 12): 5, (1, 13): 3, (2, 13): 6, (3, 13): 6, (4, 13): 3, (5, 13): 2, (6, 13): 5, (7, 13): 6, (8, 13): 6, (9, 13): 3, (10, 13): 6, (1, 14): 5, (2, 14): 2, (3, 14): 5, (4, 14): 3, (5, 14): 3, (6, 14): 3, (7, 14): 6, (8, 14): 3, (9, 14): 4, (10, 14): 5, (1, 15): 4, (2, 15): 4, (3, 15): 4, (4, 15): 3, (5, 15): 3, (6, 15): 5, (7, 15): 5, (8, 15): 5, (9, 15): 2, (10, 15): 5, (1, 16): 6, (2, 16): 5, (3, 16): 2, (4, 16): 2, (5, 16): 3, (6, 16): 3, (7, 16): 2, (8, 16): 5, (9, 16): 2, (10, 16): 5, (1, 17): 5, (2, 17): 2, (3, 17): 2, (4, 17): 3, (5, 17): 3, (6, 17): 2, (7, 17): 5, (8, 17): 3, (9, 17): 2, (10, 17): 3, (1, 18): 5, (2, 18): 4, (3, 18): 6, (4, 18): 3, (5, 18): 2, (6, 18): 4, (7, 18): 4, (8, 18): 5, (9, 18): 2, (10, 18): 4, (1, 19): 3, (2, 19): 4, (3, 19): 4, (4, 19): 6, (5, 19): 4, (6, 19): 6, (7, 19): 2, (8, 19): 4, (9, 19): 3, (10, 19): 3, (1, 20): 4, (2, 20): 6, (3, 20): 3, (4, 20): 2, (5, 20): 4, (6, 20): 3, (7, 20): 3, (8, 20): 6, (9, 20): 6, (10, 20): 4, (1, 21): 6, (2, 21): 2, (3, 21): 6, (4, 21): 3, (5, 21): 2, (6, 21): 4, (7, 21): 5, (8, 21): 5, (9, 21): 4, (10, 21): 5, (1, 22): 4, (2, 22): 5, (3, 22): 3, (4, 22): 5, (5, 22): 4, (6, 22): 5, (7, 22): 5, (8, 22): 5, (9, 22): 3, (10, 22): 6, (1, 23): 5, (2, 23): 2, (3, 23): 3, (4, 23): 3, (5, 23): 5, (6, 23): 2, (7, 23): 5, (8, 23): 5, (9, 23): 6, (10, 23): 5, (1, 24): 5, (2, 24): 4, (3, 24): 2, (4, 24): 6, (5, 24): 5, (6, 24): 3, (7, 24): 2, (8, 24): 3, (9, 24): 5, (10, 24): 3, (1, 25): 4, (2, 25): 3, (3, 25): 4, (4, 25): 3, (5, 25): 3, (6, 25): 6, (7, 25): 5, (8, 25): 4, (9, 25): 6, (10, 25): 3, (1, 26): 2, (2, 26): 6, (3, 26): 3, (4, 26): 5, (5, 26): 3, (6, 26): 6, (7, 26): 6, (8, 26): 4, (9, 26): 3, (10, 26): 6, (1, 27): 6, (2, 27): 5, (3, 27): 5, (4, 27): 5, (5, 27): 3, (6, 27): 3, (7, 27): 2, (8, 27): 5, (9, 27): 4, (10, 27): 2, (1, 28): 4, (2, 28): 4, (3, 28): 2, (4, 28): 6, (5, 28): 3, (6, 28): 4, (7, 28): 6, (8, 28): 5, (9, 28): 2, (10, 28): 6, (1, 29): 2, (2, 29): 6, (3, 29): 5, (4, 29): 2, (5, 29): 6, (6, 29): 5, (7, 29): 3, (8, 29): 5, (9, 29): 3, (10, 29): 6, (1, 30): 3, (2, 30): 3, (3, 30): 2, (4, 30): 4, (5, 30): 2, (6, 30): 2, (7, 30): 5, (8, 30): 3, (9, 30): 5, (10, 30): 6}