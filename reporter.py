def report_parameters(battery_param_name, battery_param_status):
    if battery_param_status.startswith('ALERT'):
        # Can send email Printing for demo purposes
        print(f'ALERT: Battery operating in unsafe parameters! {battery_param_name} is '
              f'{battery_param_status.split("_")[1]}!')
        return False
    else:
        # Can log to local file. Printing for demo purposes
        print(f'LOG: {battery_param_name} is OK.')
        return True