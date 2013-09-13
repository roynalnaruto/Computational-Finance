import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def compare(start_day, start_month, start_year, end_day, end_month, end_year, ls_symbols):

	# Start and End date of the charts
    dt_start = dt.datetime(start_year, start_month, start_day)
    dt_end = dt.datetime(end_year, end_month, end_day)

    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values

    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]

    # Plotting the prices with x-axis=timestamps
    plt.clf()
    fig1 = plt.figure()
    plt.plot(ldt_timestamps, na_normalized_price)
    plt.legend(ls_symbols)
    plt.ylabel('Normalized Close')
    plt.xlabel('Date')
    fig1.autofmt_xdate(rotation=45)
    plt.savefig('normalized_returns.jpg', format='jpg')

    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()

    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)

    # Plotting the scatter plot of daily returns between Company-1 & Company-2
    plt.clf()
    fig2 = plt.figure()
    plt.scatter(na_rets[:, 0], na_rets[:, 1], c='blue')
    plt.ylabel(ls_symbols[0])
    plt.xlabel(ls_symbols[1])
    plt.savefig('scatter1v2.jpg', format='jpg')
