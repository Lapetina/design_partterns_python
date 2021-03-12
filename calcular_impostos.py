# -*- coding: UTF-8 -*-


class CalcularImpostos(object):

    def realiza_calculo(self, orcamento):
        icms_calculado = orcamento.valor * 0.1
        print(icms_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = CalcularImpostos()
    calculador_de_impostos.realiza_calculo(orcamento)  ## imprimirá 50.0
