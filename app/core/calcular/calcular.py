import core_app as co

def calcular(fuente, operacion='cuenta', sector=['CO','SF','CP','TE','CA','OT'], incluyeSector='S', meses=36, moneda=['G','D']):
    '''Obtiene la cuenta o sumaMonto segun los argumentos ingresados\\
    fuente: solicitudes, morosidades\\
    operacion: cuenta, sumaMonto\\
    sector: CO, SF, CP, TE, CA, OT'''

    if operacion=='cuenta':
        result = sum(list(map(lambda x: 1 if co.eval_sn(incluyeSector, x['sector'], sector) and\
                                             co.eval_sn('S', x['moneda'], moneda)\
                                        else 0, fuente)))
        print(result)
        

    if operacion=='sumaMonto':
        result = sum(list(map(lambda x: x['monto'] if x['monto'] is not None and\
                                                      co.eval_sn(incluyeSector, x['sector'], sector) and\
                                                      co.eval_sn('S', x['moneda'], moneda)\
                                                 else 0, fuente)))
        print(result)
    
    return result






    # if operacion=='cuenta':
    #     return sum(list(map(lambda x: (x['sector'] in sector if incluyeSector=='S' else x['sector'] not in sector) and\
    #                                    x['moneda'] in moneda, fuente)))

    # if operacion=='sumaMonto':
    #     return sum(list(map(lambda x: (x['monto']) if (x['sector'] in sector if incluyeSector=='S' else x['sector'] not in sector) and\
    #                                                    x['moneda'] in moneda\
    #                                                else 0, fuente)))