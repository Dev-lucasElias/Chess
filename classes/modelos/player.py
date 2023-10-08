
class Player:
	
	def __init__(self,nome, cpf):
		if isinstance(nome, str):
			self.__nome = nome
		if isinstance(cpf,int):
			self.__cpf = cpf

	@property
	def nome(self) -> str:
		return self.__nome
	
	@nome.setter
	def nome(self, nome: str) -> None:
		if isinstance(nome, str):
			self.__nome = nome


