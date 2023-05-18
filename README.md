# botter1
A middleware to AI APIs like OpenAI::ChatGPT4
This is an experiment to learn to connect software applications with AI models via APIs provided by the latter.

![image](https://github.com/euroblaze/botter1/assets/7826363/9de72d0a-8762-426c-9d4d-6308d671f78a)

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

1. Break up the quick & dirty code to above architecture.

# Scaling

Since the AI API landscape is fast evolving, and we hope to test as many APIs as possible that are relevant to our business needs, 
we should be aiming to layout code-structures that allow maximum flexibility to experiment/test new possibilities fast.
