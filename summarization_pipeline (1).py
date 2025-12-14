"""
Document Summarization Pipeline (GenAI + AWS)

This script demonstrates the document processing and summarization
component of a GenAI-powered pipeline.

Features:
- Token estimation
- Chunking based on LLM context limits
- Mock GenAI summarization
- Final summary generation

In a production system, this logic would run inside AWS Lambda
and call an LLM via Amazon Bedrock.
"""

import os
import math


# Step 1: Token Estimation
def estimate_tokens(text: str):
    """
    Rough token estimation:
    1 token ≈ 4 characters
    """
    return math.ceil(len(text) / 4)


# Step 2: Document Processing & Chunking
def process_document(file_path: str, max_tokens: int = 5000):
    """
    Reads a text file, chunks it if it exceeds token limit,
    and returns structured metadata.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("Document not found")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        return {
            "error": "Empty document",
            "chunk_count": 0,
            "character_count": 0,
            "estimated_tokens": 0,
            "chunks": []
        }

    total_chars = len(text)
    total_tokens = estimate_tokens(text)

    chunks = []
    if total_tokens <= max_tokens:
        chunks.append(text)
    else:
        chunk_size_chars = max_tokens * 4
        for i in range(0, total_chars, chunk_size_chars):
            chunks.append(text[i:i + chunk_size_chars])

    return {
        "chunk_count": len(chunks),
        "character_count": total_chars,
        "estimated_tokens": total_tokens,
        "chunks": chunks
    }


# Step 3: Mock GenAI Summarization
def summarize_chunk(chunk_text: str) -> str:
    """
    Mock summarization function.
    In production, this would call Amazon Bedrock / LLM API.
    """
    return f"Summary of chunk (length={len(chunk_text)})"


def summarize_document(processed_doc: dict) -> str:
    summaries = []
    for chunk in processed_doc["chunks"]:
        summaries.append(summarize_chunk(chunk))

    return " ".join(summaries)


# Step 4: Final Output
if __name__ == "__main__":
    result = process_document("sample.txt")

    print("Chunks:", result["chunk_count"])
    print("Estimated Tokens:", result["estimated_tokens"])

    final_summary = summarize_document(result)
    print("Final Summary:", final_summary)
