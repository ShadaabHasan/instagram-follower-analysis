# Instagram Follower Analyzer & EDA

A Python project to analyze instagram data download. 

## About the project
This project provides two tools:

insta.py: A simple utility to find out who doesn't follow back and save the list to a .txt file.

EDA.ipynb: An Exploratory Data Analysis (EDA) script that uses Pandas and Matplotlib to analyze the timestamps to find the earliest followers, and plot the history of follower/following relationships.

This project does not violate Instagram's Terms of Service. It simply parses the JSON files that Instagram provides.

## Features
Data Analysis: Uses Pandas and Matplotlib to perform Exploratory Data Analysis on relationship history.

Generates 1 Output:
A .txt file of all accounts that don't follow back.

## How to Use

### Part 1: Run the Simple Analyzer

Download Instagram Data:

Go to Settings -> Accounts Center -> Your information and permissions.

Download your information -> Download or transfer information.

Select your account, then Some of your information.

Select only Followers and following.

Set format to JSON and click Create files.

Set Up the Project:

Unzip Instagram data download.

In this project's main folder, create a folder named insta.

Move the connections folder (which is inside the unzipped folder) into the insta folder. The path should look like: ...\\instagram_project\\insta\\connections\\...

Run the Script:

python insta.py


This will create a file in analysis_data/not_following_back_YYYY-MM-DD.txt.

### Part 2: Run the Exploratory Data Analysis (EDA)

Install Required Libraries:

pip install pandas matplotlib


Run the EDA Script:

python EDA.py


## A Note on "Ghost" or Deactivated Accounts

You will likely find that the "not following back" list is very long. This is not a bug in the script, but an issue with Instagram's data.

The Problem: Instagram's following.json file includes accounts you followed years ago that were later deleted or deactivated. Instagram never removes these "ghost" accounts from your internal "following" list.

The Result: The script correctly identifies these "ghost" accounts as "not following you back" (since a deleted account cannot follow you).

The Solution: The best way to use this tool is as a "To-Do List Generator" to clean up your account. Use the generated .txt file to manually unfollow these inactive accounts from your Instagram app.