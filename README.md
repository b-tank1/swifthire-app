## Business Problem
Given the massive number of job openings, it is a big hassle for job seekers to sift through them effectively to find the desired opening. Goal of the project is to build a recommender system which automatically suggests the most suitable job openings for a candidate based on their resume.

## Metrics
Click-Through Rate -> % of recommendations clicked by the job seeker, this will be a reflection of users' recognition for the recommendation </br>
Application Rate -> % of recommendations to which the job seekers submitted an application </br>
Cost -> cost of maintaining the infrastructure </br>

## Data
Resume -> uploaded by the user </br>
Job listings -> scraped from web using API connection to an existing Job Board (Indeed, LinkedIn, Glassdoor, etc.) </br>

## Solution

Below is an an architecture diagram. The user adds preferences and upload their resume. </br>
Resume PDFs are stored in S3, which triggers a lambda function to parse the resume and save in OpenSearch.</br>
Resumes are then matched to job listings which are the Apify web-scraping results from an API call to a job site like Indeed. </br> 
The matched listings are returned and shown in the front-end UI in a ranked order. </br>
The user can then click on the job listing to view more details. </br>

![Solution Architecture](inference-architecture-diagram.jpg)
