import aux


def hard(sequences, G):

	# the *trellis* for this matrix is obtained
	state_and_input_to_state, state_and_input_to_output = aux.trellis_from_generating_matrix(G)

	# TODO: from G, it is inferred the number of outputs...
	# n_outputs =

	# TODO: ...the possible states...
	# states =

	# TODO: ...and the possible inputs
	# inputs =

	# TODO: number of Viterbi stages is computed from the length of the sequence(s) and the length of the header
	# n_stages =

	# TODO: initialization
	# ...

	# for every stage in the algorithm...
	for i_stage in range(n_stages):

		# for every possible state...
		for i_state, state in enumerate(states):

			# for every possible input...
			for i_input, input in enumerate(inputs):

				# TODO
				pass

	return decoded_sequence

