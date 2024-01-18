# github-jira-integration
Using github webhook we will trigger flask api to create Jira issue(ticket).
If tha flask is deployed on EC2 server then using export command we need to set the env variable for API_Token. (Whenever server is restarted we need to again set the env variable -> API_Token.)
