# Overview of Election Audit

In this project, the election data from a congressional district in Colorado state has been audited to retrieve results as described in the following paragraphs.

## Election Audit Results

The elections results was stored in a dataset *election_results.csv*. A Python script *PyPoll_Challenge.py* has been written to retrieve following information when the script is run: 

  - Total number of votes cast
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
  - A complete list of candidates who received votes
  - Total number of votes each candidate received
  - Percentage of votes each candidate won
  - The winner of the election based on popular vote

The *PyPoll_Challenge.py* has been run on VSCode text editor. Initially, the dataset was imported to analye in Python. Detailed steps in Python scripts were followed to retrieve required output information from the dataset. The snapshot of the *PyPoll_Challenge.py* codes is as shown below.

![PyPoll_Challene.py](/Resources/PyPoll_Challenge_ScriptSnapshot.png)

The intended output results of this *.py* script has been written on the *election_results.txt"* text file. 

![election_results.txt](/Resources/election_results_textFilesSnapshot.png)

The .txt file was uploaded to my github repository *https://github.com/moonem/Election_Analysis* using *git bash* terminal applying a sequence of commands such as,

  - git status  // To know the status of the current directory
  - git add .   // To add (*stage*) the modified files to upload to github
  - git commit -m "..message..."  // Preparing files to upload (*push*)
  - git push    // To upload the required files to my github repository

## Election Audit Summary

This audit retrieved election results for 3 counties in Colorado state. The Election commission may use this *.py* script as a baseline code structure and modify the code as required for retrieving any election results in any counties/State(s) in the Country. 

For example, there might be more than 3 columns of information in case of National presidential election such as vote for the president nominee. In such cases, we've to specify correctly in index (e.g. *row[i]* shown in following figure) to retrieve requird data from specific column while the algorithm iterates through each row of the dataset.

![election_results.txt](/Resources/columnSectionSnapshot.png)

Another use case may appear where some new information would be required in the election results, for example, "Who won the most popular vote as a presidential nominee?" In such cases we will need to introduce additional conditional loops (i.e. *for*, *if*) under the main code script using proper indentation. The following figure shows how the *County* vote information was collected, in addition to the candidate information, from the dataset.

![election_results.txt](/Resources/retrieve_new_items_Snapshot.png)
