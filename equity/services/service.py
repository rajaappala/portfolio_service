
from equity.constants import (EVENT_DATE, NAME, NIFTY_CODE, PRICE, QUANTITY,
                              TRADE_TYPE, TRADED_ON)
from equity.models import Script
from equity.serializer import ScriptDetailSerializer, ScriptSerializer


class ScriptService:

    def __init__(self):
        pass

    def get_script_list(self):
        pass

    def save_script_data(self, request):
        try:
            data = dict(request.data.items())
            name = data.get(NAME, '')
            nifty_code = data.get(NIFTY_CODE, '')
            trade_type = data.get(TRADE_TYPE, '')
            quantity = data.get(QUANTITY, 0)
            price = data.get(PRICE, None)
            traded_on = data.get(TRADED_ON, None)

            if all([name, nifty_code, quantity, price, trade_type, traded_on]):
                script_serilizer = ScriptSerializer(data={
                    NAME: name,
                    NIFTY_CODE: nifty_code
                })
                if script_serilizer.is_valid():
                    script = script_serilizer.save()
                    detail_serializer = ScriptDetailSerializer(data={
                        'script': script,
                        TRADE_TYPE: trade_type,
                        PRICE: price,
                        QUANTITY: quantity,
                        TRADED_ON: traded_on
                    })
                    if detail_serializer.is_valid():
                        detail = detail_serializer.save()
                    else:
                        print(detail_serializer.errors)
                        raise Exception('detail serializer is not valid')
                else:
                    print(script_serilizer.errors)
                    raise Exception('script serializer is not valid')
            else:
                return {
                    'status': 400,
                    'message': "All the parameters are required"
                }
        except Exception as e:
            print(f"exception occured, {e}")
            return {
                'status': 500,
                'message': 'Internal server error occured'
            }
