from enum import StrEnum


class ProjectType(StrEnum):
    """Different types of projects."""

    BASIC = "basic"
    API = "api"
    API_AGENTS = "api-agents"
    AGENTS = "agents"
    DEEP_LEARNING = "dl"
    API_DEEP_LEARNING = "api-dl"
    ALL = "all"


__all__ = [
    "ProjectType",
]
