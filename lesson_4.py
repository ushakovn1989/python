import utils
import sys

is_arg = sys.argv[1:]

if is_arg:
    print(utils.currency_rates(sys.argv[1]))
else:
    print(utils.currency_rates('usd'))
    print(utils.currency_rates('eur'))
