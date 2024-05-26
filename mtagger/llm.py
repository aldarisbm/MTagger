from dataclasses import dataclass, field

from llama_cpp import Llama


@dataclass
class MetadataProducerLlm:
    model_path: str = field(init=True)
    __llm: Llama = field(init=False)

    def __post_init__(self):
        llm = Llama(
            model_path=self.model_path,
            n_gpu_layers=-1,
            use_mlock=True,
            n_ctx=128,
        )

    def inference(self, current_metadata: str) -> str:
        self.__llm(current_metadata)
