# Data Bot

This chatbot uses an NLP Model to create graphical plots based on user inputted data file and instructions. These instructions input the columns to be used for the creation of graphical plots. Additionally, this tool also does data quality check of uploaded data file along with sentiment analysis of user-inputted text.

## Description

The end-user will update a data file (xls or xlsx) based on which he/she provide an instruction which will consist of the columns to be used for creation of graphical plots. 
As a result, a downloadable graphical plot is returned back to the user. Including this main function, the following functions are available in this Data Bot:

1.) Creation of downloadable plots as required by the end-user. 
2.) Creation of a downloadable data quality check report.
3.) Creation of a sentiment analysis report of the textual input by end-user.

## Getting Started 

### Requirements to run and test the project:

To run this project, you will need Python3+, pip and Git installed on the system. 

The reference links are provided below.

> **Python:**
  https://www.python.org/downloads/
  
> **pip:**
  https://pypi.org/project/pip/

> **Git:**
  https://git-scm.com/downloads
	
The necessary libraries and packages are specified in the **requirements.txt** file and will be validated in the below steps

### Process for acquiring the results: 

  * **Step 1:**
  Create a local directory in your machine where you want to pull the git project and clone the project by running the below command from cmd 
  (Make sure that you are in the newly created directory first!):
  
  	```git clone https://github.com/AjayTomar3342/DataBot```

  * **Step 2:**
  From cmd, move into the main folder of the cloned project
  
 	 ```cd DataBot```

  * **Step 3:**
  Execute the below commands to meet the pre-requisites to execute the code
  
  ```  	
      Unix/macOS
      python -m pip install -r requirements.txt

      Windows
      py -m pip install -r requirements.txt
  ```

  
  * **Step 4:**
  Execute the below commands to run the code from cmd
  
  ``` 
      Unix/macOS
      python main.py

      Windows
      %run main.py
  ```


### Alternative Process for acquiring the results(Backup):

For quick running of program, PyCharm use is suggested as it has good controls for removing manual steps to pull a repository and get it running.

Steps are:

  * **Step 1:**
  Make sure one is signed in on Github in Pycharm
  
  * **Step 2:**
  Open a new project
  
  * **Step 3:**
  Go to VCS Option on the Top Horizontal Options Bar
  
  * **Step 4:**
  Select Enable Version Control Integration Control inside VCS if not done already
  
  * **Step 5:**
  After checking the previous option on, select Checkout from Version Control and select Git
  
  * **Step 6:**
  In the new pop up window, include the link of the github repository you are trying to pull.
  Subsequently in the same pop up window, select an appropriate directory where the  project will be pulled.
  
  * **Step 7:**
  Select clone option to start the pulling process.
  
  * **Step 8:**
  Select option to start the pulled project in New Window or This window as per your personal preference.
  
  * **Step 9:**
  After this the project will be up and running and requirements.txt file will automatically install required libraries. Run the file main.py from Root Folder to get the results

This is a quick process to start the testing of GitHub project taken from the Official Jet Brains Website. We have tried this with several PC’s and are confident that this will not give any errors.

> **Link to Above Process Video:**
  https://www.youtube.com/watch?v=ukbvdF5wqPQ&feature=emb_title

  **NOTE:** 
* Since, the libraries used in the project are updated by the original developers regularly, some function/functions may not run as expected. This project will be regularly updated as per the updated libraries requirement, but if project does not run at any give time when you pull the project, it may be due to the library change, rather than a coding issue. This repository is last updated as per latest libraries on 31/12/2024.

* a


### Executing program (Incomplete)

* How to run the program
* Step-by-step bullets     
* In order to submit instructions which will propel the ChatBot to create graphical plots, such an instruction is set as default. 
```
Please create a heatmap for Column Age, Column Id, Column 0 and Column Unnamed: 0
```
Such an instruction should contain which specific kind of graphical plot is required by the user and which columns should 
be used in the graphical plot. For simplicity, replacement of the graphical plot and the columns required should be done in
the above-mentioned dummy instruction. 

## Features and Outputs
This ChatBot consists of the following features:

<ol type="a">
  <li> Graphical Plots creation based on User Inputs and data file.</li>
  <li> Sentiment Analysis of User Inputted text.</li>
  <li> Data Quality checking of User Inputted data file.</li>
</ol>

The outputs of the corresponding features are as follows:

<ol type="a">
  <li> User gets a downloadable format of the graphical plot he/she requested.</li>
  <li> A downloadable word document giving a detailed sentiment analysis report.</li>
  <li> A downloadable word document giving a detailed data quality check report.</li>
</ol>

Note: The resulting documents are in editable docx format so that the 
end-user can edit the files if needed be. 

## Help

### Usage Tips (Incomplete)

Any advice for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

1.) Ajay Tomar (https://www.linkedin.com/in/ajaytomar66/)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
