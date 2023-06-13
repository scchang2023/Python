# 將值指派給名為'salutation'、'name'、'product'、'verbed'(過去式動詞)、'room'、
# 'animals'、'percent'、'spokeman'與'job_title'的變數字串。用letter.format()
# 印出使用這些值的信件。
letter="""
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us our recepit and {amount} for shipping and handling.
We will send you anouther {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokeman}
{job_title}
"""
print(letter.format(salutation='01',
                    name='02',
                    product='03',
                    percent='04',
                    verbed='05',
                    room='06',
                    animals='07',
                    amount='08',
                    spokeman='09',
                    job_title='10'
                    )
                )