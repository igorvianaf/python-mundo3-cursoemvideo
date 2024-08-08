def notas(*args, sit=False):
    """
    Analisando varias notas e situações de alunos
    args = recebe varias notas
    sit = retorna a situação (Aprovado, Em recuperação, Reprovado)
    """

    r = {}
    r['Total de notas'] = len(args)
    r['Maior'] = max(args)
    r['Menor'] = min(args)
    r['Média'] = sum(args)/len(args)
    if sit:
        if r['Média'] <= 5:
            r['Situação'] = 'Reprovado'
        elif 7 > r['Média'] >= 6:
            r['Situação'] = 'Em Recuperação'
        else:
            r['Situação'] = 'Aprovado'
    for k, v in r.items():
        print(f'{k}: {v}') 



boletim = notas(5.5, 2.5, 9, 8.5)
