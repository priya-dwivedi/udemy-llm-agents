
from dotenv import load_dotenv
from typing import Any, Dict, Iterator, List, Mapping, Optional
import os
load_dotenv()

import google.generativeai as genai
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk

# Set up the model
generation_config = {
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
#   "response_mime_type": "application/json",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


class GeminiLLM(LLM):
    model_name: str = "Gemini LLM"
    temperature: float = 0.3

    """ Runs the Gemini 1.5 Pro model from Google """

    def __init__(self, model: str = 'gemini-1.5-flash-latest', temperature: float = None,  response_mime_type: str= None, **kwargs: Any):
        """
        Initializes the TogetherLLM with specified parameters.

        Args:
            model: The name of the model to use.
            temperature: The temperature to use for sampling (optional).
            **kwargs: Additional keyword arguments to pass to the parent LLM class.
        """
        super().__init__(**kwargs)
        self.model_name = model  # Define model as an attribute
        generation_config['temperature'] = temperature if temperature is not None else self.__class__.temperature 
        if response_mime_type:
            generation_config['response_mime_type'] = response_mime_type

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        gemini_model = genai.GenerativeModel(model_name=self.model_name, generation_config=generation_config) 
        response = gemini_model.generate_content(prompt)
        response_list = response.text
        return response_list


    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        """Stream the LLM on the given prompt.

        This method should be overridden by subclasses that support streaming.

        If not implemented, the default behavior of calls to stream will be to
        fallback to the non-streaming version of the model and return
        the output as a single chunk.

        Args:
            prompt: The prompt to generate from.
            stop: Stop words to use when generating. Model output is cut off at the
                first occurrence of any of these substrings.
            run_manager: Callback manager for the run.
            **kwargs: Arbitrary additional keyword arguments. These are usually passed
                to the model provider API call.

        Returns:
            An iterator of GenerationChunks.
        """
        return None

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Return a dictionary of identifying parameters."""
        return {
            # The model name allows users to specify custom token counting
            # rules in LLM monitoring applications (e.g., in LangSmith users
            # can provide per token pricing for their model and monitor
            # costs for the given LLM.)
            "model_name": "Gemini LLM",
        }

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "Gemini LLM"