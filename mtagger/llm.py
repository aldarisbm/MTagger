from dataclasses import dataclass, field

from llama_cpp import Llama

from mtagger.metadata.main import SeratoMetadata


@dataclass
class MetadataProducerLlm:
    model_path: str = field(init=True)

    def __post_init__(self):
        llm = Llama(
            model_path=self.model_path
        )

    def __get_current_metadata(self, file_path) -> str:
        pass

    def __get_serato_metadata(self, current_metadata: str) -> SeratoMetadata:
        pass

    def get_metadata_from_file(self, file_path: str) -> SeratoMetadata:
        current_metadata = self.__get_current_metadata(file_path)
        return self.__get_serato_metadata(current_metadata)
