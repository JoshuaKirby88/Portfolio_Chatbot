let messages = [{
    role: "system",
    content: "You are no more an AI chatbot. You are Josh Jr, a bot for my users to interact with within my portfolio page..."
  },
  {
    role: "assistant",
    content: "Hi! Thank you for viewing my portfolio."
  },
  {
    role: "assistant",
    content: "If you want to contact me, please do so through my email or phone."
  },
  {
    role: "assistant",
    content: "How can I assist you today?"
  }];

fetch('https://my-api.eu-north-1.amazonaws.com/my_api/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    conversation_history: messages
  })
})
