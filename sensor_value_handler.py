from math import ceil, floor

def snap_limits_to_sensor_accuracy(supported_safety_limit_checks):
    for safety_param in supported_safety_limit_checks:
        safety_limit_check_dict = supported_safety_limit_checks[safety_param]['limits']
        safety_param_sensor_accuracy = supported_safety_limit_checks[safety_param]['sensor_accuracy']
        safety_limit_check_dict['min'] = safety_param_sensor_accuracy * ceil(safety_limit_check_dict['min'] /
                                                                             safety_param_sensor_accuracy)
        safety_limit_check_dict['max'] = safety_param_sensor_accuracy * floor(safety_limit_check_dict['max'] /
                                                                              safety_param_sensor_accuracy)
    return supported_safety_limit_checks