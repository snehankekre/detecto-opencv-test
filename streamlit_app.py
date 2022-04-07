import streamlit as st

try:
  from detecto import core, utils, visualize
  st.success("Yay!")
except ImportError as err:
  st.exception(err)
