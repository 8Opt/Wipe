# WIPE 

> Eye wiped, AI hyped. 

## Introduction

**Tired of the tears caused by technical glitches?** We're here to **wipe** them away. Wip delivers real-time updates on the latest AI trends, ensuring you stay ahead of the curve.

![](./asset/wipe_pipe.png)

**Workflow**:

+ The Publisher generates updates on the latest AI trends.
+ The Feature component processes these updates, potentially performing tasks like natural language processing, data analysis, or summarization.
+ The processed updates are sent to the Notification component, which distributes them to interested Consumers.
+ The Consumers can then utilize the trend updates for their specific purposes, such as training AI models, updating product features, or providing personalized recommendations.

## Features

- Update latest information related to AI. 
- Summarize article with Large Language Models.


## Code in Action


1. Clone the repository

```
git clone https://github.com/MinLee0210/Wipe.git
cd Wipe
```

2. Setup environment

Create an `.env` file in the root directory following this format. 

```
TAVILY_API_KEY = ""
GEMINI_API_KEY=""  
GROQ_API_KEY=""
OPENAI_API_KEY="
```

_Note:_ `TAVILY_API_KEY` is a must for the API of search engine. Choice of LLM's API depends on your usage. You can switch between Gemini, Groq, and OpenAI. 


3. Usage

**Build and start Docker Image**
```
docker-compose up --build
```


**Running the server**



## Contact me via

+ **Github:** https://github.com/MinLee0210
+ **Gmail:** minh.leduc.0210@gmail.com
+ **LinkedIn:** www.linkedin.com/in/minhle007


## Note

_User story:_ 

+ As a user, I want to be updated daily with latest AI trends.
+ As a user, I want to capture all information in the news in a matter of second. 