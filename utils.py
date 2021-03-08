from requests import get, utils
import time


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    _, content = content.split('Date="')
    code = code.upper()
    if code in content:
        date = time.strptime(content[:content.find('"')], '%d.%m.%Y')
        content = content[content.find(code):]
        content = content[:content.find('</Value>')]
        value = content[content.rfind('>') + 1:].replace(',', '.')
        return float(value.replace(',', '.')), f'{date.tm_year}-{date.tm_mon:02}-{date.tm_mday:02}'
