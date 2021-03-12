from calendar import mdays, month_name
from functools import reduce

meses_31 = list(filter(lambda mes: mdays[mes] == 31, range(1, 13)))
meses_nomes = list(map(lambda mes: month_name[mes], meses_31))
juntar_meses = reduce(lambda todos, nomes_meses:f'{todos}\n- {nomes_meses}',
                      meses_nomes, 'Months with 31 days:')

print(juntar_meses)