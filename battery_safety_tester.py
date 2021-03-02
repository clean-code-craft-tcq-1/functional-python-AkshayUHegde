from math import isnan
from Constant import SUPPORTED_SAFETY_LIMIT_CHECKS
from reporter import report_parameters
from sensor_value_handler import snap_limits_to_sensor_accuracy


def check_battery_param_limits(battery_param_name, battery_param_value):
    if battery_param_value <= SUPPORTED_SAFETY_LIMIT_CHECKS[battery_param_name]['limits']['min']:
        return 'ALERT_UNDERLIMIT'
    elif battery_param_value >= SUPPORTED_SAFETY_LIMIT_CHECKS[battery_param_name]['limits']['max']:
        return 'ALERT_OVERLIMIT'
    return 'OK'


def check_battery_param_safety(battery_param_name, battery_param_value):
    if isnan(battery_param_value):
        return 'ALERT_VALUENAN'
    elif battery_param_name not in SUPPORTED_SAFETY_LIMIT_CHECKS:
        return 'ALERT_PARAMNAMEUNKNOWN'
    return check_battery_param_limits(battery_param_name, battery_param_value)


def check_overall_battery_safety(**all_battery_params):
    snap_limits_to_sensor_accuracy(SUPPORTED_SAFETY_LIMIT_CHECKS)
    all_battery_params_status = []
    for battery_param_name in all_battery_params:
        battery_param_status = check_battery_param_safety(battery_param_name, all_battery_params[battery_param_name])
        battery_param_status = report_parameters(
            battery_param_name,
            battery_param_status
        )
        all_battery_params_status.append(battery_param_status)
    return all(all_battery_params_status)