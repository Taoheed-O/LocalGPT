# import chainlit as cl

# @cl.on_message
# def main(message:str):
#     result = message.title()

#     cl.Message(content= f"sure here is your message: {result}").send()


# @cl.on_chat_start
# def chat():
#     content = "Hi welcome to teslabot what can I do for you?"
#     cl.Message(content=content).send()

import chainlit as cl
from textblob import TextBlob
from gpt4all import GPT4All


gpt = GPT4All(model_name='nous-hermes-13b.ggmlv3.q4_0.bin', model_path='models')


@cl.on_chat_start
async def start():
    # Send the first message without the elements
    content = "Hi, this is TeslaBot how can I help you?"

    await cl.Message(
        content=content,
    ).send()

    # elements = [
    #     cl.Image(path="images/avatar.jpeg", name="image1", display="inline"),
    #     cl.Text(content="Here is a side text document", name="text1", display="side"),
    #     cl.Text(content="Here is a page text document", name="text2", display="page"),
    #]

    # Send the second message with the elements
    # await cl.Message(
    #     content=content,
    #     #elements=elements,
    # ).send()


@cl.on_message
async def message(text:str):
    # logic
    if 'count' in text:
        file = None
        while file == None:
            file = await cl.AskFileMessage(
                content='please upload the file here',
                accept=['text/plain']).send()
            
        text = file[0].content.decode("utf-8")
        count = len(text)

        await cl.Message(content = f'The word count of your text is: {count} ').send()
    else:
        response = gpt.generate(text, temp=0.65)
        await cl.Message(f'{response}')
