from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


class ToolCall(BaseModel):
    name: str
    args: Dict[str, Any]
    id: str
    type: str


class PromptFeedback(BaseModel):
    block_reason: Optional[int]
    safety_ratings: Optional[List[Any]]


class ResponseMetadata(BaseModel):
    prompt_feedback: Optional[PromptFeedback]
    finish_reason: Optional[str]
    model_name: Optional[str]
    safety_ratings: Optional[List[Any]]
    grounding_metadata: Optional[Dict[str, Any]]
    model_provider: Optional[str]


class UsageMetadata(BaseModel):
    input_tokens: Optional[int]
    output_tokens: Optional[int]
    total_tokens: Optional[int]
    input_token_details: Optional[Dict[str, Any]]
    output_token_details: Optional[Dict[str, Any]]


class MessageBase(BaseModel):
    content: str
    id: str


class HumanMessage(MessageBase):
    additional_kwargs: Optional[Dict[str, Any]] = {}
    response_metadata: Optional[Dict[str, Any]] = {}


class AIMessage(MessageBase):
    additional_kwargs: Optional[Dict[str, Any]] = {}
    response_metadata: Optional[ResponseMetadata] = None
    tool_calls: Optional[List[ToolCall]] = None
    usage_metadata: Optional[UsageMetadata] = None


class ToolMessage(MessageBase):
    name: str
    tool_call_id: str


class ResponseSchema(BaseModel):
    messages: List[Union[HumanMessage, AIMessage, ToolMessage]]
