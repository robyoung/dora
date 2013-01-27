from __future__ import division
import numpy as np
import pandas as pd

def single_exp(alpha=0.5):
    """
    Create a function to calculate the exponential moving average

    See: http://en.wikipedia.org/wiki/Exponential_smoothing#The_exponential_moving_average

    alpha: Smoothing factor 0.0 - 1.0 (0.0 no memory, 1.0 no smoothing)
    """
    single_exp.first = True
    
    def single_exp_inner(window):
        if single_exp.first:
            single_exp.first = False
            single_exp.st = window[0]
        else:
            single_exp.st = alpha * window[-1] + (1 - alpha) * single_exp.st
    
        return single_exp.st

    return single_exp_inner

def double_exp(alpha=0.5, beta=0.5):
    """
    Create a function to calculate the double exponential moving average

    See: http://en.wikipedia.org/wiki/Exponential_smoothing#Double_exponential_smoothing

    alpha: Smoothing factor
    """
    double_exp.first = True
    
    def double_exp_inner(window):
        if double_exp.first:
            double_exp.first = False
            double_exp.st = window[0]
            double_exp.bt = window[1] - window[0]
        else:
            st = alpha * window[-1] + (1-alpha) * (double_exp.st + double_exp.bt)
            bt = beta * (st - double_exp.st) + (1-beta) * double_exp.bt
    
            double_exp.st = st
            double_exp.bt = bt
    
        return double_exp.st

    return double_exp_inner


def _calculate_initial_trend(series, period):
    return sum(series.ix[period+i] - series.ix[i] for i in range(period)) / period ** 2

def _calculate_seasonal_indices(series, period, seasons):
    seasonal_averages = np.zeros(seasons)
    seasonal_indices  = np.zeros(period)

    averaged_observations = np.zeros(len(series))

    for i in range(seasons):
        for j in range(period):
            seasonal_averages[i] += series[(i * period) + j]
        seasonal_averages[i] /= period

    for i in range(seasons):
        for j in range(period):
            averaged_observations[(i * period) + j] = series[(i * period) + j] / seasonal_averages[i]

    for i in range(period):
        for j in range(seasons):
            seasonal_indices[i] += averaged_observations[(j * period) + i]
        seasonal_indices[i] /= seasons

    return seasonal_indices

def tripple_exp(series, period, alpha=0.4, beta=0.4, gamma=0.4):
    seasons = len(series) // period

    St = np.zeros(len(series))
    St[1] = series.ix[0]
    Bt = np.zeros(len(series))
    Bt[1] = _calculate_initial_trend(series, period)
    It = np.ones(len(series))
    It[:period] = _calculate_seasonal_indices(series, period, seasons)

    for i in range(2, len(series)):
        if (i - period) >= 0:
            St[i] = alpha * series.ix[i] / It[i - period] + (1.0 - alpha) * (St[i - 1] + Bt[i - 1])
        else:
            St[i] = alpha * series.ix[i] + (1.0 - alpha) * (St[i - 1] + Bt[i-1])

        Bt[i] = gamma * (St[i] - St[i - 1]) + (1 - gamma) * Bt[i - 1]

        if (i - period) >= 0:
            It[i] = beta * series.ix[i] / St[i] + (1.0 - beta) * It[i - period]

    return pd.Series(St, index=series.index)

    # i = 0
    # def applicator(value):
    #     if i <
    #     i += 1

    # return seasons.apply(applicator)


def tripple_exp2(L, alpha=0.4, beta=0.4, gamma=0.4):
    """
    Create a function to calculate the tripple exponential moving average

    See: http://en.wikipedia.org/wiki/Exponential_smoothing#Triple_exponential_smoothing

    
    """
    tripple_exp.first = True
    tripple_exp.ct = np.ones(L)
    tripple_exp.ct_i = 0
    
    def tripple_exp_inner(window):
        if tripple_exp.first:
            tripple_exp.first = False
            tripple_exp.st = window[-1]
            tripple_exp.bt = (window[-2] - window[-1])
            ct = 1.0
        else:
            cti = tripple_exp.ct[tripple_exp.ct_i]
    
            st = alpha * (window[-1] / cti) + (1 - alpha) * (tripple_exp.st + tripple_exp.bt)
            bt = beta * (st - tripple_exp.st) + (1 - beta) * tripple_exp.bt
            ct = gamma * (window[-1] / st) + (1 - gamma) * cti
    
            tripple_exp.st = st
            tripple_exp.bt = bt
            tripple_exp.ct[tripple_exp.ct_i] = ct
            tripple_exp.ct_i = (tripple_exp.ct_i + 1) % L
    
        return tripple_exp.st
    
    return tripple_exp_inner