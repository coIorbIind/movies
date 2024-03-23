from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response_data = {
            'status_code': response.status_code,
        }

        reason_text = ''
        if response.data.get('detail'):
            reason_text = response.data['detail']
        else:
            for key, value in response.data.items():
                reason_text += f'{key}: {"; ".join(value)}\n'

        response_data['reason'] = reason_text
        response.data = response_data

    return response
