def parse(query: str) -> dict:
    parse_url = {}
    if "?" not in query:
        return parse_url
    params = query.split("?", 1)[-1]
    if not params or not params[0].isalnum():
        return parse_url
    if "&" not in params and "=" in params:
        name_or_color = params.split("=", 1)
        if name_or_color[0]:
            return {f'{name_or_color[0]}': "".join(name_or_color[1:])}
    elif "&" in params or "=" in params:
        for i in params.split("&"):
            if i:
                parse_url[i.split('=', 1)[0]] = i.split('=', 1)[1]
    return parse_url


if __name__ == '__main__':
     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
     assert parse('http://example.com/') == {}
     assert parse('http://example.com/?') == {}
     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
     assert parse('http://example.com/?name=?&color=?') == {'name': '?', 'color': '?'}
     assert parse('https://example.com/path/to/page?name=ferret&color=purple&model=pxp2') == {'name': 'ferret',
                                                                                              'color': 'purple',
                                                                                              'model': 'pxp2'}
     assert parse('http://example.com/?name=') == {'name': ''}
     assert parse('http://example.com/?&') == {}
     assert parse('https://example.com/path/to/page?color=color') == {'color': 'color'}
     assert parse('https://example.com/path/to/page?name=color') == {'name': 'color'}
     assert parse('https://example.com/path/to/page?color') == {}
     assert parse('https://example.com/path/to/page?=') == {}
     assert parse('https://example.com/path/to/page?=?&') == {}
     assert parse('https://example.com/path/to/page?name==color') == {'name': '=color'}
     assert parse('https://example.com/path/to/page?name=ferret&color=purple&model=pxp2&year=2010') == {'name': 'ferret',
                                                                                              'color': 'purple',
                                                                                              'model': 'pxp2',
                                                                                              'year': '2010'
                                                                                              }


def parse_cookie(query: str) -> dict:
    cookie = {}
    if not ";" in query and "=" in query:
        cookie[f'{query.split("=", 1)}'] = query.split("=", 1)[1]
    elif ";" in query and "=" in query:
        for i in query.split(";"):
            if i and "=" in i:
                if i.split("=", 1)[1] and i.split("=", 1)[0]:
                    cookie[i.split("=", 1)[0]] = i.split("=", 1)[1]
    return cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=28=;') == {'name': 'Dima', 'age': '28='}
    assert parse_cookie('name==Dima;age=28;') == {'name': '=Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;gender=male') == {'name': 'Dima',
                                                            'age': '28',
                                                            'gender': 'male'}
    assert parse_cookie('name=Dima;age=28;gender=male;profession=programmer') == {'name': 'Dima',
                                                            'age': '28',
                                                            'gender': 'male',
                                                            'profession': 'programmer'}
    assert parse_cookie('name=;age=28;') == {'age': '28'}
    assert parse_cookie('name=age=28;age=') == {'name': 'age=28'}
    assert parse_cookie('name=age=28;age=') == {'name': 'age=28'}
    assert parse_cookie('name=;age=') == {}
    assert parse_cookie('name=Di=ma;age=') == {'name': 'Di=ma'}
    assert parse_cookie('name=name;age=age') == {'name': 'name', 'age': 'age'}
    assert parse_cookie('name=name;age=age;=name') == {'name': 'name', 'age': 'age'}

