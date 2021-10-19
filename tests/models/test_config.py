from itme.models.config import Config
import os


def test_init():
    example_toml = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "example.toml"
    )
    config = Config(example_toml)
    assert config.get("title") is not None
