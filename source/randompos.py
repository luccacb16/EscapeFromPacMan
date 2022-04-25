import random
import time

class Randompos:
	def __init__(self):
		random.seed(time.perf_counter())

		self.posicoes = [(70, 464), (255, 600), (454, 668), (131, 260), (374, 193), (253, 36), (544, 156), (443, 424)]
		self.posicoes_index = random.sample(range(8), 8)
	
	def reset(self):
		random.seed(time.perf_counter())

		self.posicoes = [(70, 464), (255, 600), (454, 668), (131, 260), (374, 193), (253, 36), (544, 156), (443, 424)]
		self.posicoes_index = random.sample(range(8), 8)