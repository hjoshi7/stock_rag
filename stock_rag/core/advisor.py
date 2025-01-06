from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from config import Config

class StockAdvisor:
    def __init__(self, vector_store):
        self.llm = ChatOpenAI(
            model_name=Config.MODEL_NAME,
            temperature=0.7,
            api_key=Config.OPENAI_API_KEY
        )
        
        system_prompt = """
        Act as a financial advisor. Using the provided context, answer the following question:
        Context: {context}
        Question: {query}
        
        Provide a detailed analysis with:
        1. Market context
        2. Specific recommendations
        3. Risk considerations
        4. Timeline suggestions
        """
        
        PROMPT = ChatPromptTemplate.from_template(system_prompt)
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={'k': 3}),
            return_source_documents=True,
            prompt=PROMPT
        )

    def get_recommendation(self, query):
        return self.qa_chain({"query": query})
