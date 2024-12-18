import streamlit as st
from datetime import datetime
import sys
from io import StringIO

from main import *

st.title("Notion - CrewAI Timeblocking Agent")

# Add a button to trigger the CrewAI execution
if st.button("Run CrewAI"):
    # Define inputs for the workflow
    datetime_now = datetime.now()
    inputs = {
        'datetime_now': datetime_now
    }

    with st.spinner("Running CrewAI..."):
        # Kick off the CrewAI workflow with inputs
        results = crew.kickoff(inputs=inputs)

    st.success("CrewAI execution completed!")

    # Display results
    st.write("Results:")
    st.json(results)
