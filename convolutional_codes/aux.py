import scipy.special
import math


def q_function(x):

	return 0.5 * scipy.special.erfc(x / math.sqrt(2))
