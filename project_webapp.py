from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#from vega_datasets import data



COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

df = pd.read_csv("file2.csv")
df = df[["Actor 1", "Actor 2","Actor 3","Year", "Normalised Votes"]]

def multiple_plots(actor_list):
  legend_arr = []
  fig = plt.figure(figsize=(20, 10))
  for actor_name in actor_list:
    df_actor = df[np.array(df["Actor 1"] == actor_name) | np.array(df["Actor 2"] == actor_name) | np.array(df["Actor 3"] == actor_name)]
    legend_arr.append(actor_name)
    #plt.plot(np.arange(len(df_actor['Votes'])) , df_actor['Votes'])
    plt.plot(np.arange(len(df_actor["Normalised Votes"])), df_actor['Normalised Votes'], lw=2)
  plt.legend(legend_arr)
  return fig

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
def symbol_compare(x):
	if (np.any(symbols == x)):
		return True
	else:
		return False

vect_symbol_compare = np.vectorize(symbol_compare)

st.set_page_config(layout="centered", page_icon="🍿", page_title="HSL384 web-app")

# Data visualisation part

st.title("Actors Career Comparision")

source = df
all_symbols = source["Actor 1"]
all_symbols = all_symbols.append(source["Actor 2"])
all_symbols = all_symbols.append(source["Actor 3"])
all_symbols = all_symbols.unique()
symbols = st.multiselect("Choose Actors to visualize", all_symbols, ["Amitabh Bachchan" , "Abhishek Bachchan"])

space(1)

chart = multiple_plots(symbols)
st.pyplot(chart)

space(2)

