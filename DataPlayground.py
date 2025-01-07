import streamlit as st
import pandas as pd

from ollama import chat
from ollama import ChatResponse
from tools import dfPrinter, scatterPlot, summarize, histogram

st.title("Data playground")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

  prompt = st.text_area(label = "", placeholder = "Enter your prompt here")

  messages = [{'role': 'user', 'content': prompt}]

  available_functions = {
    "dfPrinter": dfPrinter,
    "scatterPlot": scatterPlot,
    "summarize": summarize,
    "histogram":histogram
  }

  response: ChatResponse = chat(
    'llama3.2:1b',
    messages=messages,
    tools=[dfPrinter, scatterPlot, summarize, histogram],
  )

  if response.message.tool_calls:
    # There may be multiple tool calls in the response
    for tool in response.message.tool_calls:
      # Ensure the function is available, and then call it
      if function_to_call := available_functions.get(tool.function.name):
        #Use these two prints parameters for debugging, the first one shows the chosen tool, the second its parameters
        #print('Calling function:', tool.function.name)
        #print('Arguments:', tool.function.arguments)
        function_to_call(**tool.function.arguments)