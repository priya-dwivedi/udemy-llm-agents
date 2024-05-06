## Welcome to the course on LLM-Agents
This Github has all the coding exercises organized by Unit

### Installation
The installation steps are:
1. Git clone this repo - `git clone https://github.com/priya-dwivedi/udemy-llm-agents.git`
2. Move to the current directory - `cd udemy-llm-agents`
3. If using conda - set a new envtt:
  `conda create -n llm_agents`

  `conda activate llm_agents`

  `conda install pip`

3. Install the dependencies - `pip install -r requirements.txt`
4. Add an environment file called `*.env`
5. Add your keys to the env file

### Unit 1- Foundation of LLM agents
This unit focuses on components of an LLM Agent and building your first simple agent
Coding Exercise for the first Self-Ask Agent:
- Run Locally using Notebook: [First-Agent.ipynb](./Unit1-Foundation_LLM_Agents/My_First_Agent.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TMRYeWTi7hN1vBH5Y8hn95sIF92rhEH-?usp=sharing)


### Unit 2- LLM Tools
This unit focuses on integrating external tools into an Agent
Coding Exercise for the second unit on Tools:
1. Langchain Tools
- Run Locally using Notebook: [Langchain-Tools.ipynb](./Unit2-Tools/Langchain-tools.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yHxctap6bQeNgHJN3nLmHlyg7buFX3LA?usp=sharing)

2. LLM RestAPI tool selection
- Run Locally using Notebook: [LLM-RestAPI-Selection.ipynb](./Unit2-Tools/LLM_RestAPI_Selection.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1f7rgCsAuNsWbvgd0BFuIHwYgU4MAziMh?usp=sharing)

3. OpenAI Function Calling
- Run Locally using Notebook: [OpenAI-Function-Calling.ipynb](./Unit2-Tools/OpenAI-Function-Calling.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rWZqczP4dBiYWSryHBstSVBkoGflhCJi?usp=sharing)

### Unit 2- Memory 
This unit focuses on different types of memory and integrating memory into the Agent
Coding Exercise for the third unit on Memory:
1. Langchain Short term Memory
- Run Locally using Notebook: [Langchain-Short-term-memory.ipynb](./Unit3-Memory/Langchain-Short-term-Memory.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

2. RAG pipeline and RAG compared to Long Context LLMs
- Run Locally using Notebook: [RAG_vs_LongContext.ipynb](./Unit3-Memory/RAG_vs_LongContext.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Vv39cL0DTwxy1WJB2w2VBFbvh7FuDjxi?usp=sharing)

3. Simple Multimodal RAG
- Run Locally using Notebook: [OpenAI-Function-Calling.ipynb](./Unit2-Tools/OpenAI-Function-Calling.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rWZqczP4dBiYWSryHBstSVBkoGflhCJi?usp=sharing)

4. Knowledge-Agent
Can only be run locally
Instructions:
* Navigate to the correct directory: `cd Unit3-Memory/knowledge-agent`
* Optionally: Delete current profile : `rm current_profile.json`
* Run Streamlit interface: `streamlit run chatbot.py`