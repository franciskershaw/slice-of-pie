# Slice of Pie!

## Code Institute's Milestone Project 4 - Full Stack Frameworks

Slice of Pie is the brainchild of Zoe Thexton, who produces custom triangular tables that fit seamlessly into any section of a person's living or bedroom. Designed using CAD software, the tables can be assembled by hand in a variety of sizes, types of wood, and number of shelving levels. The inspiration for this product came from the need to get creative with the limited space available in her own living room (and generally missing somewhere to put a cup of tea down as a result of this!), while the triangular shape is the inspiration for the name.  

## Table of Contents
* [UX](#ux)
    * [User Stories](#user-stories)
* [Planning and Design](#planning-and-design)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Surface Plane](#surface-plane)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Animations](#animations)
    * [Data Model](#data-model)
* [Features and Django Apps](#features-and-django-apps)
* [Existing Features](#existing-features)
* [Defensive design features](#defensive-design-features)
* [Features left to implement](#features-left-to-implement)
* [Technologies used](#technologies-used)
    * [Languages and frameworks](#languages-and-frameworks)
    * [Additional tools](#additional-tools)
* [Git commit messages](#git-commit-messages)
* [Testing](#testing)
* [Deployment](#deployment)
* [Setting up AWS](#setting-up-amazon-web-services-aws)
* [Setting up Emails](#setting-up-email-confirmations)
* [Cloning](#cloning)
* [Credits](#credits)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)  

  
## UX

My main goals for the creation of this website were as follows:
* 
* 
* 

### User Stories

#### Developer

As the developer of the site:

#### Site owner/administrator

#### Users

## Planning and Design

### Strategy Plane

(Intro)

The **focus** of the project is:
* 

The **business goals** of the stakeholder are:

* 
* 
* 

*Therefore...*

(Research phase)

* 
* 
* 

(Importance vs viability metric)

| Opportunity                | Importance | Viability
| -------------------------- | ---------- |-----------

| **Total**                  | **total**     | **total**

(Mostly viable, but here is what I'm leaving out)

* 
* 
* 

### Scope Plane

Based on research and planning achieved during the strategy plane, and considering any limitations of my current coding abilities, the features I decided were critical for the completion of my user stories were as follows:

#### Required functional specifications

* 

#### Content requirements

* 

#### Nice to haves

(intro to nice to haves)

* 

### Structure Plane

(intro to structure plane)

1. **Homepage, containing:**


#### Interaction Design

* 

#### Information Architecture

* 

### Skeleton Plane

(intro to skeleton)

#### Changes from skeleton plane to final result

* 

### Surface Plane

(Intro to surface and buzzwords)

* Professional

#### Colour Scheme

(Intro to colours)

* 

(screenshot)

#### Typography

(intro to typography and reasoning behind choices)

(screenshot of fonts)

![Nunito screenshot](static/images/nunito.png)

#### Animations

### Data Model

#### Conceptual Design Phase

A basic map of how I could get my various entities to interact with each other on a conceptual level was created as the below flowchart:

(screenshot)

#### Logical Design Phase

The finalised way my collections work would together on the backend is best illustrated by the below entity relationship diagram:

(screenshot)

#### Physical Design Phase

(Explanation of the database choice and how it is used)

#### Data models

(Bullet points of the models)

## Features and Django Apps

### Existing Features

#### Consistent across all pages

* 

#### Homepage

* 

#### Login and registration

* 

#### Products/product builder

* 

#### Profile

* 

#### Bag and wishlist

* 

#### Checkout

* 

#### Profile page

* 

### Defensive design features

(Intro to section)

#### On the frontend

#### On the backend

*Custom 404 and 500 pages were created as well*

### Features left to implement

## Technologies used

### Languages and frameworks

* **HTML5:** Language used for structure and content across all pages.
* **CSS3:** Language used to style elements from the HTML pages.
* **Bootstrap:** CSS and JavaScript framework which allowed for the quick implementation of the homepage modals and the grid system which greatly improved the responsiveness of each page.
* **JavaScript:** Programming language used to add interactivity to the homepage and implement the logic required to make the game work.
* **jQuery:** JavaScript framework which helped me select and manipulate elements with greater ease than purely through JavaScript.
* **Python:** Backend language used to control the logic on the site.
* **Flask:** Python framework used to simmplify the routing and HTML templating on the site.
* **MongoDB**: Non-relational database used to store and update the information provided by users of the site.

### Additional tools

* [Amiresponsive:](http://ami.responsivedesign.is/) Used to produce the hero image in README.md and check general responsiveness of the pages.
* [dbdiagram:](https://dbdiagram.io/home) Used to create my entity relationship diagram.
* [Favicon Generator:](https://realfavicongenerator.net/) Used to create the favicon on the browser tab.
* [FontAwesome:](https://fontawesome.com/) Large database of icons which I used all over the site to add to the visual language.
* [Free Formatter:](https://www.freeformatter.com/html-formatter.html) Used to help ensure code was consistently formatted across all files.
* [Github:](https://github.com/) Version control and storage of my code.
* [Gitpod:](https://gitpod.io/) Development environment where all the code was written.
* [Google Docs:](https://docs.google.com/) Used for note taking and was where much of my readme was initially written.
* Google Developer Tools: Used for debugging and testing of responsiveness across several screen sizes. Also vital to the testing of JavaScript functions as and when they were created.
* [Google Fonts:](https://fonts.google.com/) Provided my site with the 'Nunito' font.
* [InVision:](https://www.invisionapp.com/) Used to create all of my wireframes at the beginning of the development process.
* [JSHint:](https://jshint.com/) Checked my javascript code was valid and error free.
* [PEP8Online:](http://pep8online.com/) Confirmed that my Python code complied to PEP8 standards.
* [TinyJPG:](https://tinyjpg.com/) Service used to compress background images and help with site performance
* [Trello:](https://trello.com/) Used to split all tasks into several sprints, to help bring the development process in line with agile principles.
* [W3C CSS Validation Service:](https://jigsaw.w3.org/css-validator/) Confirmed that my CSS is legal.
* [W3C Markup Validation Service:](https://validator.w3.org/) Confirmed that my HTML code is legal.
* [WAVE:](https://wave.webaim.org/) Allowed me to evaluate and test the accessibility of the site.

## Git commit messages

For the commits on this project, I continued to follow the basic rules I had set during my three previous milestone projects. That is to say:

* Always use the imperative tense so that readers would read as *the purpose of this commit is to* - etc.
* Commit often, and keep messages as short as possible.
* Start comments where possible with a prefix that summarises what the commit is for, such as fix (for bugs), add, remove, amend, style, or docs (for anything added to README.md).
* Include the file name or function in question where possible.
* Use the prefix 'logic:' in any commits aimed at amending or adding in something that was specifically related to backend logic.
* Use the prefix 'test:' for any commits that were being pushed specifically to test bug fixes onto the live site.

At the time of writing, these are among my recent commit messages and illustrate the format I applied for this project:

## Testing

Please see a full report of the testing applied to this project [here.](testing.md)

## Deployment

## Setting up Amazon Web Services (AWS)

## Setting up email confirmations

## Cloning

## Credits

### Media

* 

### Acknowledgements

A huge thank you to all the people who took part in user testing, the Code Institute's Slack community, and my mentor Aaron Sinnott for advice at various stages during development of the site.