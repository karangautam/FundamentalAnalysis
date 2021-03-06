# FUNDAMENTALS DATA RETRIEVAL

fundamentals_dir = './data/fundamentals/'
fundamentals_filename_glob = 'fundamentals_*.csv'
fundamentals_filename_regex = 'fundamentals_(.*).csv'
def get_fundamentals_filename(ticker):
  return 'fundamentals_' + ticker.upper() + '.csv'

# STOCKS DATA RETRIEVAL

stock_prices_dir = './data/stock_prices/'
stock_prices_ticker_pre_filename_prefix = 'close_prices_pre_2016_02_'
stock_prices_ticker_post_filename_prefix = 'close_prices_post_2016_02_'
def get_stock_prices_pre_2016_02_filename(ticker):
  return stock_prices_ticker_pre_filename_prefix + ticker.upper() + '.csv'
def get_stock_prices_post_2016_02_filename(ticker):
  return stock_prices_ticker_post_filename_prefix + ticker.upper() + '.csv'

quandl_out_shares_db_id = 'RAYMOND'
def get_quandle_outstanding_shares_filename(ticker):
  return 'outstanding_shares_' + quandl_out_shares_db_id + '_' + ticker.upper() + '.csv'
out_shares_filename_glob = 'outstanding_shares_' + quandl_out_shares_db_id + '_*.csv'
out_shares_filename_regex = 'outstanding_shares_' + quandl_out_shares_db_id + '_(.*).csv'
out_shares_filename_prefix = 'outstanding_shares_' + quandl_out_shares_db_id + '_'

# RATIOS CALCULATION

ratios_dir = 'data/calculated_ratios/'
def get_eps_filename(ticker):
  return 'eps_' + ticker.upper() + '.csv'
def get_pe_median_filename(ticker):
  return 'pe_median_' + ticker.upper() + '.csv'
pe_median_filename_glob = 'pe_median_*.csv'
pe_median_filename_regex = 'pe_median_(.*).csv'
def get_peg_filename(ticker):
  return 'peg_' + ticker.upper() + '.csv'
eps_filename_prefix = 'eps_'
pe_median_filename_prefix = 'pe_median_'
peg_filename_prefix = 'peg_'

# GRAPHS

graphs_dir = './graphs/'
def get_tickers_plot_filename(ticker):
  return ticker.upper() + '.png'

