numMachines = 10
machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
processingTimes = {(1, 1): 21, (2, 1): 10, (3, 1): 11, (4, 1): 17, (5, 1): 16, (6, 1): 21, (7, 1): 25, (8, 1): 27, (9, 1): 17, (10, 1): 22, (1, 2): 22, (2, 2): 27, (3, 2): 29, (4, 2): 19, (5, 2): 21, (6, 2): 30, (7, 2): 18, (8, 2): 19, (9, 2): 22, (10, 2): 13, (1, 3): 29, (2, 3): 11, (3, 3): 21, (4, 3): 18, (5, 3): 28, (6, 3): 12, (7, 3): 15, (8, 3): 22, (9, 3): 17, (10, 3): 28, (1, 4): 13, (2, 4): 27, (3, 4): 12, (4, 4): 14, (5, 4): 14, (6, 4): 15, (7, 4): 28, (8, 4): 26, (9, 4): 26, (10, 4): 22, (1, 5): 12, (2, 5): 25, (3, 5): 30, (4, 5): 11, (5, 5): 22, (6, 5): 13, (7, 5): 23, (8, 5): 20, (9, 5): 28, (10, 5): 29, (1, 6): 25, (2, 6): 25, (3, 6): 23, (4, 6): 24, (5, 6): 30, (6, 6): 19, (7, 6): 30, (8, 6): 28, (9, 6): 13, (10, 6): 14, (1, 7): 26, (2, 7): 28, (3, 7): 19, (4, 7): 22, (5, 7): 23, (6, 7): 10, (7, 7): 29, (8, 7): 12, (9, 7): 11, (10, 7): 17, (1, 8): 21, (2, 8): 11, (3, 8): 24, (4, 8): 12, (5, 8): 14, (6, 8): 12, (7, 8): 24, (8, 8): 13, (9, 8): 15, (10, 8): 10, (1, 9): 28, (2, 9): 29, (3, 9): 30, (4, 9): 16, (5, 9): 28, (6, 9): 15, (7, 9): 16, (8, 9): 11, (9, 9): 27, (10, 9): 25, (1, 10): 27, (2, 10): 26, (3, 10): 25, (4, 10): 18, (5, 10): 20, (6, 10): 12, (7, 10): 11, (8, 10): 25, (9, 10): 26, (10, 10): 19, (1, 11): 22, (2, 11): 13, (3, 11): 18, (4, 11): 25, (5, 11): 14, (6, 11): 26, (7, 11): 22, (8, 11): 30, (9, 11): 28, (10, 11): 12, (1, 12): 11, (2, 12): 12, (3, 12): 20, (4, 12): 26, (5, 12): 26, (6, 12): 12, (7, 12): 16, (8, 12): 17, (9, 12): 28, (10, 12): 23, (1, 13): 16, (2, 13): 28, (3, 13): 28, (4, 13): 19, (5, 13): 26, (6, 13): 13, (7, 13): 28, (8, 13): 19, (9, 13): 11, (10, 13): 12, (1, 14): 26, (2, 14): 22, (3, 14): 22, (4, 14): 26, (5, 14): 17, (6, 14): 11, (7, 14): 30, (8, 14): 27, (9, 14): 29, (10, 14): 26, (1, 15): 10, (2, 15): 29, (3, 15): 18, (4, 15): 27, (5, 15): 13, (6, 15): 25, (7, 15): 27, (8, 15): 30, (9, 15): 17, (10, 15): 10, (1, 16): 26, (2, 16): 28, (3, 16): 23, (4, 16): 17, (5, 16): 28, (6, 16): 14, (7, 16): 24, (8, 16): 13, (9, 16): 14, (10, 16): 30, (1, 17): 14, (2, 17): 26, (3, 17): 21, (4, 17): 12, (5, 17): 24, (6, 17): 20, (7, 17): 17, (8, 17): 28, (9, 17): 19, (10, 17): 26, (1, 18): 14, (2, 18): 15, (3, 18): 12, (4, 18): 14, (5, 18): 21, (6, 18): 12, (7, 18): 14, (8, 18): 27, (9, 18): 24, (10, 18): 13, (1, 19): 24, (2, 19): 15, (3, 19): 28, (4, 19): 26, (5, 19): 12, (6, 19): 24, (7, 19): 14, (8, 19): 18, (9, 19): 11, (10, 19): 19, (1, 20): 18, (2, 20): 30, (3, 20): 28, (4, 20): 22, (5, 20): 22, (6, 20): 14, (7, 20): 18, (8, 20): 23, (9, 20): 15, (10, 20): 23}