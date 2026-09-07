# Activity 1 - Git Collaboration practice

## Purpose: 
This activity is designed to practice collaborative work using GitHub. Each team member works on a separate part of the project in their own branch, and changes are integrated into the shared repository.

## Project files

### `hello_world.py`
A simple introductory script that prints a personalized greetings. It displays the student's name, a welcome message, the course name, and an additional personalized message, along with a comment explaining part of the code.

### `financial_calculation.py`
A script that calculates the future value of an investment using the compound interest formula: future_value = present_value *(1 + interest_rate ** periods.
It includes two financial scenarios with different present values, interest rates, and periods, and prints a comparison between the two resulting future values.

## How to Run
Both scripts run with python 3 and require no additional libraries
python exercises/hello_world.py
python exercises/financial_calculation.py

## Team members and responsibilities
Andrea - Improved `hello_world.py` with a personalized message and code comments
Jorge - Added a second financial scenario and a comparison to `financial_calculation.py` 
Caro - Wrote this documentation 
Clemente - Reviewed all team's work and Pull requests

## Git workflow
1. Update the local repository before starting new work: git checkout main and git pull
2. Create an individual branch for each responsibility (never work directly on main)
3. Modify only the assigned file to avoid merge conflicts
4. Run and test the changes locally before committing
5. Check git status, then stage and commit with a descriptive message
6. Push the branch to GitHub with git push -u origin <branch-name>
7. Open a pull request from the branch into main, describing the change
8. Have at least one teammate review the Pull request before merging
9. Merge into main once approved, then update local copies with git checkout main and git pull
10. Verify the final files on GitHUb and stop the codespace when done
