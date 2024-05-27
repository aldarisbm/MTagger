from dataclasses import dataclass, field
from lib2to3.pgen2.grammar import Grammar
from typing import Any, Dict

from llama_cpp import Llama


@dataclass
class MetadataProducerLlm:
    model_path: str = field(init=True)
    __default_kwargs: Dict[Any, Any] = field(init=False)

    # TODO need to add defaults for LLM from pretrained
    __default_llm_repo_id: str = field(init=False)
    __default_llm_filename: str = field(init=False)
    __llm: Llama = field(init=False)
    __system_prompt: str = field(init=False)
    __grammar: Grammar = field(init=False)

    def __post_init__(self):
        self.__default_kwargs = dict(
            n_gpu_layers=-1,
            use_mlock=True,
            n_ctx=128
        )

        if self.model_path:
            llm = Llama(
                model_path=self.model_path,
                **self.__default_kwargs,
            )
        if not self.model_path:
            llm = Llama.from_pretrained(
                repo_id=self.__default_llm_repo_id,
                filename=self.__default_llm_filename,
                verbose=False,
                **self.__default_kwargs,
            )

    def inference(self, current_metadata: str) -> str:
        messages = [
            {
                "role": "system",
                "content": self.__system_prompt
            }
        ]
        resp = self.__llm.create_completion(
            grammar=self.__grammar,

        )
        return resp.choices[0].text
