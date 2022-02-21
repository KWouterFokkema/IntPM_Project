numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
processingTimes = {(1, 1): 6, (2, 1): 7, (3, 1): 4, (4, 1): 6, (5, 1): 6, (6, 1): 4, (7, 1): 10, (8, 1): 6, (9, 1): 10, (10, 1): 4, (1, 2): 4, (2, 2): 8, (3, 2): 6, (4, 2): 5, (5, 2): 10, (6, 2): 8, (7, 2): 11, (8, 2): 4, (9, 2): 6, (10, 2): 9, (1, 3): 12, (2, 3): 12, (3, 3): 6, (4, 3): 6, (5, 3): 8, (6, 3): 4, (7, 3): 10, (8, 3): 10, (9, 3): 5, (10, 3): 6, (1, 4): 9, (2, 4): 11, (3, 4): 12, (4, 4): 6, (5, 4): 4, (6, 4): 8, (7, 4): 11, (8, 4): 4, (9, 4): 4, (10, 4): 10, (1, 5): 4, (2, 5): 4, (3, 5): 4, (4, 5): 8, (5, 5): 11, (6, 5): 10, (7, 5): 5, (8, 5): 4, (9, 5): 11, (10, 5): 6, (1, 6): 9, (2, 6): 6, (3, 6): 10, (4, 6): 8, (5, 6): 11, (6, 6): 4, (7, 6): 11, (8, 6): 9, (9, 6): 6, (10, 6): 7, (1, 7): 5, (2, 7): 12, (3, 7): 5, (4, 7): 9, (5, 7): 9, (6, 7): 4, (7, 7): 9, (8, 7): 9, (9, 7): 5, (10, 7): 9, (1, 8): 7, (2, 8): 4, (3, 8): 10, (4, 8): 8, (5, 8): 6, (6, 8): 9, (7, 8): 6, (8, 8): 9, (9, 8): 11, (10, 8): 8, (1, 9): 5, (2, 9): 4, (3, 9): 12, (4, 9): 8, (5, 9): 6, (6, 9): 5, (7, 9): 5, (8, 9): 5, (9, 9): 11, (10, 9): 7, (1, 10): 12, (2, 10): 8, (3, 10): 12, (4, 10): 9, (5, 10): 8, (6, 10): 5, (7, 10): 10, (8, 10): 4, (9, 10): 7, (10, 10): 6, (1, 11): 6, (2, 11): 4, (3, 11): 8, (4, 11): 12, (5, 11): 9, (6, 11): 9, (7, 11): 12, (8, 11): 10, (9, 11): 11, (10, 11): 6, (1, 12): 9, (2, 12): 6, (3, 12): 4, (4, 12): 10, (5, 12): 6, (6, 12): 5, (7, 12): 10, (8, 12): 9, (9, 12): 4, (10, 12): 8, (1, 13): 7, (2, 13): 9, (3, 13): 6, (4, 13): 7, (5, 13): 4, (6, 13): 4, (7, 13): 12, (8, 13): 11, (9, 13): 4, (10, 13): 9, (1, 14): 11, (2, 14): 7, (3, 14): 9, (4, 14): 4, (5, 14): 8, (6, 14): 6, (7, 14): 9, (8, 14): 7, (9, 14): 5, (10, 14): 6, (1, 15): 9, (2, 15): 9, (3, 15): 4, (4, 15): 12, (5, 15): 5, (6, 15): 6, (7, 15): 12, (8, 15): 5, (9, 15): 7, (10, 15): 12, (1, 16): 5, (2, 16): 5, (3, 16): 7, (4, 16): 7, (5, 16): 8, (6, 16): 10, (7, 16): 7, (8, 16): 10, (9, 16): 9, (10, 16): 12, (1, 17): 7, (2, 17): 4, (3, 17): 5, (4, 17): 6, (5, 17): 6, (6, 17): 5, (7, 17): 10, (8, 17): 10, (9, 17): 9, (10, 17): 12, (1, 18): 9, (2, 18): 11, (3, 18): 12, (4, 18): 5, (5, 18): 12, (6, 18): 10, (7, 18): 4, (8, 18): 5, (9, 18): 6, (10, 18): 5, (1, 19): 7, (2, 19): 9, (3, 19): 12, (4, 19): 9, (5, 19): 7, (6, 19): 9, (7, 19): 9, (8, 19): 12, (9, 19): 4, (10, 19): 8, (1, 20): 4, (2, 20): 7, (3, 20): 4, (4, 20): 10, (5, 20): 12, (6, 20): 4, (7, 20): 5, (8, 20): 12, (9, 20): 11, (10, 20): 6}
