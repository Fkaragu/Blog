## One Minute Pitch
## Pitch is a web application that gives you 60 seconds to pitch your idea.
### 08 February 2019
#### By **[Francis T Karagu]**

## Description
Pitch is a web application that provides a platform for the user to pitch his / her idea and get comment on it from the public. For one to see the comment or pitch an idea you must have signed in mean you have to be a user.

## Specifications
### Who is the target User?
* Anyone who wants to Pitch an idea and get feedback.

### Front-end/User Interface Logic Objectives
* By default the page will load and provide three categories and a sign up option.
* Home: This is the current landing page
* Interview: This is the section to be used for pitching Interview related statements
* Pickup Line: This is the section to be used for pitching Pickup line related statements
* Promotion: This is the section to be used for pitching Promotion related statements
* Sign In: This is the section to be used for signing in or creating new members.

### Back-end/Business logic Objectives
* The application is using a postgres database to store data.
* Once a user is created he / she can sign in and post or comment on available posts.

### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View Home | Click on the Pitch | Loads the home page. |
| View Home | Click on the Category | Loads the home page. |
| View Interview | Click on the Interview | Validation helps to check if you are logged in. If yes page load else you are routed to sign in page.|
| View Pickup Line | Click on the Pickup Line | Validation helps to check if you are logged in. If yes page load else you are routed to sign in page.|
| View Promotion | Click on the Promotion | Validation helps to check if you are logged in. If yes page load else you are routed to sign in page.|

## Prerequiites
    - Python 3.6 required

## Application link
Here is a live working link https://thashpitch.herokuapp.com/

## Set-up and Installation
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py

    Incase you need to access / improve the application please follow the below steps
    1.  Use this command $ git clone <https://github.com/Fkaragu/Pitch>
        This will clone the projects repository into a local folder on your device.
    2.  Open the files with an editor( preferably Atom. )
    3.  Study the code. learn from it. Improve on it.

## Known bugs
No known errors.

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap

## Support and contact details
In case of any problems reach me through my email:fkaragu@gmail.com

### License
Copyright (c) {2019} **{Francis Thande Karagu}**
Permission is hereby granted, free of charge, to any person willing to obtain a copy of this program for personal use. However if the program will be used for commercial gain then a royalty fee will have to be paid to the author of the program.
