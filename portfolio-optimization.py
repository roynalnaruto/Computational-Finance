#The problem at our disposal is:
#Given a set of companies we decided to invest into
#For a particular time period, how would the portfolio perform
#Calculate the ratio of allocations for various cases of interest
#For example: 1. Portfolio with maximum Cumulative return
#             2. Portfolio with maximum returns per volatility (Max Sharpe-ratio)
#The following python code is for case-2 (Maximum Sharpe-ratio)

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():

	#list of symbols of companies
	ls_symbols = ['BRCM', 'ADBE', 'AMD', 'ADI']
	
	#start and end dates 
	dt_start = dt.datetime(2010, 1, 1)
	dt_end = dt.datetime(2010, 12, 31)

	#start of procedure to send in various allocation ratios
	mylist = []
	ls_alloc = []
	average_daily_list = []
	cumulative_list = []
	std_dev_list = []
	sharpe_list = []

	for a in np.arange(0.0, 1.1, 0.1):
		for b in np.arange(0.0, 1.1, 0.1):
			for c in np.arange(0.0, 1.1, 0.1):
				for d in np.arange(0.0, 1.1, 0.1):
					sublist = [a, b, c, d]
					mylist.append(sublist)

	for i in mylist:
		if(sum(i) == 1.0):
			i = [round(elem, 2) for elem in i]
			ls_alloc.append(i)

	for alist in ls_alloc:
		(average_daily, cumulative, std_dev, sharpe_ratio) = simulate(dt_start, dt_end, ls_symbols, alist)
		average_daily_list.append(average_daily)
		cumulative_list.append(cumulative)
		std_dev_list.append(std_dev)
		sharpe_list.append(sharpe_ratio)
	#end of the procedure to send in various allocation ratios

	#find optimized portfolio index and corresponding allocation
	optimize_index = sharpe_list.index(max(sharpe_list))
	optimize_port_alloc = ls_alloc[optimize_index]

	#print all rounded off values
	print("Maximum Sharpe ratio for the chosen Symbols : ")
	print(round(max(sharpe_list), 4))
	print("Portfolio Average daily returns : ")
	print(round(average_daily, 4))
	print("Portfolio Cumuative return : ")
	print(round(cumulative, 4))
	print("Volatility of Portfolio : ")
	print(round(std_dev, 4))
	print("Ratio of allocation for this optimized solution : ")
	print(optimize_port_alloc)
	

def simulate(dt_start, dt_end, ls_symbols, ls_alloc):

	#set the time of day to 16:00
	dt_timeofday = dt.timedelta(hours = 16)
	
	#declare timestamps
	ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

	#get data from Yahoo
	c_dataobj = da.DataAccess('Yahoo')
	
	#list of keys to be taken
	ls_keys = ['open', 'close']
	
	#get the data
	ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
	d_data = dict(zip(ls_keys, ldf_data))

	#get close values
	na_close = d_data['close'].values

	#calculate close values in ratio of allocation
	na_close_port = na_close*ls_alloc

	#calculate daily value for portfolio
	na_rets = [sum(na_close_port[i]) for i in range(len(na_close_port))]

  	#calculate daily returns for portfolio
	na_rets_port = tsu.returnize0(na_rets)

	#calculate cumulative return of portfolio
	cum_return_port = sum(na_rets_port)

	#calculate avg_daily_returns
	avg_daily_returns = np.mean(na_rets_port)

	#calculate standard deviation
	stddev = np.std(na_rets_port)

	#calculate sharpe ratio for portfolio
	sharpe = np.sqrt(252)*avg_daily_returns/stddev

  	#return 4 values
	return(avg_daily_returns, cum_return_port, stddev, sharpe)


if __name__ == '__main__':
	main()
