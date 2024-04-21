from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    yt_api_key: str
    spotipy_client_id: str
    spotipy_client_secret: str
    spotipy_redirect_uri: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
