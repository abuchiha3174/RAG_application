from langchain_core.prompts import ChatPromptTemplate
from src.exception import CustomException

class PromptBuilder:
    def __init__(self, system_template: str, user_template: str):
        self.template = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("user", user_template)
        ])

    def get_prompt(self, **kwargs):
        return self.template.format_messages(**kwargs)

    def get_template(self):
        return self.template
    
    @staticmethod
    def build_context_section(context_docs: list[str] = None) -> str:
        if context_docs and len(context_docs) > 0:
            joined = "\n".join(context_docs)
            return f"CONTEXT:\n{joined}\n--- End of Context ---"
        else:
            return "No context was provided."
