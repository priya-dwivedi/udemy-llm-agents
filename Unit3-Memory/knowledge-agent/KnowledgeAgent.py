
import os
import json
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") ## Put your OpenAI API key here
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY") ## Put your Tavily Search API key here
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") ## Put your Langsmith API key here
os.environ["LANGCHAIN_HUB_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") ## Put your Langsmith API key here
os.environ["LANGCHAIN_TRACING_V2"] = 'true' ## Set this as True
os.environ["LANGCHAIN_ENDPOINT"] = 'https://api.smith.langchain.com/' ## Set this as: https://api.smith.langchain.com/
os.environ["LANGCHAIN_HUB_API_URL"] = 'https://api.hub.langchain.com' ## Set this as : https://api.hub.langchain.com
os.environ["LANGCHAIN_PROJECT"] = 'llm-agents-memory'

## Add Together API Key
os.environ["TOGETHER_API_KEY"] = os.getenv("TOGETHER_API_KEY")

### import together
from together_llm import TogetherLLM

### Langchain imports
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory


class Memory:
    def __init__(self, model='meta-llama/Llama-3-8b-chat-hf', temperature=0.1, max_tokens=256):
        self.llm_memory = TogetherLLM(model=model, temperature=temperature, max_tokens=max_tokens)
        self.system_message = ''' You are an expert at extracting relevant details from the user message and adding them to the profile.
        Your current profile has information about a person and their interests or dislikes.
        Example can be:
        Dad: Likes to do gardening. Loved the shovel I bought him last year

        When you get a new message, you can do one of the following:

        1. Do nothing. No interesting information was presented
        2. Update the current profile for a person. If someone's likes/dislikes change, then keep track of that
        3. Add a new person to the Current Profile. If a new person is mentioned, then keep track of that
        4. Remove a person from the Current Profile. If someone is mentioned as no longer being relevant, then remove them from the profile. 

        Important: When you are done, return the Current Profile as a JSON in the format below.
        Below is an example of the profile. Not the actual one.
        {{
        "Dad" : "Likes Gardening. Loved the shovel gifted last year",
        "Mom" : "Has birthday in July. loves hiking"
        }}
        VERY IMPORTANT: ONLY return the JSON output. If you have no profile return None. Don't return any text or explanations

        Current Profile: {current_profile}

        New Message: {input}
        '''

    def load_json_file(self, file_path):
        """Load a JSON file from the given file path or return None if not present or on error."""
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading JSON file: {e}")
        else:
            print(f"No file found at {file_path}")
        return {}

    def run(self, input):
        prompt = PromptTemplate(
        input_variables=["current_profile", "input"], template=self.system_message)

        # Create an LLMChain using the custom LLM
        memory_agent = LLMChain(llm=self.llm_memory, prompt=prompt)

        current_profile = self.load_json_file('current_profile.json')
        ## Run the chain and return results
        result = memory_agent.invoke({'input':input,  "current_profile": current_profile})
        print("Memory Agent Output: ", result['text'])
        try:
            output = json.loads(result['text'])

            ## Save this to profile file
            with open('current_profile.json', 'w') as file:
                json.dump(output, file)
        except:
            print("LLM message was not in JSON format. Is not being saved")
        return result


class Chatbot:
    def __init__(self, model='gpt-4-turbo-preview', temperature=0.3):
        self.llm_rec = ChatOpenAI(model=model, temperature=temperature, model_kwargs={"response_format": {"type": "json_object"}})
        self.system_prompt = ''' You are an expert at recommending gifts based on the person's profile/likes and dislikes.
            You use the web search tool you have to do a web search and select gifts based on likes/dislikes/budget.
            You also have access to a everyone's current profile which stores long term information about everyone. If present use this, else proceed on your own.
            You respond in JSON format in the key response. Don't respond as a string. Example:
            {{'response': 'If your dad likes gardening then buy them a nice shovel which will cost around $25'}}
            Don't ask the user questions. Just respond with what you have.
            '''
        self.memory = ChatMessageHistory(session_id="test-session")
        self.tools = [TavilySearchResults(max_results=1)]

    def load_json_file(self, file_path):
        """Load a JSON file from the given file path or return None if not present or on error."""
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading JSON file: {e}")
        else:
            print(f"No file found at {file_path}")
        return {}
    
    def run(self, input):
        ## Load Current Profile
        current_profile = self.load_json_file('current_profile.json')

        prompt_rec = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
            content=self.system_prompt
        ),
          MessagesPlaceholder(variable_name="chat_history"),   
          MessagesPlaceholder(variable_name="agent_scratchpad"),

         ("user", " Current profile for everyone is: {current_profile}"),
         ("user", " Now help me with suggestions for: {input}. Use the search tool provided to you to get information"),            
        ]
    )
        # Construct the OpenAI Functions agent
        recommendation_agent = create_openai_tools_agent(self.llm_rec, self.tools, prompt_rec)
        agent_executor = AgentExecutor(agent=recommendation_agent, tools=self.tools)
        agent_with_chat_history = RunnableWithMessageHistory(
            agent_executor,
            # This is needed because in most real world scenarios, a session id is needed
            # It isn't really used here because we are using a simple in memory ChatMessageHistory
            lambda session_id: self.memory,
            input_messages_key="input",
            history_messages_key="chat_history",
        )
        result = agent_with_chat_history.invoke({'input': input, 'current_profile': current_profile}, config={"configurable": {"session_id": "1234"}})
        print("Result from the recommendation agent: ", result)
        return result['output']

if __name__=="__main__":
    memory_agent = Memory(model='meta-llama/Llama-3-8b-chat-hf', temperature=0.2)
    memory_agent.run("My mom likes to bake. She is passionate of making bread")

    rec_agent = Chatbot()
    result = rec_agent.run("Can you recommend some kitchen mixers for my mom")
    print(result)