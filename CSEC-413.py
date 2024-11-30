import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats as stats

class ModelingSimulationApp:
    def __init__(self):
        # Configure Streamlit page
        st.set_page_config(
            page_title="Modeling & Simulation Workflow", 
            page_icon="🔬",
            layout="wide"
        )
