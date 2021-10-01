# Nao importa o nome deste arquivo, desde que seja com extensão .py
# O sublime monitora os arquivos ate um certo nivel de pastas
import sublime
import sublime_plugin
from math import ceil # para arredondar para cima

# Obtido do 'goto_line.py' do pacote 'Default.sublime-package'
class PromptDivisorLinhasCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Qte Objetos por Linha:", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            qte = int(text)
            if self.window.active_view():
                self.window.active_view().run_command("divisor_linhas", {"qte_objetos": qte})
        except ValueError:
            pass

class DivisorLinhasCommand(sublime_plugin.TextCommand):
	
	def totallinhas(self):
		'''Retorna o total de linhas de uma visualizacao'''
		lines, _ = self.view.rowcol(self.view.size())
		return lines

	def run(self, edit, qte_objetos):		
		qte_objetos = int(qte_objetos)
		# Para evitar numeros negativos e zero no denominador
		if qte_objetos <=0:
			qte_objetos = 1

		# Quantidade de linhas
		qte_linhas = ceil(self.totallinhas()/qte_objetos)

		# Obter todos os dados selecionados em uma Lista
		lista=[]
		# Obtendo cada regiao da selecao
		for regiao in self.view.sel():
			# Por algum motivo ele coloca tudo em uma coluna na List (uma Região)
			lista.append(self.view.substr(self.view.line(regiao)))
		# Transformando para uma lista o único elemento
		saida_total=lista[0].split('\n')

		# Loop para separar os objetos em linhas
		i=0
		txt=''
		# Lembrando que o range não pega o ultimo valor por isso o +1
		for j in range(1,qte_linhas+1):
			txt+=';'.join(saida_total[i:qte_objetos*j]) + '\n'
			i=qte_objetos*j
		
		# Substituindo toda a região com o texto
		self.view.replace(edit, self.view.line(regiao), txt)
		# Limpando a selecao
		self.view.sel().clear()

# Lembre-se que DEVE ESTAR SELECIONADO para execução do plugin

# Sendo o nome da classe DivisorLinhas, deve-se chamar internamente no Sublime:
## view.run_command('divisor_linhas')

# Para chamar com parametros fazer:
## view.run_command('divisor_linhas',{'qte_objetos': 10})

# Se utilizar um comando não existente, não há aviso de erro
## view.run_command('poxa_vida')

# view.sel() - retorna o que estiver selecionado
# Usando 'edit' traz a capacidade de utilizar o ctrl-z

# Biblioteca:
# Forum Sublime : https://forum.sublimetext.com
# Referencia API: https://www.sublimetext.com/docs/api_reference.html#example_plugins:ver-3.2
# Sublime Community Doc: https://docs.sublimetext.io
# Exemplo Tutorial: https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685