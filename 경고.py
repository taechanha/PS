# 20:00:00
# 04:00:00 08:00:00

# 12:34:56
# 14:36:22 02:01:26

def convert_to_abs(time):
    h = int(time[:2]) * 60 * 60
    m = int(time[3:5]) * 60
    s = int(time[6:])
    return h + m + s


def convert_to_24(time):
    h, r = divmod(time, 60 * 60)
    m, s = divmod(r, 60)
    if int(h) < 10:
        h = "0" + str(h)
    if int(m) < 10:
        m = "0" + str(m)
    if int(s) < 10:
        s = "0" + str(s)
    return str(h) + ":" + str(m) + ":" + str(s)


curr_time = input()
throw_time = input()

abs_curr_time = convert_to_abs(curr_time)
abs_throw_time = convert_to_abs(throw_time)

if abs_curr_time >= abs_throw_time:
    abs_throw_time += 86400

abs_diff_time = abs_throw_time - abs_curr_time

new_24_time = convert_to_24(abs_diff_time)

print(new_24_time)
