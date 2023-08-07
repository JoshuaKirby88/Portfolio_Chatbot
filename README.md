# Portfolio_Chatbot
A GPT-3.5 powered chatbot for my portfolio website that is able to answer questions about me, and handle visitor interactions.

Flow:
1. The conversation history stored as a json object is passed to an API that I created using AWS.
2. The json object is then passed on to the OpenAI API.

Security:
- My AWS API only allows access from my portfolio website, by setting the origin for CORS to my website address.
- The OpenAI API key is secured as an environment variable, within my AWS API.

Files:
- "my_api_access.js" is a snippet of code for my chatbot hosted on my portfolio website that accesses my API on AWS.
- "openai_api_access.py" is my AWS Lambda function that is connected to my AWS API, which securely calls the OpenAI API.
