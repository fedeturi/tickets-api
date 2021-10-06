<!--
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Development Team Ticket API</h3>

  <p align="center">
    An API endpoint that integrates with TRELLO to create development tickets.
  </p>
</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* _[Python](https://www.python.org/downloads/)_

* PIP

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fedeturi/tickets-api.git
   ```
2. Create venv

   ```sh
   python -m venv tickets-api
   ```
3. Activate venv

	Windows
   ```sh
   tickets-api\Scripts\activate
   ```

	UNIX systems
   ```sh
   source tickets-api/bin/activate
   ```

4. Install dependencies 

	Install all dependencies from `requirements.txt`	
   ```sh
   pip install -r requirements.txt
   ```

4. Run project

	Change directory 
   ```sh
   cd devtickets
   python manage.py runserver
   ```

	Open a web browser and go to `https://trello.com/b/Vxv7dECV/space-x` to see the TRELLO board that will be updated when using the API.

<!-- USAGE EXAMPLES -->
## Usage

You can create new Tickets in the board, with one of the following types:
* __An issue:__ This represents a business feature that needs implementation, provide a short title and a description. All issues gets added to the “To Do” list as unassigned.

* __A bug:__ This represents a problem that needs fixing. Provide a description, and the title is randomized with the following pattern: bug-{word}-{number}. It doesn't matter that they repeat internally. They will have the “Bug” label.

* __A task:__ This represents some manual work that needs to be done. Provide a title and a category (Maintenance, Research, or Test) each corresponds to a label in trello. 

You can test the endpoint with the HTML client `client-form.html` using a web-browser, or other tools such as a python script (coming soon) using the _Requests module_, or `curl`.

The following are some examples for every use case, using curl:

	Create ISSUE Ticket 
   ```sh
   curl -d "title=Title&description=description&type=issue" http://localhost:8000/ticket/
   ```

	Create Maintenance TASK Ticket 
   ```sh
   curl -d "title=Title&category=Maintenance&type=task" http://localhost:8000/ticket/
   ```
   ```

	Create BUG Ticket 
   ```sh
   curl -d "description=description&type=bug" http://localhost:8000/ticket/
   ```



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Federico Brun - [@fedeturi](https://twitter.com/fedeturi) - [fedejbrun@gmail.com](mailto:fedejbrun@gmail.com)

Project Link: [https://github.com/fedeturi/tickets-api.git](https://github.com/fedeturi/tickets-api.git)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
