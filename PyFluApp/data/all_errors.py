from datetime import datetime, date


error_historic = dict()

def log_error(where, error, to_return):

    error_historic[str(f'-[{len(error_historic)}]  {date.today()}:')] = (where, error, to_return)

    return (f'\n    [ {to_return} ]\n\n\n'
            f'Acesse:\n'
            f'          https://pythonfluente.com/\n')
