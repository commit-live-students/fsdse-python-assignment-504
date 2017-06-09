import pandas as pd
import numpy as np


def solution(exam_data, labels):
    df = pd.DataFrame(exam_data, index=labels)
    color = ['Red', 'Blue', 'Orange', 'Red', 'White', 'White', 'Blue', 'Green', 'Green', 'Red']
    #Enter Code Here