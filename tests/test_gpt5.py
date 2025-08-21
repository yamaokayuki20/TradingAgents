import os
import sys
import questionary

# Ensure repository root on path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import cli.utils as utils
import tradingagents.default_config as default_config

class DummySelect:
    def __init__(self, choices):
        self.choices = choices
    def ask(self):
        # ensure GPT-5 is available as an option
        assert any(choice.value == "gpt-5" for choice in self.choices)
        return "gpt-5"

def test_select_shallow_thinking_agent_includes_gpt5(monkeypatch):
    def fake_select(*args, **kwargs):
        return DummySelect(kwargs["choices"])
    monkeypatch.setattr(questionary, "select", fake_select)
    result = utils.select_shallow_thinking_agent("openai")
    assert result == "gpt-5"

def test_select_deep_thinking_agent_includes_gpt5(monkeypatch):
    def fake_select(*args, **kwargs):
        return DummySelect(kwargs["choices"])
    monkeypatch.setattr(questionary, "select", fake_select)
    result = utils.select_deep_thinking_agent("openai")
    assert result == "gpt-5"

def test_default_config_uses_gpt5():
    assert default_config.DEFAULT_CONFIG["deep_think_llm"] == "gpt-5"
