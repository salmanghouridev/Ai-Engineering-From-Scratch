## Overview

Every AI API works the same way: send a request, get a response. The details change, the pattern doesn't.

## Languages

Python, TypeScript

## Learning Objectives

- Store API keys securely using environment variables and .env files
- Make an LLM API call using both the Anthropic Python SDK and raw HTTP
- Compare SDK-based and raw HTTP request/response formats for debugging
- Identify and handle common API errors including authentication and rate limits

## The Problem

Starting from Phase 11, you'll call LLM APIs (Anthropic, OpenAI, Google). In Phase 13-16 you'll build agents that use these APIs in loops. You need to know how API keys work, how to store them safely, and how to make your first API call.

## Exercises
- Get an Anthropic API key and make your first API call
- Try the raw HTTP version and compare the response format to the SDK version
- Intentionally use a wrong API key and read the error message

