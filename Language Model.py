import transformers
nlp = transformers.pipeline("conversational", 
                            model="microsoft/DialoGPT-medium")
#Time to try it out
input_text = "hello!"
nlp(transformers.Conversation(input_text), pad_token_id=50256)

nlp(transformers.Conversation(input_text), pad_token_id=50256)

chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
res = str(chat)
res = res[res.find("bot >> ")+6:].strip()

