'''
Script for plotting the EEG file of patients using plotly
'''
import plotly.plotly as py

import plotly
from plotly import tools
from plotly.graph_objs import Layout, Scatter, Annotation, Annotations, Data, Figure, Marker, Font
from plotly.graph_objs.layout import YAxis

import warnings
warnings.filterwarnings("ignore")

from read_file import read_edf


def plot_file(files):
    for item, index in file:
            