MODELS = [
    # {
    #     'name': '',
    #     'patch': '',
    #     'foreignkey': [
    #         {
    #             'model_to': '',
    #             'related_name': '',
    #             'col_from': '',
    #             'col_to': '',
    #         },
    #     ]
    # },
    {
        'name': 'cliente',
        'patch': '/home/pdalmasso/Descargas/cliente.json',
        'foreignkey': []
    },
    {
        'name': 'juzgado',
        'patch': '/home/pdalmasso/Descargas/juzgado.json',
        'foreignkey': []
    },
    {
        'name': 'jurisdiccion',
        'patch': '/home/pdalmasso/Descargas/jurisdiccion.json',
        'foreignkey': []
    },
    {
        'name': 'estado',
        'patch': '/home/pdalmasso/Descargas/estado.json',
        'foreignkey': []
    },
    {
        'name': 'casos',
        'patch': '/home/pdalmasso/Descargas/caso.json',
        'foreignkey': [
            {
                'model_to': 'cliente',
                'related_name': 'cliente',
                'col_from': 'c_id_cliente',
                'col_to': 'idcliente',
            },
            {
                'model_to': 'juzgado',
                'related_name': 'juzgado',
                'col_from': 'c_id_juzgado',
                'col_to': 'idjuzgado',
            },
            {
                'model_to': 'jurisdiccion',
                'related_name': 'jurisdiccion',
                'col_from': 'c_id_jurisdiccion',
                'col_to': 'idjurisdiccion',
            },
            {
                'model_to': 'estado',
                'related_name': 'estado',
                'col_from': 'c_id_estado',
                'col_to': 'idestado',
            },
        ]
    },
]
