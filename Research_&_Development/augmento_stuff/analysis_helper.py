import numpy as np


def nb_safe_divide(a, b):
	# divide each element in a by each element in b
	# if element b == 0.0, return element = 0.0
	c = np.zeros(a.shape[0], dtype=np.float64)
	for i in range(a.shape[0]):
		if b[i] != 0.0:
			c[i] = a[i] / b[i]
	return c

def strip_data_by_time(t_data, data, t_min, t_max):
	data = np.array([s for s, t in zip(data, t_data) if t >= t_min and t <= t_max])
	t_data = np.array([t for t in t_data if t >= t_min and t <= t_max])
    
	return t_data, data

def nb_causal_rolling_norm(arr, window_size):
	
	# create an output array
	out_arr = np.zeros(arr.shape[0])
	
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size-1) * arr[0], arr))
	
	# for each output element, find the mean and std of the last few
	# input elements, and standardise the input element by the mean and std of the window
	#for i in nb.prange(out_arr.shape[0]):
	for i in range(out_arr.shape[0]):
			num = new_arr[i+window_size-1] - np.mean(new_arr[i : i + window_size])
			denom = np.max(np.abs(new_arr[i : i + window_size] - np.mean(new_arr[i : i + window_size])))
			if denom != 0.0:
					out_arr[i] = num / denom
	
	return out_arr

def nb_causal_rolling_average(arr, window_size):
	
	# create an output array
	out_arr = np.zeros(arr.shape[0])
	
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size-1) * arr[0], arr))
	
	# for each output element, find the mean of the last few input elements
	#for i in nb.prange(out_arr.shape[0]):
	for i in range(out_arr.shape[0]):
		out_arr[i] = np.mean(new_arr[i : i + window_size])
	
	return out_arr

def nb_causal_rolling_sd(arr, window_size):
	
	# create an output array
	out_arr = np.zeros(arr.shape[0])
	
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size-1) * arr[0], arr))
	
	# for each output element, find the mean and std of the last few
	# input elements, and standardise the input element by the mean and std of the window
	#for i in nb.prange(out_arr.shape[0]):
	for i in range(out_arr.shape[0]):
		num = new_arr[i+window_size-1] - np.mean(new_arr[i : i + window_size-1])
		denom = np.std(new_arr[i : i + window_size-1])
		if denom != 0.0:
			out_arr[i] = num / denom
	
	return out_arr

def nb_causal_rolling_sd_rand(arr, window_size_rand):
	
	# create an output array               
	out_arr = np.zeros(arr.shape[0])
			
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size_rand-1) * arr[0], arr))
	
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size_rand-1) * arr[0], arr))
	# for each output element, find the mean and std of the last few
	# input elements, and standardise the input element by the mean and std of the window
	#for i in nb.prange(out_arr.shape[0]):
	for i in range(out_arr.shape[0]):
		window_size_std = 1.0
		window_size = round(np.random.normal(window_size_rand, window_size_std))       
		num = new_arr[i+window_size-1] - np.mean(new_arr[i : i + window_size-1])
		denom = np.std(new_arr[i : i + window_size-1])
		if denom != 0.0:
			out_arr[i] = num / denom
	
	return out_arr

def nb_causal_rolling_norm_rand(arr, window_size_rand, peturb):
	
	# create an output array
	out_arr = np.zeros(arr.shape[0])
	
	# create an array from the input array, with added space for the rolling window
	new_arr = np.hstack((np.ones(window_size_rand-1) * arr[0], arr))

	index_new = window_size_rand
	
	# for each output element, find the mean and std of the last few
	# input elements, and standardise the input element by the mean and std of the window
	#for i in nb.prange(out_arr.shape[0]):
	for i in range(out_arr.shape[0]):

		window_size_std = peturb * np.float64(window_size_rand)
		window_size = round(np.random.normal(window_size_rand, window_size_std))

		i_end_new = i + window_size_rand
		i_start_new = i_end_new - window_size

		if i_start_new < 0:
			i_start_new = 0

		out_arr[i] = np.mean(new_arr[i_start_new : i_end_new])
		#print(out_arr[i-1:i+1])

		#num = new_arr[i+window_size-1] - np.mean(new_arr[i : i + window_size])
		#denom = np.max(np.abs(new_arr[i : i + window_size] - np.mean(new_arr[i : i + window_size])))
		#if denom != 0.0:
		#	out_arr[i] = num / denom
	
	return out_arr

def nb_calc_sentiment_score_rand_a(sent_a, sent_b, ra_win_size, std_win_size, peturb):
	# example method for creating a stationary sentiment score based on Augmento data
	
	# compare the raw sentiment values
	sent_ratio = nb_safe_divide(sent_a, sent_b)
	
	# smooth the sentiment ratio
	sent_ratio_smooth = nb_causal_rolling_norm_rand(sent_ratio, ra_win_size, peturb)
	
	# create a stationary(ish) representation of the smoothed sentiment ratio
	sent_score = nb_causal_rolling_sd(sent_ratio_smooth, std_win_size)
	
	return sent_score

def nb_calc_sentiment_score_a(sent_a, sent_b, ra_win_size, std_win_size):
	# example method for creating a stationary sentiment score based on Augmento data
	
	# compare the raw sentiment values
	sent_ratio = nb_safe_divide(sent_a, sent_b)
	
	# smooth the sentiment ratio
	sent_ratio_smooth = nb_causal_rolling_average(sent_ratio, ra_win_size)
	
	# create a stationary(ish) representation of the smoothed sentiment ratio
	sent_score = nb_causal_rolling_sd(sent_ratio_smooth, std_win_size)
	
	return sent_score

def nb_calc_sentiment_score_b(sent_a, sent_b, ra_win_size_short, ra_win_size_long):
	# example method for creating a stationary sentiment score based on Augmento data
	
	# compare the raw sentiment values
	sent_ratio = nb_safe_divide(sent_a, sent_b)
	
	# smooth the sentiment ratio
	sent_ratio_short = nb_causal_rolling_average(sent_ratio, ra_win_size_short)
	sent_ratio_long = nb_causal_rolling_average(sent_ratio, ra_win_size_long)
	
	# create a stationary(ish) representation of the smoothed sentiment ratio
	sent_score = sent_ratio_short - sent_ratio_long
	
	return sent_score

def nb_calc_sentiment_score_c(sent_a, sent_b, ra_win_size, std_win_size):
	# example method for creating a stationary sentiment score based on Augmento data
	
	# compare the raw sentiment values
	sent_ratio = nb_safe_divide(sent_a, sent_b)
	
	# smooth the sentiment ratio
	sent_ratio_smooth = nb_causal_rolling_average(sent_ratio, ra_win_size)
	
	# create a stationary(ish) representation of the smoothed sentiment ratio
	sent_score = nb_causal_rolling_norm(sent_ratio_smooth, std_win_size)
	
	return sent_score

def nb_backtest_a(price, sent_score, start_pnl, buy_sell_fee):
	# example backtest with approximate model for long/short contracts
	
	# create an array to hold our pnl, and set the first value
	pnl = np.zeros(price.shape, dtype=np.float64)
	pnl[0] = start_pnl
	
	# for each step, run the market model
	for i_p in range(1, price.shape[0]):
		
		# if sentiment score is positive, simulate long position
		# else if sentiment score is negative, simulate short position
		# else if the sentiment score is 0.0, hold
		# (note that this is a very approximate market simulation!)
		n_sample_delay = 2
		if i_p < n_sample_delay:
			pnl[i_p] = pnl[i_p-1]
		if sent_score[i_p-n_sample_delay] > 0.0:
			pnl[i_p] = (price[i_p] / price[i_p-1]) * pnl[i_p-1]
		elif sent_score[i_p-n_sample_delay] <= 0.0:
			pnl[i_p] = (price[i_p-1] / price[i_p]) * pnl[i_p-1]
		elif sent_score[i_p-n_sample_delay] == 0.0:
			pnl[i_p] = pnl[i_p-1]
		
		# simulate a trade fee if we cross from long to short, or visa versa
		if i_p > 1 and np.sign(sent_score[i_p-1]) != np.sign(sent_score[i_p-2]):
			pnl[i_p] = pnl[i_p] - (buy_sell_fee * pnl[i_p])
	
	return pnl

def compare_sents(sent_a, sent_b, window_size=1):

	# find the ratio
	s = np.divide(sent_a, sent_b, out=np.zeros_like(sent_a), where=(sent_b != 0))

	# average the data
	if window_size > 1:
		s = causal_rolling_average(s, window_size)

	return s