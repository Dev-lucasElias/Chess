class relatorioError (Exception):
      def __init__(self):
            self.mensagem = "Não foi possivel gerar o relatorio, contate o setor de TI"
            super().__init__(self.mensagem)
            
