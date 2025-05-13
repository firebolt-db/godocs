---
layout: default
title: MCP Server
description: Use Firebolt MCP Server to enable AI-powered workflows with LLMs.
nav_order: 16
parent: Integrate with Firebolt
---

# Firebolt MCP Server

Firebolt MCP Server is a lightweight service that enables **large language models (LLMs)** like Claude, GitHub Copilot Chat, and Cursor to connect to Firebolt in a secure, context-aware way. It acts as a bridge between your data warehouse and AI assistants, allowing them to:

- Understand Firebolt-specific SQL
- Query your databases with context-aware prompts
- Access technical documentation, metadata, and live data

It’s designed for developers, analysts, and teams who want to integrate Firebolt into AI-driven workflows or copilots with minimal setup.

## When to Use MCP Server

Use Firebolt MCP Server if you want to:

- Enable LLMs to write and execute SQL against your Firebolt environment
- Automate documentation lookups and metadata extraction
- Create advanced AI agents that can explore, troubleshoot, and analyze Firebolt data

Typical use cases include:

- Querying Firebolt using natural language
- Custom copilots in VSCode or Cursor with deep Firebolt context
- AI workflows that require real-time access to Firebolt SQL features

## Getting Started

MCP Server is available as both a binary and a Docker container. To run it, you’ll need:

- A [Firebolt service account]({% link Guides/managing-your-organization/service-accounts.md %}) (Client ID and Secret)
- Either Docker or a supported OS for running Go binaries
- An LLM client that supports [Model Context Protocol (MCP)](https://modelcontextprotocol.io)

> 📘 Full setup instructions, environment variables, and integration guides are available on the [Firebolt MCP GitHub repository](https://github.com/firebolt-db/mcp-server).
