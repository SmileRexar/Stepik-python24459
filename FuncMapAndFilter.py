import sys

'''
Примеры работы map и filter
'''
try:
    first_arg, second_arg = map (int,input().split())
except ValueError as e:
    print("Input error. Exception type from {0} {1}".
        format(
        type(e),
        "\nThis Script exit with code is '1'")
        )
    sys.exit(1)
except Exception as e:
    print("Type Error: {0}, Error mess:{1}".format(type(e)), e)
    sys.exit(1)

print("Сумма {0} + {1} = {2}".format(first_arg, second_arg, first_arg+second_arg))


#Пример фильтра
filter_evens=map(int, input('Список на фильтр :').split())

def even(x):
    if(x%2==0):
        return True
    return False

evens=filter(even, filter_evens)
for _ in evens:
    print("Filtered element from list: {}".format(_))
