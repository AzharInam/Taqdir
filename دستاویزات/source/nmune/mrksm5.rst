مرکسم ۵ کا استعمال
==================

مرکسم ۵ آبوہوا کی تبدیلیاں کے خاکے کے لحاس سے آبوہوا کے کوائف دیتا ہیے۔ مرکسم جالبین میں ہیے اور آپ اسکو
آپکے خود کے سںگنک پر بھی تنصیب کر سکتے ہیں۔

تقدیر دونوں سے کوائف ڈھئنڈ سکتا ہیے، پر سنگنک پر ہونے والا مرکسم ھمیشہ جالبین کا مرکسم سے جلدی رہیگا۔ اسی لئے،
اگر آپ مرکسم کے ساتھ بہت کام کرنے والے ہیں، بہتر ہوگا کے مرکسم تنصیب کریں۔

جالبین مرکسم کا استعمال
-----------------------
کچھ بھی کرنے کی زرورت نہیں۔ اگر جالبین دستیاب ہیے، تقدیر کو پتا ہوگا کے کیا کرنا ہیے۔

سنگنک پر مرکسم کا استعمال
-------------------------
پہلہ سے ھی آپکو مرکسم کہ تنصیب کرنے پڑیگا۔ بعاد میں تقدیر کہ بتانا ہیے کے آپکا مرکسم کہاں رکھا ہیے:

.. code-block:: python

    from تقدیر.ذرائع.مرکسم۵ import راستہ_مرکسم_بتانا
    راستہ_مرکسم_بتانا('~میرا/مرکسم/ہیے/یہاں/marksim.exe')

مرکسم کے خاص نمونے
------------------
مرکسم ۵ میں ۱۷ مختلف آبوہوا تبدیلیوں کے نمونے ہیں۔ آم تور پر ہم سارے ۱۷ کا استعمال کریں گے۔
پر اگر آپکو خاص نمونوں کا استعمال کرنا ہیے تو مرکسم کے ذریعے بناتے پر ھی بتا سکتے ہیں
کے آپکو کاون سے نمونے چاہئے۔ یہ جالبین اور سنگنک کے مرکسم دونوں کے لئے چلیگا۔

.. code-block:: python

   from تقدیر.ذرائع import مرکسم۵, مرکسم۵_جال, ناسا
   from تقدیر.مقام import مقام

   میرا_مقام = مقام(چوڑائی=11.02, طول=76.96, بلندی=1)

   نمونہ = '۰۰۰۰۰۱۰۰۰۰۰۰۰۰۰۰۰'
   ذرائع = (مرکسم۵(نمونہ=نمونہ), مرکسم۵_جال(نمونہ=نمونہ), ناسا())
   کو = میرا_مقام.کوائف_پانا(سے='۲۰۵۰۰۱۰۱', تک='۲۰۶۰۰۱۰۱', ذرائع=ذرائع)

