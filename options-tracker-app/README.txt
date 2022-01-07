Options Tracker App:

The goal of the options trading app is to query options charts and list the top 25 stocks based on "PREMIUM-ALGO".
The premium-algo is the following algorithm:
  a = strike price
  b = premium
  c = (b/a)*100 formatted as %
  d = c grouped by expiration date and option type (PUT or CALL) and sorted by b
  
Sample output:

|  Rank  |  Ticker  |  Strike  |  Premium  |  Premium %  |  Expiration Date  |  Type  |
|    1   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    2   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    3   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    4   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    5   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    6   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    7   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    8   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
|    9   |   ABC    |    15    |    1.43   |    9.53%    |    01/28/2022     |   PUT  |
                                  ......
