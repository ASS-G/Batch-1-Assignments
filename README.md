<div align="left">
<h1>
    <img alt="header" src="/src/assets/Header.png" width="900" height="300"></img>
</h1>


Welcome to the  ASS-G - Assignment Repository. The assignments will be posted here implement. Successfully completing an assignment implies proper conceptual understanding.


**:white_check_mark: Send a pull request only after completing an assignment.**

**:white_check_mark: Please submit PRs (Pull Requests) after completion of every assignment.**

**:white_check_mark: [Please follow this PR Template while submitting assignments](https://github.com/ASS-G/Batch-1-Assignments/pull/9)**

**:white_check_mark: Please read through the [FAQ](#faq) before proceeding with the assignment.**

**:white_check_mark: Please follow proper file structure else the PR would be rejected**

**:white_check_mark: Keep fetching the repository from here as we instruct so that you'd receive all assignments in time**


## What Do I Do?
One assignment for every week. Scroll down to take a look at them. All you need to do is fork this repository, complete the given assignment, send a pull request over to us and repeat the process for every assignment. Check out our FAQ for more information.


## Index
  - [**Assignment 1 - Using Git**](#assignment-1---using-git)
  - [**Assignment 2 - Python Basics and Strings**](#assignment-2---python-basics-and-strings)
  - [**FAQ**](#faq)


## Algorithms
### **Assignment 1 - Using Git**
  - **Problem**
    - Write your first python program `hello_world.py` and upload it to our Assignment Repository using Git.
    - :warning: Follow the file structure properly as instructed [here](#how-should-i-complete-these-programs) else the Pull request will be automatically rejected.

  - **Expected Output**
    ```python
      py hello_world.py >
      Hello World!
    ```

  - **Resources**
    - [Git Training Kit](https://github.com/ASS-G/Git-Training-Kit)
    - [Getting started with Python](https://github.com/ASS-G/Python-Training-Kit)
    - [Hello World using Print function](https://github.com/ASS-G/Batch-1-Assignments/blob/master/Assignment%201/180501000/hello_world.py)

  - **Still stuck?**
    - :warning: Try doing the assignment by yourself before proceeding.
    - [Video describing how to submit the pull request](https://drive.google.com/file/d/1wZX83l7aphEwwgEfdCWTZqeg3XM8pc3O/view?usp=sharing)


### **Assignment 2 - Python Basics and Strings**
  - **Problem 1 (robberThief.py)**
    - Given an amount robbed by a thief ,who’s aim was to rob more than 20,000, classify the profit of the thief as following:
         - Loss if he has robbed less than `5000`
         - Moderate if it is between `5000` to `19999`
         - Good theft if more than `20000`

    - **Sample Input**
    ```
    Enter the amount robbed by the thief: 9500
    ```
    - **Sample Output**
    ```
    Profit is Moderate
    ```


  - **Problem 2 (occurances.py)**
    - Print the characters in a string along with the number of occurances of those characters.

    - **Sample Input**
      ```
      Enter the String: aabbccddee
      ```
    - **Sample Output**
      ```
      Occurances:
      a -> 2
      b -> 2
      c -> 2
      d -> 2
      e -> 2
      ```


  - **Problem 3 (attendanceStudents.py)**
    - The details of students and their respective attendance
details are given below. Using the concepts of lists and Strings in Python. Print the names of the students who were present
    - The name and their Attendance statuses are separated by "-"
    - `P` stands for Present while `A` stands for Absent

          Ram-P
          Malar-A
          Ahuja-P
          Vijay-P
          Harini-A

    - **Sample Input**
      ```
      Enter your String:
      Leena-P
      Steve-A
      Dinesh-P
      Pragya-P
      ```
    - **Sample Output**
      ```
      The present students were:
      Leena Dinesh Pragya
      ```

  - **Resources**
    - [Python Basics and Strings](https://nbviewer.jupyter.org/github/ASS-G/Python-Training-Kit/blob/master/notebook/Python_Basics_and_Strings.ipynb)
    - [Getting started with Python](https://github.com/ASS-G/Python-Training-Kit)



FAQ:
======

  #### When should I submit the pull request?
  Just submit it once you're done an assignment.

  #### Fork? Pull request? What is all that? I don't know how to use GitHub!
  If you are new to Git or GitHub, check out this [small tutorial.](https://guides.github.com/activities/hello-world/)

  #### Where are the rest of the assignments?
  Our code ninjas are hard at work preparing the rest of the problems. Don't worry, they'll be up soon.

  #### How should I complete these programs?
  We have a folder for each assignment. Simply create a folder with your `registration_number` ,  complete your code and move the file into that folder.
  Some examples:
  If your `registration_number` is **180501XXX** submitting `assignment Y` then:
  1. Go to the folder `assignment Y`
  2. Create a folder `180501XXX` inside `assignment Y`
  3. Upload your code in the path `assignment Y\\180501XXX`

  **:no_entry_sign: Please do not modify any existing files in the repository.**

  #### I forked the repository but some problems were added only after that. How do I access those problems?
  Not to worry! Open your nearest terminal or command prompt and navigate over to your forked repository. Enter these commands:
  ```bash
  git remote add upstream https://github.com/ASS-G/Batch-1-Assignments.git
  git fetch upstream
  git merge upstream/master
  ```
  If you're curious, the commands simply add a new remote called upstream that is linked to this repository. Then it 'fetches' or retrieves the contents of the repository and attempts to merge it with your progress.
  Note that if you've already added the upstream repository, you don't need to re-add it in the future while fetching the newer questions.

  #### I received a merge error. What do I do?
  This shouldn't happen unless you modify an existing file in the repository. There's a lot of potential troubleshooting that might be needed, but the simplest thing to do is to make a copy of your code outside the repository and then clone it once again. Now repeat the steps from the answer above. Merge it and then add your code. Now proceed as usual. :)

  #### I'm facing difficulties with/need help understanding a particular question.
  Contact one of the board members or open up an [issue](https://github.com/ASS-G/Batch-1-Assignments/issues) on this repository and we'll do our best to help you out.

###### [:arrow_up: Back to Top](#----)


![wave](http://cdn.thekrishna.in/img/common/border.png)
