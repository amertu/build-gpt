# BuildSensei (GPT-Powered Build & Code Analysis)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-4B0082?logo=openai)](https://platform.openai.com/)
[![GitHub API](https://img.shields.io/badge/GitHub%20API-v3-black?logo=github)](https://docs.github.com/en/rest)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-800080?logo=uvicorn)](https://www.uvicorn.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions)](https://docs.github.com/en/actions)


## Project Overview
Build-GPT is a domain-specific AI system that analyzes failed build pipelines and helps developers understand and fix the problem faster. It parses logs from tools like Maven and npm, extracts the relevant error messages, retrieves matching code from the repo, and sends the entire context to GPT, which responds with a human-readable explanation and fix suggestion.

The goal is to reduce time spent digging through CI logs and help teams recover from broken builds faster with clear, actionable insight.


## Key Features
- Log parsing for Maven and npm build outputs
- GPT-based error analysis and code-aware explanation
- Code context resolver using GitHub API
- Returns suggestions via API or PR comments
- Modular and extensible for other tools (e.g., Gradle, Jest, etc.)
  

## Architecture
```markdown
                                  ┌─────────────────────────────┐
                                  │        GitHub Actions       │
                                  │   (Backend & Frontend CI/CD)│
                                  └────────────┬────────────────┘
                                               │
                                      Generate build logs
                                               │
                            ┌──────────────────▼──────────────────┐
                            │           Log Collector             │
                            │   (mvn.log / npm.log / test.log)    │
                            └──────────────────┬──────────────────┘
                                               │
                            ┌──────────────────▼──────────────────┐
                            │       Log Parser & Classifier       │
                            │  ┌────────────┐   ┌───────────────┐ │
                            │  │ MavenParser│   │ NpmParser     │ │
                            │  └────────────┘   └───────────────┘ │
                            │      → Error code, file, line       │
                            └──────────────────┬──────────────────┘
                                               │
                            ┌──────────────────▼──────────────────┐
                            │        Code Context Resolver        │
                            │    (GitHub API or local repository) │
                            │      → Code snippet ±10 lines       │
                            └──────────────────┬──────────────────┘
                                               │
                            ┌──────────────────▼─────────────────────┐
                            │             GPT Service                │
                            │   Prompt template depends on parser    │
                            │         (Java vs. JS/TS)               │
                            │ Response: explanation + fix suggestion │
                            └──────────────────┬─────────────────────┘
                                               │
                             ┌─────────────────▼──────────────────┐
                             │        Output Layer / Feedback     │
                             │    PR comments, Slack, Email, UI   │
                             └────────────────────────────────────┘

```
