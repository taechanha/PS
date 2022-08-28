# 초기 설정
# 근무시간
work_time = {
    'start': '2020-01-01 09:00:00',
    'end': '2020-01-01 18:00:00'
}
# 휴일 설정
holidays = ['2020-01-01']
# 평일 근무시간 설정
work_time_weekday = {
    'start': '09:00:00',
    'end': '18:00:00'
}
# 평일 근무시간 설정(휴일)
work_time_weekday_holiday = {
    'start': '09:00:00',
    'end': '18:00:00'
}


def is_holiday(date):
    """휴일 여부 확인"""

    if date in holidays:
        return True

    return False


def is_night(date):
    """야간 여부 확인"""

    if date.hour >= 22 or date.hour < 6:
        return True

    return False


def get_work_time(date):
    """근무시간 계산"""

    # 휴일인 경우, 일반 근무시간 대신 휴일 근무시간 사용하여 계산함. (9~18)
    if is_holiday(date):
        work_time = work_time_weekday_holiday

        # 일반 근무시간 대신 휴일 근무시간 사용하여 계산함. (9~18)
    else:
        work_time = work_time_weekday

    # 일반 근무 시작, 끝 시각 변환 (8~18) -> (08~18) -> (08:00~18:00) -> (08:00:00~18:00:00) -> datetime.datetime() -> (minutes)

    # 리턴 : (minutes)
    pass


def get_overtime(date):
    """overtime pay"""

    # get_work_time() : (minutes)

    # overtime pay : (minutes) * 0.5 * wage = (money)

    pass


def get_night(date):
    """night allowance"""

    # is_night() : bool()

    # get_work_time() : int() (minutes) * 0.5 * wage = (money)

    pass


def get_holiday(date):
    """holiday allowance"""

    # is_holiday() : bool()

    # get_work_time() : int() (minutes) * 0.5 * wage = int() (money)

    pass


def get_holiday_overtime(date):
    """holiday overtime pay"""

    # is_holiday() : bool()

    # get_work_time() : int() (minutes) * 0.5 * wage = (money)

    pass


def get_pay(date):
    """총 급여 계산"""

    # get_overtime() : (money)
    # get_night() : (money)
    # get_holiday() : (money)
    # get_holiday_overtime() : (money)

    # 총 급여 : (money)

    pass


if __name__ == '__main__':
    # 근무시간
    work_time = {
        'start': '2020-01-01 09:00:00',
        'end': '2020-01-01 18:00:00'
    }

    # 휴일 설정
    holidays = ['2020-01-01']

    # 평일 근무시간 설정
    work_time_weekday = {
        'start': '09:00:00',
        'end': '18:00:00'
    }

    # 평일 근무시간 설정(휴일)
    work_time_weekday_holiday = {
        'start': '09:00:00',
        'end': '18:00:00'
    }

    # 급여 계산
    pay = get_pay(work_time)

    print(pay)


usual_pay_day = 0
def get_pay(montly_work_info):
    pay = 0
    for daily_work_info in montly_work_info:
        if did_overwork(daily_work_info): pay += usual_pay_day*1.5
        if did_nightwork(daily_work_info): pay += usual_pay_day*1.5
        if is_holiday(daily_work_info): pay += usual_pay_day*1.5

def did_overwork(work_info):
    """초과 근무 여부"""
    pass
def did_nightwork(work_info):
    """야간 근무 여부"""
    pass
def is_holiday(work_info):
    """휴일 여부"""
    pass
def get_work_time(work_info):
    """근무 시간 확인"""
    pass