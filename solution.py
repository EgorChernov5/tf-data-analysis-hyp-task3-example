import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1107380406

def solution(control_sample, test_sample) -> bool:
    t, p = ttest_ind(test_sample, control_sample)
    alpha = 0.02
    if p < alpha:
        return True
    return False
