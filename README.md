# Exercise 07.1 - Construction and Testing
## _CS4320/7320 Software Engineering_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Run

```sh
python3 -m pytest
```

## Restore Data

```sh
python3 RestoreData.py
```

## Features

`passed` login - System.py  
`passed` check_password - System.py  
`failed` change_grade - Staff.py
```sh
self.users[user]['courses'][course][assignment]['grade'] = 0
```
> should be

```sh
self.users[user]['courses'][course][assignment]['grade'] = grade
```
`passed` create_assignment - Staff.py  
`failed` add_student - Professor.py
```sh
self.users[self.name]['courses'][course] = assignments
```
> should be

```sh
self.users[name]['courses'][course] = assignments
```
`passed` drop_student - Professor.py  
`failed` submit_assignment - Student.py
```sh
due_date = self.all_courses['comp_sci']['assignments'][assignment_name]["due_date"]
```
> should be

```sh
due_date = self.all_courses[course]['assignments'][assignment_name]["due_date"]
```
`failed` check_ontime - Student.py
```sh
return True
```
> should be

```sh
return SomeDateComparisonFunction(submission_date, due_date)
```
`passed?` `failed?` check_grades - Student.py
> I'm not sure if this is a mistake by the professor because the "grade" key value is misspelled as "Grade" in some data, which causes a "KeyError". So I split it into two functions to test.

*hdjsr7's assignment2 of cloud_computing*
```sh
"hdjsr7":{
    "courses":{
        "cloud_computing":{
            "assignment1":{
                "grade":100,
                "submission_date":"1/3/20",
                "submission":"Blah Blah Blah",
                "ontime":true
            },
            "assignment2":{
                "Grade":100,
                "Submission Data":"2/3/20",
                "Submission":"Blah2 Blah2 Blah2",
                "ontime":true
            }
        },
        ...
    },
    "password":"pass1234",
    "role":"student"
}
```
*yted91's assignment2 of cloud_computing*
```sh
"yted91":{
    "courses":{
        "cloud_computing":{
            "assignment1":{
                "grade":3,
                "submission_date":"1/7/20",
                "submission":"Blah Blah Blah",
                "ontime":false
            },
            "assignment2":{
                "Grade":5,
                "Submission Data":"2/7/20",
                "Submission":"Blah2 Blah2 Blah2",
                "ontime":false
            }
        },
        ...
    },
    "password":"imoutofpasswordnames",
    "role":"student"
}
```
`failed` view_assignments - Student.py
```sh
course = self.all_courses['comp_sci']['assignments']
```
> should be

```sh
course = self.all_courses[course]['assignments']
```
`failed` check_password_with_unexisted_user - System.py
> When an incorrect username is entered, the system should return an account password error, not a crash.

`failed` create_assignment_with_wrong_ta - Staff.py
> TAs should not have the permission to create assignments that are not part of their courses.

`failed` create_assignment_with_wrong_professor - Staff.py
> Professors should not have the permission to create assignments that are not part of their courses.

`failed` drop_student_with_wrong_professor - Professor.py
> A professor should not have the permission to drop students from a course that is not his.

`failed` check_grades_with_wrong_ta - Staff.py
> TAs should not have the permission to check grades that are not part of their courses.

`failed` check_grades_with_wrong_professor - Staff.py
> Professors should not have the permission to check grades that are not part of their courses.

## License

MIT

**Free Software, Hell Yeah!**
