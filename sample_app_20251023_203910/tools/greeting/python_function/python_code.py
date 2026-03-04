import json

def greeting() -> dict:
  """A static default greeting that is sent to the user."""
  # Deterministically call another tool from within the greeting tool.
  # The syntax for OpenAPI spec tools is:
  # tools.<tool_name>_<endpoint_name>({tool_args})
  res = tools.crm_service_get_cart_information({})

  FIRST_NAME = context.variables["customer_profile"]["customer_first_name"]

  return {
    "greeting": f"Hi there! Welcome to Cymbal Garden. Is this {FIRST_NAME}?",
    "cart_information": res.json()
    }
