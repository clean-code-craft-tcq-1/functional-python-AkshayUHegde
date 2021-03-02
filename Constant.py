SUPPORTED_SAFETY_LIMIT_CHECKS = { # sensor accuracies are defined in the same units as the limits
    'cell_temperature_in_celsius': {'limits': {'min': 0, 'max': 45}, 'sensor_accuracy': 2},
    'soc_in_percent': {'limits': {'min': 25, 'max': 75}, 'sensor_accuracy': 1},
    'charge_rate_in_c_rate': {'limits': {'min': 0.5, 'max': 0.8}, 'sensor_accuracy': 0.1}
    # Can add more values in the above format if required, ideally store in DB
}