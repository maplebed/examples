import json
import os

from iopipe.iopipe import IOpipe

iopipe = IOpipe(os.environ['IOPIPE_TOKEN'])

playver = 12

@iopipe.decorator
def handler(event, context):
    body = {
      'message': 'Your function version {} executed successfully!'.format(playver),
      'input': event
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }
    iopipe.log("playver", playver)
    iopipe.log("libhoney", True)
    # iopipe.log("libhoney2", True, False)
    iopipe.log("libhoney", False)
    iopipe.log("subdur", 5.123)
    iopipe.log("kitty", "catty")

    return response
