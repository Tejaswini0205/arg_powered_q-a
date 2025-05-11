# Sample agent logic (simplified)
def determine_tool(query):
    if 'calculate' in query or 'define' in query:
        return 'external_tool'  # Placeholder for actual logic
    return 'rag_pipeline'  # Placeholder for actual RAG pipeline logic

def handle_query(query):
    tool = determine_tool(query)
    if tool == 'rag_pipeline':
        # Placeholder: Integrate RAG pipeline
        return 'Answer from LLM after retrieving relevant context.'
    elif tool == 'external_tool':
        # Placeholder: Call an external tool like a calculator or dictionary API
        return 'Answer from external tool (e.g., dictionary, calculator).'
