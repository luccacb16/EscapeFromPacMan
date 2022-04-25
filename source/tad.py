import pygame

# TAD Pilha

class Pilha:

	def __init__(self):
		self.data = []
		self.topo = 0

	''' Operações '''

	# VAZIA
	def vazia(self):
		return self.topo <= 0

	# CHEIA
	def cheia(self):
		return self.topo >= 4

	# EMPILHA
	def empilha(self, item):
		if self.cheia() != True:
			self.data.append(item)
			self.topo += 1

	# DESEMPILHA
	def desempilha(self):
		if self.vazia != True:
			self.data.pop()
			self.topo -= 1

	# GET TOPO
	def getTopo(self):
		return self.data[self.topo-1]

	# GET INDEX_TOPO
	def getIndexTopo(self):
		return self.topo-1

	# PRINTA PILHA
	def printa(self):
		for i in range(self.topo):
			print(self.data[i])

	# RESET (pygame)
	def reset(self):
		self.data = []
		self.topo = 0
