# botter1
A middleware to AI APIs like OpenAI::ChatGPT4
This is an experiment to learn to connect software applications with AI models via APIs provided by the latter.

![image](https://github.com/euroblaze/botter1/assets/7826363/2f6c8af4-74ce-4f9e-b54f-f164ed93e5b8)

# To do

## Architecture

1. Define the REST API calls of botter1.
    - receive requests
    - return responses
 
2. Define the logic-layer of botter1 as an MVC.
    - support calls to multiple AI APIs
        - Start with OpenAI
        - Google APIs will probably be next
    - Able to process files, ex. PDF, MP3, MP4 etc
    - Connect with other services, like Dropbox

3. Has a simple web-UI to test prompts, conversations etc. 
    - This Botter-UI better use the Botter1-REST-API.

## Simple Code

1. Break up the [quick & dirty script]([url](https://github.com/euroblaze/botter1/blob/main/quickanddirtyscript.py)) to above architecture.
2. Put up a simple webform that allows to provide inputs to botter1 and view, evaluate and resend inputs/prompts.

# Scaling

The AI API landscape is fast evolving.
We hope to test as many APIs as possible that are relevant to our business needs.
Hence we should be aiming to layout code-structures that allow maximum flexibility to experiment/test new possibilities fast.
