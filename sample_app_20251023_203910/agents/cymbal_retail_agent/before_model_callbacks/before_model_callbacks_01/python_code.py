def get_all_text(contents: List[Content]) -> str:
  """Collate all text from the most recent set of contents."""
  all_text = []
  for content in contents:
    for part in content.parts:
      all_text.append(part.text)

  return all_text

def get_last_utterance(request: LlmRequest) -> str:
  """Extract the last user utterance from the list of texts."""
  all_text = get_all_text(request.contents)

  return all_text[-1]
  
def respond(text: str) -> LlmResponse:
  """Help method to format the LlmResponse class."""
  return LlmResponse(content=Content(parts=[Part(text=text)], role="model"))
  
def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
  user_query = get_last_utterance(llm_request)
  print(f"USER QUERY IS: {user_query}")

  if user_query:
    if "system instructions" in user_query.lower():
      print("--- MANUAL GUARDRAIL: OVERRIDE LLM RESPONSE ---")
      return respond("I'm sorry but I'm afraid I can't comply with that request.")