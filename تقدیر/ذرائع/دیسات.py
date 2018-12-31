import datetime

import pandas as pd
from تقدیر.ذریعہ_نکتہ import ذریعہ_نکتہ

from tradssat import WTHFile, MTHFile


class دیسات(ذریعہ_نکتہ):

    def __init__(خود, مسل, خاکے=None):
        خود.مسل = مسل
        خود.کوائف_دیسات = WTHFile(خود.مسل)

        چوڑائی = خود.کوائف_دیسات.get_value('LAT')
        طول = خود.کوائف_دیسات.get_value('LONG')
        بلندی = خود.کوائف_دیسات.get_value('ELEV')
        super().__init__(چوڑائی, طول, بلندی, خاکے)

    def _کوائف_بنانا(خود, سے, تک, چوڑائی, طول, بلندی, خاکے):
        return دیسات_سے_پڑھنا(خود.کوائف_دیسات, سال=None)


class دیسات_ماھانہ(ذریعہ_نکتہ):

    def __init__(خود, مسل, چوڑائی, طول, بلندی, خاکے=None):
        خود.مسل = مسل
        خود.کوائف_دیسات = MTHFile(خود.مسل)

        super().__init__(چوڑائی, طول, بلندی, خاکے)

    def _کوائف_بنانا(خود, سے, تک, چوڑائی, طول, بلندی, خاکے):
        ستون = {
            'بارش': 'ramn',
            'شمسی_تابکاری': 'srmn',
            'درجہ_حرارت_زیادہ': 'txmn',
            'درجہ_حرارت_کم': 'tnmn',
        }
        اعداد = {س: خود.کوائف_دیسات.get_value(مت) for س, مت in ستون.items()}
        سال = خود.کوائف_دیسات.get_value('yr')
        مہینہ = خود.کوائف_دیسات.get_value('mo')
        return pd.DataFrame(
            اعداد,
            index=pd.PeriodIndex([str(س) + str(م).rjust(2, '0') for س, م in zip(سال, مہینہ)], freq='M')
        )


def دیسات_سے_پڑھنا(مسل, سال):
    ستون = {
        'بارش': 'RAIN',
        'شمسی_تابکاری': 'SRAD',
        'درجہ_حرارت_زیادہ': 'TMAX',
        'درجہ_حرارت_کم': 'TMIN',
    }

    اعداد = {س: [] for س in ستون}
    تاریخیں = []

    for ش, تاریخ in enumerate(مسل.get_value('DATE')):
        سال = سال or 2000 + int(str(تاریخ)[:2])
        اسلی_تاریخ = datetime.date(سال, 1, 1) + datetime.timedelta(days=int(str(تاریخ)[-3:]) - 1)

        تاریخیں.append(اسلی_تاریخ)

        for مت, مت_دیسات in ستون.items():
            اعداد[مت].append(مسل.get_value(مت_دیسات)[ش])

    return pd.DataFrame(اعداد, index=pd.PeriodIndex(تاریخیں, freq='D'))
