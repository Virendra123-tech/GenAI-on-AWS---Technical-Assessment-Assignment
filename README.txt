This project demonstrates a document summarization pipeline using GenAI concepts
and AWS serverless architecture. The solution focuses on document processing,
token estimation, and chunking to handle large inputs within LLM context limits.

The pipeline is designed to use Amazon S3 for document storage, AWS Lambda for
processing and chunking, and Amazon Bedrock for GenAI-based summarization. Each
document chunk is summarized individually and combined into a final summary,
helping reduce hallucination risk and optimize inference cost.
