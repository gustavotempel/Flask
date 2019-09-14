import jsonload.jsonload

def main():
    #########################
    # Definicion de Fuentes #
    #########################
    def source_definition():

        global persona
        global datosPersonales
        global caracteristicasFisicas
        global clubes
        global partidos

        persona = jsonload.jsonload.persona
        datosPersonales = jsonload.jsonload.datosPersonales
        caracteristicasFisicas = jsonload.jsonload.caracteristicasFisicas
        clubes = jsonload.jsonload.clubes
        partidos = jsonload.jsonload.partidos

        return 0

    ########################
    # Calculo de Atributos #
    ########################
    def attribute_calculator():

        atributos = {}

        atributos['cant_partidos'] = co.calcular(partidos)
        

        return atributos
    #######################
    # Salida de Atributos #
    #######################

    co.salida(atributos)
