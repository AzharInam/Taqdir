import datetime

from .ذرائع import مرکسم۵_جال, مرکسم۵, ناسا
from .ذریعہ import ذریعہ
from .کوائف import کوائف


class مقام(object):
    """
    ایک مقام، جیسے آبوہوا کے کوائف چاہئے۔
    """

    def __init__(خود, چوڑائی, طول, بلندی):
        خود.بلندی = بلندی
        خود.طول = طول
        خود.چوڑانی = چوڑائی

    def کوائف_پانا(خود, سے, تک, ذرائع=None, خاکے='۸۔۵'):
        """
        آبوہوا کے کوائف پانا۔

        Parameters
        ----------
        سے: str | datetime.date
            وہ تاریخ جب سے کوائف چاہئے۔
        تک: str | datetime.date
            وہ تاریخ جب تک کوائف چاہئے۔
        ذرائع: ذریعہ | list
            وہ ذرائع جین میں کہائف ڈھونڈنا ہیے۔ یا :class:`~تقدیر.ذریعہ.ذریعہ`، یا انکے فرست ہو سکتا ہیے۔
        خاکے: str | float
            آبوہوا کی تبدیلی کا خاکے۔

        Returns
        -------
        کوائف
            آبوہوا کے :class:`~تقدیر.کوائف.کوائف`۔

        """
        # ذرائع کی تئیاری
        if ذرائع is None:
            ذرائع = []
        if isinstance(ذرائع, ذریعہ):
            ذرائع = [ذرائع]
        if isinstance(ذرائع, list):
            ذرائع += [ناسا(), مرکسم۵(), مرکسم۵_جال()]

        # ھر ذریعہ کے کوائف پانا
        اعداد = کوائف(None, سے, تک)
        for ذر in ذرائع:
            نئے = ذر.کوائف_پانا(سے, تک, خود.چوڑانی, خود.طول, خود.بلندی, خاکے=خاکے)
            if نئے is not None:
                اعداد += نئے
            # رکنا اگر لاپتہ کچھ نہیں ہیے
            if اعداد.لاپتہ().size == 0:
                break

        return اعداد
