# voltAIc

.. is an AI platform for PowerOn, with generative and predictive capabilities. It prioritises running own model-servers over using APIs of big-tech (OpenAI, Google, Azure, AWS).

voltAIc has generative capabilities such as:

1. Read data from Project and Task models and create a project report (summarisation).
2. Read customer record and produce a complete dossiert and dashboard with key facts and figures.
3. Systemwide search, so user has 1 UI to query the whole ERP.

voltAIc's predictive capabilities are such that..

1. It can understand incoming performance data from solar installation-devices and predict maintenance.
2. It can easily predict stock-requirements for the next weeks and months, and potentially trigger [Purchase Automations](https://github.com/euroblaze/schulsachen/tree/16.0/purchase_automation/models).
3. It can predict future sales.

## Architecture

We operate voltAIc at 3 levels.

1. Servers -- model-servers, vector database servers, RDBMS etc.
2. API libraries, like [ollama-python](https://github.com/ollama/ollama-python) and LangChain.
3. Applications, like Odoo etc., which load the API libraries for delivering business and use cases.

Following software components populate the current voltAIc runtime.

### Servers

1. Ollama
2. Open-WebUI

### API Librarires

1. ollama-python
2. LangChain

### Application Software

1. Odoo


### Serverless

1. Google Sheets
2. NextCloud


---

(OLD STUFF BELOW. CAN BE ARCHIVED).
### Middleware
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
