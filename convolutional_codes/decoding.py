import aux


def hard(sequence, G):

	# *trellis* for this matrix is obtained
	state_and_input_to_state, state_and_input_to_output = aux.trellis_from_generating_matrix(G)

	# TODO
	pass
