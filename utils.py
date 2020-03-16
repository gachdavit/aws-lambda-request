import json
import typing

def get_http_request_dict(event: typing.Dict) -> typing.Union[typing.Dict, typing.NoReturn]:
    if event['httpMethod'] == 'GET':
        query_string = event['queryStringParameters']
        return_dict = query_string if query_string else {}
    elif event['httpMethod'] in ('POST', 'PUT'):
        body = event['body']
        return_dict = json.loads(body) if body else {}
    else:
        raise NotImplementedError('''
            get_http_request_dict() can handle and parse only HTTP GET/POST/PUT requests.
        ''')
    return return_dict

def render_to_response(
        status_code: int = 200, 
        data: typing.Optional[typing.Dict] = {}
    ) -> typing.Dict:
    response = {
        'statusCode': status_code,
        'body': json.dumps(data)
    }
    return response