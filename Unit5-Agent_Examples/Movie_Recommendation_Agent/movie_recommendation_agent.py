### Langchain imports
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

import pandas as pd


class MovieSelectionTool():

  @tool("Movie_Selector")
  def movie_selector(data):
    """Call this tool to get a list of movies that match the user's criteria.
       The input to this tool is a movie genres, min and max year of the movie.
       All genres should be pipe sepearated and years should be / separated. 
       Example if the user is look for comedy and drama from 1990 to 2000, then input should be `Comedy|Drama/1990/2000`
       Example if the user is looking for Romance, Family and Animation from 1995 to 2005 then input should be: Romance|Family|Animation/1995/2005
       The output from this tool will be all the movies that match that criteria
    """
    try:
      genres_piped, min_year, max_year = data.split('/')
      min_year = int(min_year)
      max_year = int(max_year)
      genres = genres_piped.split('|')
      print(f"Tool Run with inputs: Genres: {genres}  Min Year: {min_year}  Max Year: {max_year}")

      ## Step 1: Load CSV
      important_columns = ['title', 'movie_genres', 'year', 'rating', 'overview']
      df = pd.read_csv('../data/movie_ratings.csv')
      df = df.dropna()
      df = df[important_columns]

      ## Step 2: Filter based on criteria
      #### Filter by selected genres
      genres_filter = df['movie_genres'].apply(lambda x: any(item for item in genres if item in x))
      df = df[genres_filter]
      #### Filter by year
      year_filter = (df['year'] >= min_year) & (df['year'] <= max_year)
      df = df[year_filter]
      ### Filter by rating
      min_rating =3
      df = df[df['rating'] >= min_rating]


      ##Step 3: Sort DF by number of matched genres
      df['matched_genres'] = df['movie_genres'].apply(lambda x: len([item for item in genres if item in x]))
      df.sort_values(by='matched_genres', ascending=False, inplace=True)
      df = df.head(100)

      ## Step 4: Create data for loading in the model
      text_to_llm = ''
      for index, row in df.iterrows():
        text_to_llm += f"--- Movie Title {row['title']} --- "
        text_to_llm += f"--- Movie Plot {row['overview']} --- "
        text_to_llm += f"--- Movie Genres {row['movie_genres']} ---"
        text_to_llm += f"--- Movie Release Year {row['year']} ---"
        text_to_llm += f"--- Movie Rating {row['rating']} ---"
        text_to_llm += '\n'
      
      return text_to_llm
    except Exception as e:
      print(e)
      return "Error with the input format for the tool."
    
movie_tool = MovieSelectionTool.movie_selector

class Chatbot:
    def __init__(self, model='gpt-4o', temperature=0.3, memory=None):
        self.llm_rec = ChatOpenAI(model=model, temperature=temperature)
        self.system_prompt = ''' You are a friendly assistant who will guide customers to select movies of their choice from a database I have.
        You will follow a multi-stage approach to finding the best movies for a customer

        Introduction: Introduce yourself as a movie recommendation bot who will help customers find the best movies from a wide selection of classical movies from 1980 to 2010.

        Stage 1: Understand the customer's interests
        Ask only one question at a time. Always end your responses with a question
        1. Ask 2-3 questions to understand the customer's interests and what kind of movies they like
        2. Infer the genre of the movie based on their preferences or explicitely ask it. I have movies from the following genres:
        'Science Fiction', 'Fantasy', 'War', 'Adventure', 'Romance', 'Documentary', 'Family', 'Animation', 'Comedy', 'TV Movie', 'Thriller', 'Drama', 'Crime', 'Mystery', 'Music', 'Horror', 'Action', 'History'
        3. I have movies from 1985-2005. Understand which decade, range of years they are interested in

        Stage 2: Use the tool you have to get a database of movies you have
        The input to the tool is the genres and min and max years
        The tool takes the following inputs:
        Genres as a list. Genres should be from the above selections
        Min and max years as int
        All genres should be pipe sepearated and years should be / separated. 
        Example if the user is look for comedy and drama from 1990 to 2000, then input should be `Comedy|Drama/1990/2000`
        Example if the user is looking for Romance, Family and Animation from 1995 to 2005 then input should be: Romance|Family|Animation/1995/2005
        Example if the user is looking for Comedy and Drama from 1990 to 2000 then input should be: Comedy|Drama/1990/2000

        Stage 3: The tool will give you all the movies that match the criteria you shared and are well rated
        From this set, you now need to present top 3 choices to the customer and explain your rationale
        Try and match the movies to the type they like

        Stage 4: Adjust your choices if the user doesn't like your recommendation
        Ask them about the kind of plot they would like to see and then look for movies with those plots
        Present the top 3 choices again

        General rules:
        1. Ask one question at a time. Wait for the user's response before asking the next question
        2. End your responses with questions so you can continue the conversation
        '''
        self.memory = memory if memory else ChatMessageHistory(session_id="test-session")
        self.tools = [movie_tool]
    
    def run(self, input):
        ## Load Current Profile

        prompt_rec = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
            content=self.system_prompt
        ),
          MessagesPlaceholder(variable_name="chat_history"),   
          MessagesPlaceholder(variable_name="agent_scratchpad"),

         ("user", "{input}"),            
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
        result = agent_with_chat_history.invoke({'input': input,}, config={"configurable": {"session_id": "1234"}})
        # print("Memory: ", self.memory)
        # print("========")
        return result['output']