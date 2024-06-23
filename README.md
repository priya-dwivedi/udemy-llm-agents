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

### Unit 3- Memory 
This unit focuses on different types of memory and integrating memory into the Agent
Coding Exercise for the third unit on Memory:
1. Langchain Short term Memory
- Run Locally using Notebook: [Langchain-Short-term-memory.ipynb](./Unit3-Memory/Langchain-Short-term-Memory.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WAv7GwDHBrI4GZsGwrD0ssXGT8j7G4_q?usp=sharing)

2. RAG pipeline and RAG compared to Long Context LLMs
- Run Locally using Notebook: [RAG_vs_LongContext.ipynb](./Unit3-Memory/RAG_vs_LongContext.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Vv39cL0DTwxy1WJB2w2VBFbvh7FuDjxi?usp=sharing)

3. Simple Multimodal RAG
- Run Locally using Notebook: [MultiModal-RAG.ipynb](./Unit3-Memory/MultiModal_RAG.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yX2r1u_euYuxODzTyoeFPhCtUgymq7Gh?usp=sharing)

4. Knowledge-Agent
Can only be run locally
Instructions:
* Navigate to the correct directory: `cd Unit3-Memory/knowledge-agent`
* Optionally: Delete current profile : `rm current_profile.json`
* Run Streamlit interface: `streamlit run chatbot.py`

### Unit 4-Planning
This unit focuses on different types of planning and how to improve the Agent's accuracy and performance with planning 
Coding Exercise for the fourth unit on Planning:
1. Plannning with task decomposition
- Run Locally using Notebook: [Planning_with_task_decomposition.ipynb](./Unit4-Planning/Planning_with_task_decomposition.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EzQ8-3ubyChDXaX5VRie58Bw5z6hDnkK?usp=sharing)

2. Skeleton of Thought Generation
- Run Locally using Notebook: [Skeleton_of_Thought_Generationa.ipynb](./Unit4-Planning/Skeleton_of_Thought_Generation.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JjgbvuhJdna-6ZgT0MdDOP7iJ-ftcxKr?usp=sharing)

3. Basics of Langgraph
- Run Locally using Notebook: [Basics_of_Langgraph.ipynb](./Unit4-Planning/Basics_of_Langgraph.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UWYtytGMC4UtEE4LoFmVcMbrf0Wke0jn?usp=sharing)

4. Reflection Agent
- Run Locally using Notebook: [Reflection_Agent.ipynb](./Unit4-Planning/Reflection_Agent.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15hi4bAmZflP_Z7pS75FhbbsA8kVkQ2co?usp=sharing)

4. Reflexion Agent
- Run Locally using Notebook: [Reflexion_Agent.ipynb](./Unit4-Planning/Reflexion_Agent.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s0VCGf7nboqoBs-Kh-bi2n6Nlo4smQBc?usp=sharing)

### Unit 5-Agent Examples
This unit focuses on building more complex agents combining everything learned so far in the course
Coding Exercise for the fifth unit on Agent Examples:
1. Agentic-RAG
- Run Locally using Notebook: [Agentic-RAG.ipynb](./Unit5-Agent-Examples/Agentic-RAG.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10V6iHz_qnfXwV2bCgLDeSwUNWw8GgzE6?usp=sharing)

2. Movie Recommendation Bot
Can only be run locally
Instructions:
* Navigate to the correct directory: `cd Unit5-Agent_Examples/Movie_Recommendation_Agent`
* Run Streamlit interface: `streamlit run chatbot.py`

3. Coding Assistant
- Run Locally using Notebook: [Coding-Assistant.ipynb](./Unit5-Agent-Examples/Coding-Assistant.ipynb)
- Run on Colab with Link: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/122G2pJ9f_-01ROt00Hd9WEM_l25P_aN_?usp=sharing)

