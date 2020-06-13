fullstack-coding-challenge
Thank you for your interest in a fullstack position at ELSA. This README specifies the challenge that we're proposing you to show off your skills.
Please fork this repository and work in your own fork, then do a pull request when you are finished. We will evaluate your work on the pull request. ´
We will be looking for code style, functionality, organization and structure.
The challenge is designed to allow us to evaluate your programming skills, but this is not the only thing we are looking for an ELSA team member. Do not worry if you are pressed with time and can not finish all parts of the challenge, likewise, feel free to extend its functionality beyond what is proposed if you want.
We appreciate that after you check the description below you let us know when you expect to be able to send us a result, so that we can already schedule a technical interview where we look at the code together and resolve any questions we might have on it.

Challenge: language-usage statistics for websites
We would like to compute the histogram (count of number of occurrences of each unique element in a list) of all the words appearing in any given website the user provides. We are only interested in the visualized/rendered text, not the metadata or html tags.
One possible user interface is a text entry box that allows the user to provide a website URL. This is then parsed and results displayed back to the user.
It is up to you how nice or visual you make it. The MVP (Minimum viable product) is an ordered list of the top 100 words ordered from most to least appearing.
You should develop a python backend server that serves a Vue.JS application to the enduser and communicates to the backend via a REST-API.
You should consider what parts of the application shall be implemented on the frontend and what parts should be computed in the backend. IF you are not proficient with Vue.JS feel free to do it in another frontend language.

Plus features
A big plus would be to provide a way (Ansible, docker, etc.) to easily deploy the code.
Another plus would be to provide the backend with a database where previous searches are stored.
Thinking of something else that would be very cool? do it!

Technology Requirements

Frontend
- Stack: Django, Flask, Vue, Angular, React, or other framework.
- UI: Ordered list (minimum) or table/ beautiful chart
- Advantages: Any idea on showing a good dashboard with many useful visualisation

Backend
- Stack: Python (Django, Flask, …), Lambda
- Outcome: API work well with good documentation 
- Advantages: Cache or DB, ….

Repository
- Well arranged
- Build & Deploy
- Docker, Docker-Compose, Makefile

Documentation
- At least how to run
- How to work on …