from typing import Any, Dict, Iterator, List, Mapping, Optional
import os
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk
from together import Together


class TogetherLLM(LLM):
    model_name: str = "Together open source LLM"
    max_tokens: int = 1024
    temperature: float = 0.3

    """ Runs an open source LLM model from together """

    def __init__(self, model: str = 'mistralai/Mistral-7B-Instruct-v0.3', max_tokens: int = None, temperature: float = None, **kwargs: Any):
        """
        Initializes the TogetherLLM with specified parameters.

        Args:
            model: The name of the model to use.
            max_tokens: The maximum number of tokens to generate (optional).
            temperature: The temperature to use for sampling (optional).
            **kwargs: Additional keyword arguments to pass to the parent LLM class.
        """
        kwargs['model_name'] = model  
        kwargs['max_tokens'] =  max_tokens if max_tokens is not None else self.__class__.max_tokens 
        kwargs['temperature'] = temperature if temperature is not None else self.__class__.temperature 
        super().__init__(**kwargs)  


    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        together_client = Together(api_key=os.environ["TOGETHER_API_KEY"])
        response = together_client.chat.completions.create(
            model=self.model_name,  # Use the model specified in __init__
            messages=[{"role": "user", "content": f"{prompt}"}],
            temperature=self.temperature,  # Use the temperature specified in __init__
            max_tokens=self.max_tokens,    # Use the max_tokens specified in __init__
        )
        return response.choices[0].message.content


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
            "model_name": "Together open source LLM",
        }

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "Together Open source LLM"