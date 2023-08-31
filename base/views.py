from django.shortcuts import render

def inicio(request):
    noticias = []
    dados = ({
        'categoria': 'Politica',
        'titulo': 'Preso Por Corrupção',
        'data': '29/Ago',
        'descricao': '''Lorem ipsum dolor sit amet, 
        consectetur adipiscing elit. Aliquam rutrum tortor a velit auctor sodales. 
        Pellentesque habitant morbi tristique'''
    },
    {
        'categoria': 'Tecnologia',
        'titulo': 'Avanço Tecnológico na Medicina',
        'data': '29/Ago',
        'descricao': '''Nulla volutpat vehicula augue. 
        Maecenas eu nibh eu elit elementum accumsan. 
        Mauris nisi ipsum, vestibulum nec fringilla eu, lobortis'''
    },
    {
        'categoria': 'Esporte',
        'titulo': 'Vitória do XV de Piracicaba',
        'data': '29/Ago',
        'descricao': '''Donec quis massa ut elit interdum congue. 
        Phasellus ultricies aliquet erat id malesuada. 
        Fusce libero nisi, auctor et ullamcorper vel,'''
    })
    noticias.extend(dados)

    return render(request, 'index.html', {'noticias':noticias})

def contato(request):

    return render(request, 'contato.html')

