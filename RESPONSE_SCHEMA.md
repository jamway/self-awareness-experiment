# Response Schema Documentation

This document describes the data model for the response received from the call. The schema is implemented in `src/schema.py` using Pydantic for type validation and clarity.

## Top-level Structure
- `messages`: List of message objects. Each message can be a `HumanMessage`, `AIMessage`, or `ToolMessage`.

## Message Types

### HumanMessage
- `content` (str): The message content from the human.
- `id` (str): Unique identifier for the message.
- `additional_kwargs` (dict, optional): Additional keyword arguments.
- `response_metadata` (dict, optional): Metadata about the response.

### AIMessage
- `content` (str): The message content from the AI.
- `id` (str): Unique identifier for the message.
- `additional_kwargs` (dict, optional): Additional keyword arguments, e.g., function calls.
- `response_metadata` (ResponseMetadata, optional): Metadata about the response, including model info and safety ratings.
- `tool_calls` (list of ToolCall, optional): List of tool calls made by the AI.
- `usage_metadata` (UsageMetadata, optional): Token usage and related metadata.

### ToolMessage
- `content` (str): The message content from the tool.
- `id` (str): Unique identifier for the message.
- `name` (str): Name of the tool used.
- `tool_call_id` (str): Identifier for the tool call.

## Supporting Models
- `ToolCall`: Represents a tool call with name, args, id, and type.
- `ResponseMetadata`: Contains prompt feedback, finish reason, model name, safety ratings, and provider info.
- `UsageMetadata`: Contains token usage details.

---

Refer to `model/schema.py` for the full implementation.
