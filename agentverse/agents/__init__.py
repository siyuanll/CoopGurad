# from .agent import Agent
from agentverse.registry import Registry

agent_registry = Registry(name="AgentRegistry")

from .base import BaseAgent
from .conversation_agent import ConversationAgent

from .honeytrap_agent import HoneyTrapAgent
from .honeytrap_multi_agent import HoneyTrapAgent
from .honeytrap_multi_agent_con import HoneyTrapAgent