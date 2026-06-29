# Evaluation

| Query | Expected | Result |
|------|---------|--------|
| Leave policy | Correct | Correct |
| Refund policy | Correct | Correct |
| Unknown question | No information | Correct |

## Hallucination Prevention

The LLM is instructed to answer only from the retrieved context.

## Retrieval

Top 3 chunks are retrieved from FAISS.