from ticdat import TicDatFactory

# define table and column names the engine can expect as inputs
input_schema = TicDatFactory(
    parameters=[['Name'], ['Value']]
)

solution_schema = TicDatFactory(
    parameters=[['Name'], ['Value']]
)


def solve(dat):
    assert input_schema.good_tic_dat_object(dat)
    assert not input_schema.find_foreign_key_failures(dat)
    assert not input_schema.find_data_type_failures(dat)
    assert not input_schema.find_data_row_failures(dat)

    sln = solution_schema.TicDat()

    for n, v in dat.parameters.items():
        sln.parameters[n] = v

    return sln
