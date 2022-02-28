numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
processingTimes = {(1, 1): 6, (2, 1): 5, (3, 1): 3, (4, 1): 6, (5, 1): 3, (6, 1): 2, (7, 1): 4, (8, 1): 3, (9, 1): 2, (10, 1): 2, (1, 2): 5, (2, 2): 3, (3, 2): 2, (4, 2): 2, (5, 2): 4, (6, 2): 4, (7, 2): 2, (8, 2): 5, (9, 2): 6, (10, 2): 3, (1, 3): 3, (2, 3): 6, (3, 3): 4, (4, 3): 3, (5, 3): 4, (6, 3): 6, (7, 3): 6, (8, 3): 6, (9, 3): 2, (10, 3): 3, (1, 4): 4, (2, 4): 6, (3, 4): 5, (4, 4): 5, (5, 4): 5, (6, 4): 5, (7, 4): 3, (8, 4): 2, (9, 4): 2, (10, 4): 2, (1, 5): 3, (2, 5): 4, (3, 5): 4, (4, 5): 2, (5, 5): 6, (6, 5): 2, (7, 5): 3, (8, 5): 5, (9, 5): 4, (10, 5): 5, (1, 6): 6, (2, 6): 4, (3, 6): 6, (4, 6): 5, (5, 6): 4, (6, 6): 5, (7, 6): 5, (8, 6): 2, (9, 6): 4, (10, 6): 6, (1, 7): 2, (2, 7): 2, (3, 7): 2, (4, 7): 2, (5, 7): 4, (6, 7): 5, (7, 7): 6, (8, 7): 5, (9, 7): 5, (10, 7): 5, (1, 8): 3, (2, 8): 2, (3, 8): 5, (4, 8): 5, (5, 8): 5, (6, 8): 4, (7, 8): 4, (8, 8): 6, (9, 8): 6, (10, 8): 3, (1, 9): 5, (2, 9): 6, (3, 9): 6, (4, 9): 5, (5, 9): 4, (6, 9): 4, (7, 9): 3, (8, 9): 6, (9, 9): 5, (10, 9): 5, (1, 10): 5, (2, 10): 4, (3, 10): 4, (4, 10): 3, (5, 10): 4, (6, 10): 6, (7, 10): 3, (8, 10): 4, (9, 10): 6, (10, 10): 5, (1, 11): 2, (2, 11): 4, (3, 11): 4, (4, 11): 5, (5, 11): 2, (6, 11): 4, (7, 11): 3, (8, 11): 4, (9, 11): 5, (10, 11): 2, (1, 12): 4, (2, 12): 6, (3, 12): 3, (4, 12): 5, (5, 12): 3, (6, 12): 6, (7, 12): 5, (8, 12): 6, (9, 12): 4, (10, 12): 6, (1, 13): 6, (2, 13): 3, (3, 13): 2, (4, 13): 6, (5, 13): 2, (6, 13): 3, (7, 13): 4, (8, 13): 4, (9, 13): 3, (10, 13): 3, (1, 14): 4, (2, 14): 3, (3, 14): 5, (4, 14): 3, (5, 14): 5, (6, 14): 4, (7, 14): 2, (8, 14): 3, (9, 14): 6, (10, 14): 2, (1, 15): 6, (2, 15): 2, (3, 15): 6, (4, 15): 4, (5, 15): 5, (6, 15): 2, (7, 15): 2, (8, 15): 2, (9, 15): 2, (10, 15): 6, (1, 16): 5, (2, 16): 4, (3, 16): 3, (4, 16): 5, (5, 16): 3, (6, 16): 5, (7, 16): 6, (8, 16): 6, (9, 16): 4, (10, 16): 3, (1, 17): 6, (2, 17): 5, (3, 17): 4, (4, 17): 3, (5, 17): 6, (6, 17): 5, (7, 17): 2, (8, 17): 6, (9, 17): 3, (10, 17): 5, (1, 18): 4, (2, 18): 2, (3, 18): 4, (4, 18): 5, (5, 18): 3, (6, 18): 4, (7, 18): 4, (8, 18): 3, (9, 18): 4, (10, 18): 5, (1, 19): 5, (2, 19): 2, (3, 19): 6, (4, 19): 4, (5, 19): 3, (6, 19): 2, (7, 19): 4, (8, 19): 6, (9, 19): 3, (10, 19): 3, (1, 20): 6, (2, 20): 4, (3, 20): 5, (4, 20): 4, (5, 20): 6, (6, 20): 6, (7, 20): 6, (8, 20): 6, (9, 20): 2, (10, 20): 6}