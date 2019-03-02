#! /usr/bin/env python3

import math
import numpy as np
import matplotlib.pylab as plt

# our own stuff
import encoding
import channel
import decoding
import aux

sequence = None

# ----------------------------- parameters

# number of simulated frames (realizations of the transmission)
n_frames = 5

# length of each frame
n_bits_per_frame = 1000

# generating matrix
G = [[1, 0, 1], [1, 1, 1]]

# Eb/N0's (in dBs) to be tested
Eb_N0s_dBs = list(range(12))

# ----------------------------- processing

# a `numpy` array to store every computed BER [<with/without coding>, <EbN0>, <frame>]
BER = np.empty((2, len(Eb_N0s_dBs), len(n_frames)))

# for every simulated frame...
for i_frame in range(n_frames):

	print('processing frame {}'.format(i_frame))

	# TODO: a random sequence of bits is generated
	# sequence = ...

	# the sequence is encoded
	encoded_sequence = encoding.conv_encoding(G, sequence)

	# for every EbN0 to be tested...
	for i_ebn0, ebn0_dbs in enumerate(Eb_N0s_dBs):

		# the EbN0 is converted to natural units
		ebn0 = 10**(ebn0_dbs/10)

		# ================= *with* coding

		# the probability of error is computed from the EbN0
		Pe = aux.q_function(math.sqrt(ebn0))

		# transmission is simulated
		received_sequence = channel.binary_symmetric(encoded_sequence, Pe)

		# decoding
		decoded_sequence = decoding.hard(received_sequence, G)

		# TODO: the BER is computed
		# BER[0, i_ebn0, i_frame] = ...

		# ================= *without* coding

		# the probability of error is computed from the EbN0
		Pe = aux.q_function(math.sqrt(2*ebn0))

		# the simulated sequence is transmitted as is
		received_sequence = channel.binary_symmetric(sequence, Pe)

		# TODO: the BER is computed
		# BER[1, i_ebn0, i_frame] = ...

# average BER over all the frames
average_BER = BER.mean(axis=2)

# TODO: plotting
# plt.semilogy()

# figure is saved
plt.savefig('BER.pdf')
