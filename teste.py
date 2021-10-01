import sublime
import sublime_plugin
from math import ceil # para arredondar para cima

class TesteDivisorCommand(sublime_plugin.TextCommand):
	
	def totallinhas(self):
		'''Retorna o total de linhas de uma visualizacao'''
		lines, _ = self.view.rowcol(self.view.size())
		return lines

	def run(self, edit):
		lista=[]
		# Obtendo cada regiao da selecao
		for regiao in self.view.sel():
			# Por algum motivo ele coloca tudo em uma coluna na List (uma Região)
			lista.append(self.view.substr(self.view.line(regiao)))
		# Transformando para uma lista o único elemento
		texto=lista[0].split('\n')
		# Concatenando
		saida=';'.join(texto)
		# Substituindo o resultado na Região selecionda
		self.view.replace(edit, self.view.line(regiao), saida)


654321
456123
459654
123465;444444;666666;777777;888888
999999