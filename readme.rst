====================================================================================
Interactive Brokers Python API (Native) - A Step-by-step Guide - AlgoTrading101 Blog
====================================================================================

This is the code used in `Interactive Brokers Python API (Native) <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/>`_ published on the AlgoTrading101 Blog

-----------------
Table of Contents
-----------------

* `What is the Interactive Brokers Python native API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#what-is-ib-python-api-native>`_
* `Why should I learn the IB Python Native API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#why-should-I-learn-ib-python-native-api>`_
* `Why shouldn’t I learn the IB Python Native API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#why-shouldnt-I-learn-ib-python-native-api>`_
* `IB Python native API vs Third Party Libraries (IBridgePy, IbPy etc) <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#ib-python-api-vs-ibridgepy-ibpy>`_
* `How to set up the IB native Python API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#how-to-set-up-the-ib-native-python-api-on-windows>`_
* `How to retrieve the current ask price of Apple’s Stock (AAPL) <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#retrieve-ask-price-aapl>`_
* `Retrieving market data for other assets – EUR/USD, Bitcoin & Gold <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#retrieve-market-data>`_
* `How to retrieve the last 10 hourly candlebars using the native Python API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#retrieve-historical-data>`_
* `What’s the best way to store historical data for later use? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#ib-store-historical-data>`_
* `3 ways to calculate the 20 SMA <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#calculate-moving-average>`_
* `How to fire an order using the native Python API? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#fire-trade-ib-python-api>`_
* `How to implement a stop loss or take profit? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#implement-stop-loss-take-profit>`_
* `How to fire an order for Apple when Google hits a certain price?  <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#how-do-I-use-ib-python-api-price-condition-to-trade>`_
* `How to fire an order for Apple when Google moves more than 5% within the last 5 minutes? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#how-can-I-execute-aapl-trade-when-goog-moves-5-percent>`_
* `How to send notifications via telegram? <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#send-notifications-telegram>`_
* `Common Errors with the IB Python Native API v9.76 <https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/#common-errors-with-ib-python-native-api-v976>`_

------------
Requirements
------------

* `python <https://www.python.org>`_ >= 2.7, 3.4+
* `pandas <https://github.com/pandas-dev/pandas>`_ (tested to work with >= 1.0.3 )
* `requests <https://github.com/psf/requests>`_ (tested to work with >= 2.22.0 )
* `ibapi <https://interactivebrokers.github.io/>`_ (tested to work with >= 9.76.1 )

-----------
Author Info
-----------

:author: Jignesh Davda 
:author page: https://algotrading101.com/learn/author/jdavda/
:published: 2020-02-07
