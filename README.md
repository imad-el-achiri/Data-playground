# Data Playground
A new way to analyze your data! Zero-code natural language interaction! <Br> 
<Br> (A link of a demonstration video will be added here) <Br> <Br>
This agents-based project runs completely locally, no paid LLMs apis (like OpenAI/Gemini) are needed. <Br>
The model used is a 1B llama 3.2, qunatized to 8 bit, which takes ~ 1.5GB of memory. <Br>

## How to setup the project:
<ol>
  <b>
    <li>
      LLM setup by Ollama:
    </li>
  </b>
  
  <ul>
    <li>
      Download and install Ollama (For Windows/MacOS/Linux) from : https://ollama.com/download
    </li>
    <li>
      After installation, restart your computer
    </li>
    <li>
      On the command line/terminal run the following command: <code>ollama run llama3.2:1b </code>
    </li>
  </ul>

  <b>
    <li>
      Python setup:
    </li>
  </b>

  <ul>
    <li>
      Download Python 3.9+ from: https://www.python.org/downloads/
    </li>
    <li>
      Create a virtual environment, by following the instructions for your operating system: https://www.geeksforgeeks.org/python-virtual-environment/
    </li>
    <li>
      Clone or download this project as zip file
    </li>
    <li>
      Open the command line/terminal, navigate to the project directory, activate the virtual environment, then run the command: <code> pip install -r requirements.txt </code>
    </li>
  </ul>

  <b>
    <li>
      Run the project:
    </li>
  </b>

  <ul>
    <li>
      Make sure that Ollama is running
    </li>
    <li>
      Open the command line/terminal, navigate to the project directory, then run the command : <code> streamlit run DataPlayground.py </code>
    </li>
    <li>
      If it does not open automatically, you can access the interface through a web browser at : <code> http://localhost:8501/ </code>
    </li>
    <li>
      Upload your csv file
    </li>
    <li>
      Enjoy prompting!
    </li>
  </ul>
  
</ol>

