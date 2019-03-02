import scipy.special
import math


def q_function(x):

	return 0.5 * scipy.special.erfc(x / math.sqrt(2))


def trellis_from_generating_matrix(G):

	# a dictionary of dictionaries, the keys in the "outer one" being states and those in the "inner" one being inputs,
	# so that `state_and_input_to_state[s][i]` will give you the *state* the machine moves to when it is at state `s`
	# and input `i` is received
	# TODO: this is just an example, not the real thing
	# TODO 2: this is *hardwired* in the code, but this should actually be obtained from G
	state_and_input_to_state = {'00': {'0': '00'}}

	# a dictionary of dictionaries, the keys in the "outer" one being states and those in the "inner" one being inputs,
	# so that `state_and_input_to_output[s][i]` will give you the *output* produced by the machine when it is at state
	# `s` and input `i` is received
	# TODO: see above TODO's
	state_and_input_to_output = {'00': {'0': '01'}}

	return state_and_input_to_state, state_and_input_to_output
