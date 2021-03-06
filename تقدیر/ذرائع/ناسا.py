from json import JSONDecodeError

import pandas as pd
import requests
from pcse.db import NASAPowerWeatherDataProvider
from تقدیر import متاغیرات
from تقدیر.ذریعہ import ذریعہ


class ناسا(ذریعہ):
    """
    یہ ذریعہ ناسا کے `پنے <https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py>`_ سے آوہوا مشاہدات کے کوائف پاتا ہیے۔
    """

    def _کوائف_بنانا(خود, سے, تک, چوڑائی, طول, بلندی, خاکے):
        try:
            ذریعہ_ناسا = NASAPowerWeatherDataProvider(latitude=چوڑائی, longitude=طول, force_update=False)
        except (requests.exceptions.ConnectionError, KeyError, JSONDecodeError):
            return

        سے = max(ذریعہ_ناسا.first_date, سے)
        تک = min(ذریعہ_ناسا.last_date, تک)

        اعداد_پاندس = pd.DataFrame(columns=list(متاغیرات), index=pd.period_range(سے, تک), dtype=float)

        ستون = {
            'بارش': 'RAIN',
            'شمسی_تابکاری': 'IRRAD',
            'درجہ_حرارت_زیادہ': 'TMAX',
            'درجہ_حرارت_کم': 'TMIN',
            'درجہ_حرارت_اوسط': 'TEMP'
        }

        for تاریخ in اعداد_پاندس.index:
            for س, س_ناسا in ستون.items():
                اعداد_پاندس.loc[تاریخ][س] = getattr(ذریعہ_ناسا(سے), س_ناسا)

        اعداد_پاندس.شمسی_تابکاری *= 1e-6

        return اعداد_پاندس
