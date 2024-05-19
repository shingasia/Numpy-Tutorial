from datetime import datetime, timedelta

# ================================================================================================================================
# Timedelta
# timedelta로 datetime 객체의 더하기, 빼기를 수행할 수 있다.
# ================================================================================================================================
a = timedelta(weeks=10, days=5, hours=36, minutes=15, seconds=55, milliseconds=999, microseconds=999)
print(type(a))      # <class 'datetime.timedelta'>
print(a.__str__())  # 76 days, 12:15:55.999999
del a

# 하루 전 시간
delta = datetime.now() - timedelta(1)
print(F'하루 전 시간 : {delta}') # 'YYYY-MM-DD HH:MM:SS.mmmmmm' 형태로 출력된다.
# 2주 전 시간
delta = datetime.now() - timedelta(14)
print(F'2주 전 시간 : {delta}')
# 1년 전/후 시간
delta1, delta2 = datetime.now() - timedelta(1)*365, datetime.now() + timedelta(365) # timedelta() 객체에 상수 곱하기 가능
print(F'1년 전 : {delta1}, 1년 후 : {delta2}')
del delta1, delta2


delta = timedelta(
    weeks=2,
    days=2,
    hours=16,
    minutes=20,
    seconds=30,
    milliseconds=999,
    microseconds=999
)

print(delta)                            # 16 days, 16:20:30.999999
print(F'{delta - timedelta(weeks=3)}')  # -5 days, 16:20:30.999999
print(F'{delta + timedelta(days=-10)}') # 6 days, 16:20:30.999999
print(F'{delta - timedelta(microseconds=999999)}') # 16 days, 16:20:30
# '>':오른쪽 정렬, 'd':정수, 'f':실수
print(F'{delta.days:>15d}')             # 16
print(F'{delta.microseconds:>15d}')     # 999999
print(F'{delta.total_seconds():>15f}')  # 1441230.999999
del delta



# ================================================================================================================================
# Datetime
# strftime() : datetime -> str
# strptime() : str -> datetime
# ================================================================================================================================

stamp = datetime(2024, 5, 1, 22, 59, 59, 999999)
print(F'{type(stamp)}, {stamp}') # <class 'datetime.datetime'>, 2024-05-01 22:59:59.999999

print(stamp.strftime('%Y-%m-%d %H:%M:%S')) # 2024-05-01 22:59:59
print(datetime.strftime(stamp, '%Y-%m-%d') == stamp.strftime('%Y-%m-%d')) # True


stamp = datetime.strptime('2024-03-31 23:59:59.999999', '%Y-%m-%d %H:%M:%S.%f')
print(F'{type(stamp)}, {stamp}') # <class 'datetime.datetime'>, 2024-03-31 23:59:59.999999


# ----------------------------------------------
# %a : 요일 약칭 ✅ Sun, Mon, …, Sat
# %A : 요일 풀네임 ✅ Sunday, Monday, ..., Saturday
# %w : 숫자로 표시된 요일 ✅ 0(일요일), 6(토요일)
# %d : 월의 몇 번째 일자인지 표시 ✅ 01, 02, …, 31
# %b : 월의 약칭 ✅ Jan, Feb, …, Dec
# %B : 월의 풀네임 ✅ January, February, …, December
# %m : 월을 숫자로 ✅ 01, 02, …, 12
# %y : 세기가 없는 2글자 년도 ✅ 00, 01, …, 99
# %Y : 세기를 포함한 4글자 년도 ✅ 0001, 0002, …, 2013, 2014, …, 9998, 9999
# %H : 시간(24-hour clock) ✅ 00, 01, …, 23
# %I : 시간(12-hour clock) ✅ 01, 02, …, 12
# %p : 오전/오후 ✅ AM, PM
# %M : 분(Minute) ✅ 00, 01, …, 59
# %S : 초(Second) ✅ 00, 01, …, 59
# %f : 마이크로초(Microsecond) ✅ 000000, 000001, …, 999999
# %z : UTC offset ✅ (empty), +0000, -0400, +1030, +063415, -030712.345216
# %Z : Time zone 이름 ✅ (empty), UTC, GMT
# %j : 년도의 일(Day of year) ✅ 001, 002, …, 366
# %U : 년도의 주 번호(Week number of the year, 일요일은 주의 첫 번째 날). 새해의 첫 번째 일요일 이전의 모든 날짜는 0주차로 간주 ✅ 00, 01, …, 53
# %W : 년도의 주 번호(Week number of the year, 월요일은 주의 첫 번째 날). 새해의 첫 번째 월요일 이전의 모든 날짜는 0주차로 간주 ✅ 00, 01, …, 53
# %c : 적절한 날짜 및 시간 표현 ✅ Tue Aug 16 21:30:00 1988 (en_US)
# %x : 적절한 날짜 표현 ✅ 08/16/1988 (en_US)
# %X : 적절한 시간 표현 ✅ 21:30:00 (en_US)
# %% : '%'기호 ✅ %
# ----------------------------------------------



# 제너레이터로 range 만들기
def my_date_range(start, end, step = None, /):
    if type(start) != datetime or type(end) != datetime :
        raise TypeError
    if step != None and type(step) != timedelta :
        raise TypeError
    
    next_val = start
    while True :
        if next_val >= end :
            break
        yield next_val
        next_val = next_val + (step if step != None else timedelta(days=1))


print(list(my_date_range(datetime(2023, 1, 1, 0, 0, 0, 0), datetime(2023, 12, 31, 23, 59, 59, 999999), timedelta(days=15)))) # 15일 간격으로
# [datetime.datetime(2023, 1, 1, 0, 0), datetime.datetime(2023, 1, 16, 0, 0), ..., datetime.datetime(2023, 12, 27, 0, 0)]
print(list(my_date_range(datetime(2023, 1, 1, 0, 0, 0, 0), datetime(2023, 1, 1, 23, 59, 59, 0), timedelta(minutes=30)))) # 30분 간격으로
# [datetime.datetime(2023, 1, 1, 0, 0), datetime.datetime(2023, 1, 1, 0, 30), ..., datetime.datetime(2023, 1, 1, 23, 30)]




