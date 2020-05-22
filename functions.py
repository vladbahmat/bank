def from_str_to_bool(buf):
    if buf=='True':
        check=True
        return check
    elif buf=='False':
        check=False
        return check

def int_control():
    while True:
        try:
            n=int(input())
            if n>1000000000:
                raise Exception
            else:
                return n
        except ValueError:
            print('Enter a NUMBER')
        except Exception:
            print("Number can't be more than 1000000000")




text_string="""ШРЕКБАНК ИНКОРПОРЭЙТЭД (ООО БОЛОТО БАНК)
В этом файле представлен отчет о количестве сотрудников банка на данный момент.
Наш банк предоставляет большое количество услуг. И тут очень приятные работяги.
Хорошего вам дня!
Приветсвуем постановку оценки 10 (десять) (ten) Баллов за моой курсач.
"""