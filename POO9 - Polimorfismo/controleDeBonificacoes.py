class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        # resolve erro código com if
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('Instancia de  {} não implementao método get_bonificacao()'.format(self.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes