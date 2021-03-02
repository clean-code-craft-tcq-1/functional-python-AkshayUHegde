from battery_safety_tester import check_battery_param_safety, check_overall_battery_safety
from sensor_value_handler import snap_limits_to_sensor_accuracy

if __name__ == '__main__':
    assert (check_overall_battery_safety(cell_temperature_in_celsius=25,
                                         soc_in_percent=70.123456,
                                         charge_rate_in_c_rate=0.7) is True)
    assert (check_overall_battery_safety(cell_temperature_in_celsius=50,
                                         soc_in_percent=85,
                                         charge_rate_in_c_rate=0) is False)
    assert (check_battery_param_safety("cell_temperature_in_celsius", float("nan")) == 'ALERT_VALUENAN')
    assert (check_battery_param_safety("soh_in_percent", 50) == 'ALERT_PARAMNAMEUNKNOWN')
    assert (check_battery_param_safety("cell_temperature_in_celsius", 55) == 'ALERT_OVERLIMIT')
    assert (check_battery_param_safety("soc_in_percent", 15) == 'ALERT_UNDERLIMIT')
    assert (snap_limits_to_sensor_accuracy({'test_value':{'limits': {'min': 0, 'max': 45},
                                                          'sensor_accuracy': 2}})['test_value']['limits']['max'] == 44)