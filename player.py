from abc import ABC, abstractmethod

class Player:
	@abstractmethod
	def __init__(self, cor: str):
		if isinstance(cor, str):
			self.__cor = cor

	@property
	def cor(self) -> str:
		return self.__cor
	
	@cor.setter
	def cor(self, cor: str) -> None:
		if isinstance(cor, str):
			self.__cor = cor


