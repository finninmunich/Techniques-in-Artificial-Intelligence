#!/usr/bin/env python
# coding: utf-8

# # Programming Exercise 2: Constraint Satisfaction Problem

# Welcome Party
# 
# The student union is planning to hold a welcome party for the new students. 8 Students (Abigail, Brian,
# Caroline, Daniel, Edith, Frank, Grace, Harold) volunteer to perform in several shows. The following four
# types of shows are allowed to be performed on the party. (Each type of show is performed no more than
# once): Singing (costume for each student costs 50), Dancing (costume for each student costs 80), Comedy, Piano performance (costume for each student costs 100)
# 
# Consider the following constraints:
# 
# 1. Everyone should participate in exactly one show
# 2. No one performs alone
# 3. Every type of show is performed (each show must be performed at least by one student)
# 4. Total budget is less than or equal to 400
# 5. Singing requires at least 3 students if it is performed
# 6. Dancing requires a maximum of 2 students if it is performed
# 7. Comedy requires 2 or 3 students if performed
# 8. Piano is played by a single student if it is performed
# 9. Piano is played by two student if it is performed
# 10. Abigail performs together with Harold (other students could also perform with them)
# 11. Frank, Grace and Harold don't perform in the same show because they don't get along (any two of
# them don't want to perform together.)
# 12. Brian and Daniel don't want to dance
# 13. Abigail and Caroline don't want to perform the comedy
# 14. Edith and Grace want to sing (other students could also sing with them)
# 15. No one plays the piano 
#                                                                                          
# Model the constraint satisfaction problem in Python. For each of the following subsets of constraints,
# find the solution, if it exists:
# 
# Problem 2.1: { 1-2, 5-7, 9-14 }
# Problem 2.2: { 1, 3-8, 10-12, 14 }
# Problem 2.3: {1, 3-7, 9-13 }
# Problem 2.4: { 1-3, 6-7, 11-14 }
# Problem 2.5: {1-2, 4-7, 9-14 }
# Problem 2.6: { 1-2, 4-7, 10-15 }
# Note that problems 2.3 can not be satisfied.
# 
# 
#                                                                                          
# Programming Framework:
# 
# For this programming exercise Jupyter Notebooks will be used. The template for the exercise can be
# found in ARTEMIS. Since you have to model the constraint satisfaction problem, programming skills in
# Python lambdas, lists and dictionaries are necessary to complete this exercise. The following steps are
# required to correctly set up the environment for the programming exercise:
# 1. Installation of Anaconda and Download of the AIMA python code If you do not already
# have the Jupyter Notebook environment installed on your machine, the installation is the first
# step you have to perform. We recommend to install Anaconda, since this will set up the whole
# environment for you. The template for the programming exercise is based on the code from the
# AIMAcode project. Therefore, you first have to download the code from this project before the
# template can be used. Instructions for installation of Anaconda and AIMA python code can be
# found in AIMAinstallation
# 2. Pull of the template: Pull the repository with the template from ARTEMIS. To avoid issues
# with the relative file paths, we recommend to copy all files contained in the template into the
# root-directory of the AIMAcode project that you downloaded in the previous step.
#                                                                                          
# After completing the above steps, you are all set up to start with the exercise. The main function of
# the template is the Jupyter Notebook csp.ipynb, which is also the only file you have to
# work on. Your task is to model the Welcome Party problem. An example, on how to model a constraint
# satisfaction problem using the AIMAcode, is provided in the notebook. This is the same as given in
# Exercise 3.4.
# 
#                                                                                          
# Submission:
# 
# For submission, you have to upload the following files in ARTEMIS:
# 1. Copy csp.ipynb (notebook containing your solution for modelling the Welcome
# Party problem) to the pulled repository.
# 2. Add and commit the altered notebook to, and push it to ARTEMIS.
# A pass will be awarded only if:
# 1. you submitted the correct file with the correct name, as shown above.
# 2. you did not zip your file.
# 3. you pushed your files to your ARTEMIS branch.
# 4. you did not change the variable names provided by us within the template.
# 5. your submitted files can be run in an Anaconda environment (Python 3.7) with the packages pro-
# vided by the requirements.txt in the aima repository, the utils.py, the search.py and the csp programming exercise.py
# provided by us within a reasonable time (under 5 minutes).
# 6. the problem has been modelled correctly using the NaryCSP class from the module
# csp programming exercise.
# 7. like the rest of the programming exercises, this is an individual project and work must be your
# own. (We will use a plagiarism detection tool and any copied code will annul all bonus exercises
# from both the copier and the copied person!)
# 
# Submission will close on Sunday, 29.12.2020 at 23:59. Your solution will be marked by ARTEMIS.
# There will be feedback on formatting errors and rightly solved CSP. Nonetheless, it is very important to
# follow the instructions exactly!
# We offer preliminary checks of your solution and ARTEMIS will show your progress. You can submit
# your solution multiple times and get feedback for each submission. Your final submission will be checked.
# We award 1 point if all checks including plagiarism pass.
#                                                                                          
# 
# 
# <div class="alert alert-info">
#     <h3>Please read the following important information before starting with the programming exercise: </h3>
#     <p>In order to avoid problems with the relative file path we recommend to place the provided notebook and csp_programming_exercise.py file in the rootfolder of your <b>aima repository</b>.</p> 
#     <p>Do not use/install any additional packages, which are not provided in the requirements.txt of the  <b>aima repository</b>. </p>
#     <p>For modelling the constraint satisfaction problem you will have to define some variables. Do not change the names of variables that we provided you! Since we use these variables for an automatic evaluation, changing  variable names will result in failing the programming exercise. </p>
#     <p>Do not modify the example with the TWO + TWO = FOUR problem!</p>
#     <p>Do not modify the csp_programming_exercise.py!</p>
#     <p>After completing the exercise, download this jupyter notebook as *.py file (File &rarr; Download as 	&rarr; python (*.py)) </p>
#     <p>Before uploading this file together with your jupyter notebook to moodle, check if you can run <i>'python AI_Assignment2.py'</i> inside your anaconda environment in the root folder of your <b>aima repository</b>. If we are not able to run your submitted files in an environment with the packages provided by the requirements.txt of the <b>aima repository</b>, you will fail the programming exercise.</p>
#     
# </div>

# ## Initialization

# In[1]:


# Do not change this part.
import sys, os
import pathlib
sys.path.append(pathlib.Path().absolute())
from csp_programming_exercise import *


# ## Example for Solving a Constraint Satisfaction Problem

# In this exercise we are going to construct the Welcome Party problem as a constraint satisfaction problem in Python using the csp library. The "TWO + TWO = FOUR" problem from the exercise (see Problem 3.4) will help us to understand how to model a constraint satisfaction problem with this library.
# 

# ### Constructing the Domains: TWO + TWO = FOUR

# We start with constructing the domains for our problem. As an example the domains for the TWO + TWO = FOUR- problem from the csp library are given. 

# In[2]:


# Do not change this part
# Here we form the domains for the variables: T, F, W, O, U, R, C1, C2 and C3
# Domains are formed using key-value pairs,
# where the key stands for the variable and the value is for the possible values
# set(range(1, 4)) is a short way of creating an array with numbers from 1 to 4
# set (range(1, 4)) == [1, 2, 3]
# Tip: Remember that you can construct arrays with any variable types

domains_TF = {'T': set(range(1, 10)),
           'F': set(range(1, 10)),
           'W': set(range(0, 10)),
           'O': set(range(0, 10)),
           'U': set(range(0, 10)),
           'R': set(range(0, 10)),
           'C1': set(range(0, 2)), 
           'C2': set(range(0, 2)), 
           'C3': set(range(0, 2))
}


# ### Constructing the Constraints: TWO + TWO = FOUR

# We continue with defining the constraints for our problem, the most important part of any constraint satisfaction prolem. Let's take a look at the constraints for our "TWO + TWO = FOUR" problem to give you some insight about how to construct constraints with the csp library.

# In[3]:


# Do not change this part
# Here we define our constraints
# The constraint constructor of csp takes two arguments:
# 1. The variables that take part in the constraint
# 2. The constraint itself which is a function that takes the variables as arguments and returns true or false
# all_diff and eq are functions defined in csp 
# Like their name suggest all_diff returns true if every value is different
# and eq returns true if the two values are equal
# Tip: Take a look at the lambda operator in python https://www.w3schools.com/python/python_lambda.asp


constraint1_TF = Constraint(('T', 'F', 'W', 'O', 'U', 'R'), all_diff)
constraint2_TF = Constraint(('O', 'R', 'C1'), lambda o, r, c1: o + o == r + 10 * c1)
constraint3_TF = Constraint(('W', 'U', 'C1', 'C2'), lambda w, u, c1, c2: c1 + w + w == u + 10 * c2)
constraint4_TF = Constraint(('T', 'O', 'C2', 'C3'), lambda t, o, c2, c3: c2 + t + t == o + 10 * c3)
constraint5_TF = Constraint(('F', 'C3'), eq)


# ### Combine the constraints and set up the TWO + TWO = FOUR Problem

# In[4]:


# Do not change this part
# TWO + TWO = FOUR Problem
two_four_constraints = [constraint1_TF, constraint2_TF, constraint3_TF, constraint4_TF, constraint5_TF]
two_four = NaryCSP(domains_TF, two_four_constraints)


# ### Solve the TWO + TWO = FOUR Problem

# In[5]:


# Do not change this part
ac_search_solver(two_four)


# ## Programming Exercise Welcome Party

# ### Constructing the Domain

# In[109]:


# Define your domain here
# 50 represent Singing, 80 represent Dancing, 0 represent Comedy, 100 represent Piano
domains_WP={'Abigail':[50,80,0,100],
            'Brian':[50,80,0,100],
            'Caroline':[50,80,0,100],
            'Daniel':[50,80,0,100],
            'Edith':[50,80,0,100],
            'Frank':[50,80,0,100],
            'Grace':[50,80,0,100],
            'Harold':[50,80,0,100],
           }


# ### Constructing the Constraints: Welcome Party

# In[110]:


# Define you constraints here
constraint1_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: True)
constraint2_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: not a!=b!=c!=d!=e!=f!=g!=h)
constraint3_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: 50 in [a,b,c,d,e,f,g,h] and 80 in [a,b,c,d,e,f,g,h] and                            0 in [a,b,c,d,e,f,g,h] and 100 in [a,b,c,d,e,f,g,h])
constraint4_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: a+b+c+d+e+f+g+h <=400)
constraint5_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: [a,b,c,d,e,f,g,h].count(50) >= 3 if 50 in [a,b,c,d,e,f,g,h]                           else True)
constraint6_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: [a,b,c,d,e,f,g,h].count(80) <= 2 if 80 in [a,b,c,d,e,f,g,h]                           else True)
constraint7_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: [a,b,c,d,e,f,g,h].count(0) == 2 or [a,b,c,d,e,f,g,h].count(0)                            == 3 if 0 in [a,b,c,d,e,f,g,h] else True)
constraint8_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: [a,b,c,d,e,f,g,h].count(100) == 1 if 100 in [a,b,c,d,e,f,g,h]                             else True)
constraint9_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: [a,b,c,d,e,f,g,h].count(100) == 2 if 100 in [a,b,c,d,e,f,g,h]                             else True)
constraint10_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: a==h)
constraint11_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: f!=g and g!=h and f!=h)
constraint12_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: b!=80 and d!=80)
constraint13_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: a!=0 and c!=0)
constraint14_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: e==50 and g==50)
constraint15_WP = Constraint(('Abigail', 'Brian', 'Caroline', 'Daniel', 'Edith', 'Frank','Grace','Harold'),                             lambda a,b,c,d,e,f,g,h: 100 not in [a,b,c,d,e,f,g,h])


# ### Combine the constraints and set up the CSPs for the different problems

# <div class="alert alert-info">
#     <p>The variables csp_21, csp_22, .. are defined for setting up the CSPs for the corresponding problems. You have to use these variable names otherwise this will result in failing the programming exercise.</p> 
# </div>

# In[111]:


# Construct the Welcome Party Problems

# Combine Constraints and set up the csp for Problem 2.1
# TODO:
csp_21_constraints=[constraint1_WP, constraint2_WP, constraint5_WP, constraint6_WP, constraint7_WP,                     constraint9_WP, constraint10_WP, constraint11_WP, constraint12_WP, constraint13_WP,                    constraint14_WP]
csp_21 = NaryCSP(domains_WP, csp_21_constraints)

# Combine Constraints and set up the csp for Problem 2.2
# TODO:
csp_22_constraints=[constraint1_WP, constraint3_WP, constraint4_WP, constraint5_WP, constraint6_WP,                     constraint7_WP, constraint8_WP, constraint10_WP, constraint11_WP, constraint12_WP,                    constraint14_WP]
csp_22 = NaryCSP(domains_WP, csp_22_constraints)


# Combine Constraints and set up the csp for Problem 2.3
# TODO:
csp_23_constraints=[constraint1_WP, constraint3_WP, constraint4_WP, constraint5_WP, constraint6_WP,                     constraint7_WP, constraint9_WP, constraint10_WP, constraint11_WP, constraint12_WP,                    constraint13_WP]
csp_23 = NaryCSP(domains_WP, csp_23_constraints) 


# Combine Constraints and set up the csp for Problem 2.4
# TODO:
csp_24_constraints=[constraint1_WP, constraint2_WP, constraint3_WP, constraint6_WP, constraint7_WP,                     constraint11_WP, constraint12_WP, constraint13_WP, constraint14_WP]
csp_24 = NaryCSP(domains_WP, csp_24_constraints) 


# Combine Constraints and set up the csp for Problem 2.5
# TODO:
csp_25_constraints=[constraint1_WP, constraint2_WP, constraint4_WP, constraint5_WP, constraint6_WP,                     constraint7_WP, constraint9_WP, constraint10_WP, constraint11_WP, constraint12_WP,                    constraint14_WP]
csp_25 = NaryCSP(domains_WP, csp_25_constraints) 


# Combine Constraints and set up the csp for Problem 2.6
# TODO:
csp_26_constraints=[constraint1_WP, constraint2_WP, constraint4_WP, constraint5_WP, constraint6_WP,                     constraint7_WP, constraint10_WP, constraint11_WP, constraint12_WP, constraint13_WP,                    constraint14_WP,constraint15_WP,]
csp_26 = NaryCSP(domains_WP, csp_26_constraints) 


# ### Solving the CSP

# <div class="alert alert-info">
#     <p>Do not change the following cell. If you can't execute the following cell, you may have renamed the variables defined by us.</p> 
# </div>

# In[112]:


print(ac_search_solver(csp_21))
print(ac_search_solver(csp_22))
print(ac_search_solver(csp_23))
print(ac_search_solver(csp_24))
print(ac_search_solver(csp_25))
print(ac_search_solver(csp_26))


# In[ ]:




