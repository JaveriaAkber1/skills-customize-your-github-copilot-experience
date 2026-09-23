# 📘 Assignment: Python Functions and File Handling

## 🎯 Objective

Practice writing reusable Python functions and reading from and writing to text files by building a small student data tool.

## 📝 Tasks

### 🛠️ Average Calculator

#### Description
Write a function called `calculate_average()` that takes a list of numbers and returns their average.

#### Requirements
Completed program should:

- Accept a list of numeric values as an argument.
- Return the average as a float.
- Handle an empty list gracefully by returning `0`.
- Example usage:
  ```python
  print(calculate_average([80, 90, 100]))  # 90.0
  ```

### 🛠️ Save a Study Log

#### Description
Write a function called `write_report()` that creates a file containing a short study log.

#### Requirements
Completed program should:

- Take a filename and a list of strings as arguments.
- Write each item to the file on a new line.
- Return a message confirming the file was created.
- Example output:
  ```python
  print(write_report("study_log.txt", ["Monday: Reviewed loops", "Tuesday: Practiced functions"]))
  # Report saved to study_log.txt
  ```

### 🛠️ Read Student Scores

#### Description
Write a function called `read_scores()` that reads a text file containing student names and scores, then prints a summary.

#### Requirements
Completed program should:

- Open a file containing lines in the format `Name,Score`.
- Read each line and parse the values.
- Print each student and their score.
- Return the number of students read.
- Example file content:
  ```text
  Ava,92
  Ben,85
  Cara,90
  ```
