numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
processingTimes = {(1, 1): 18, (2, 1): 15, (3, 1): 24, (4, 1): 8, (5, 1): 11, (6, 1): 24, (7, 1): 17, (8, 1): 24, (9, 1): 12, (10, 1): 15, (1, 2): 21, (2, 2): 17, (3, 2): 12, (4, 2): 12, (5, 2): 20, (6, 2): 18, (7, 2): 17, (8, 2): 22, (9, 2): 24, (10, 2): 9, (1, 3): 14, (2, 3): 13, (3, 3): 17, (4, 3): 10, (5, 3): 21, (6, 3): 23, (7, 3): 21, (8, 3): 16, (9, 3): 9, (10, 3): 10, (1, 4): 19, (2, 4): 19, (3, 4): 22, (4, 4): 8, (5, 4): 24, (6, 4): 24, (7, 4): 14, (8, 4): 20, (9, 4): 9, (10, 4): 17, (1, 5): 13, (2, 5): 16, (3, 5): 14, (4, 5): 21, (5, 5): 10, (6, 5): 24, (7, 5): 18, (8, 5): 10, (9, 5): 15, (10, 5): 16, (1, 6): 20, (2, 6): 17, (3, 6): 15, (4, 6): 21, (5, 6): 9, (6, 6): 9, (7, 6): 22, (8, 6): 24, (9, 6): 19, (10, 6): 24, (1, 7): 21, (2, 7): 10, (3, 7): 12, (4, 7): 22, (5, 7): 12, (6, 7): 24, (7, 7): 21, (8, 7): 24, (9, 7): 13, (10, 7): 14, (1, 8): 22, (2, 8): 20, (3, 8): 9, (4, 8): 12, (5, 8): 23, (6, 8): 21, (7, 8): 12, (8, 8): 13, (9, 8): 8, (10, 8): 14, (1, 9): 18, (2, 9): 18, (3, 9): 16, (4, 9): 8, (5, 9): 24, (6, 9): 15, (7, 9): 19, (8, 9): 9, (9, 9): 15, (10, 9): 9, (1, 10): 23, (2, 10): 8, (3, 10): 16, (4, 10): 19, (5, 10): 21, (6, 10): 12, (7, 10): 15, (8, 10): 23, (9, 10): 14, (10, 10): 11, (1, 11): 9, (2, 11): 23, (3, 11): 24, (4, 11): 9, (5, 11): 13, (6, 11): 20, (7, 11): 9, (8, 11): 10, (9, 11): 22, (10, 11): 24, (1, 12): 14, (2, 12): 19, (3, 12): 18, (4, 12): 14, (5, 12): 9, (6, 12): 16, (7, 12): 11, (8, 12): 18, (9, 12): 16, (10, 12): 20, (1, 13): 9, (2, 13): 18, (3, 13): 8, (4, 13): 19, (5, 13): 18, (6, 13): 9, (7, 13): 8, (8, 13): 21, (9, 13): 20, (10, 13): 20, (1, 14): 24, (2, 14): 20, (3, 14): 9, (4, 14): 12, (5, 14): 20, (6, 14): 13, (7, 14): 8, (8, 14): 18, (9, 14): 17, (10, 14): 13, (1, 15): 14, (2, 15): 14, (3, 15): 17, (4, 15): 22, (5, 15): 12, (6, 15): 17, (7, 15): 14, (8, 15): 19, (9, 15): 20, (10, 15): 13, (1, 16): 15, (2, 16): 14, (3, 16): 15, (4, 16): 8, (5, 16): 8, (6, 16): 9, (7, 16): 9, (8, 16): 13, (9, 16): 10, (10, 16): 13, (1, 17): 19, (2, 17): 13, (3, 17): 16, (4, 17): 19, (5, 17): 20, (6, 17): 22, (7, 17): 11, (8, 17): 19, (9, 17): 20, (10, 17): 13, (1, 18): 18, (2, 18): 17, (3, 18): 15, (4, 18): 22, (5, 18): 20, (6, 18): 8, (7, 18): 10, (8, 18): 13, (9, 18): 19, (10, 18): 18, (1, 19): 15, (2, 19): 17, (3, 19): 18, (4, 19): 24, (5, 19): 24, (6, 19): 11, (7, 19): 10, (8, 19): 22, (9, 19): 17, (10, 19): 12, (1, 20): 19, (2, 20): 16, (3, 20): 9, (4, 20): 16, (5, 20): 12, (6, 20): 8, (7, 20): 22, (8, 20): 10, (9, 20): 11, (10, 20): 16}