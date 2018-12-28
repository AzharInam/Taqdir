from .ذرائع import مرکسم۵_جال, مرکسم۵, ناسا
from .کوائف import کوائف
from .ذریعہ import ذریعہ


class مقام(object):

    def __init__(خود, چوڑائی, طول, بلندی):
        خود.بلندی = بلندی
        خود.طول = طول
        خود.چوڑانی = چوڑائی

    def اعدادوشمار_پانا(خود, سے, تک, ذرائع=None, خاکے='۸۔۵ََ'):
        if ذرائع is None:
            ذرائع = []
        if isinstance(ذرائع, ذریعہ):
            ذرائع = [ذرائع]
        if isinstance(ذرائع, list):
            ذرائع += [ناسا(), مرکسم۵(), مرکسم۵_جال()]

        اعداد = کوائف(سے, تک)
        for ذر in ذرائع:
            نئے = ذر.کوائف_پانا(سے, تک, خود.چوڑانی, خود.طول, خود.بلندی, خاکے=خاکے)
            if نئے:
                اعداد += نئے
            if اعداد.لاپتہ().size == 0:
                break
        return اعداد
