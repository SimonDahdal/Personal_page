# Researcher Profile Application

This application dynamically generates a researcher profile page by extracting publication data from a BibTeX file and embedding it into an HTML page. The process was developed using Python, Flask, Jinja2 templating, Bootstrap for styling, and the bibtexparser package to parse the bibliography data.

## Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework used to serve the dynamic HTML page.
- **Jinja2**: Templating engine used by Flask (placeholders in the HTML template).
- **bibtexparser**: Library to parse the BibTeX file.
- **Bootstrap 5**: CSS framework for quick, responsive design.

## Application Structure

- **/src**
  - **logic_processing.py**  
    Contains functions to parse the BibTeX file and generate HTML snippet lists for conference papers, journal articles, and patents.

  - **templates/researcher_personal_page.template.html**  
    HTML template with Jinja2 placeholders (`$conference`, `$journal`, `$patents`) that will be substituted with the generated HTML lists.

  - **generate_static_page.py** (optional)  
    A script that uses Python's `string.Template` to replace placeholders in the template and generate a final static HTML page.

  - **app.py** (optional)  
    A Flask application script that dynamically renders the HTML page using the generated publication data.

## Development Process With GitHub Copilot

1. **Project Setup:**
   - Created a new project folder and initialized the required files:  
     - `logic_processing.py` for processing the BibTeX data.
     - `templates/researcher_personal_page.template.html` as the HTML template.
     - Optionally, `app.py` for serving the dynamic page with Flask.
   - Installed required Python packages using:
     ```bash
     pip install flask bibtexparser
     ```

2. **Implementing BibTeX Parsing and HTML Generation:**
   - Used GitHub Copilot to assist in writing functions that:
     - Parse the BibTeX file (`parse_bib_file`).
     - Filter entries by type (conference papers, journal articles, patents).
     - Generate an HTML list of items for each section.
   - Copilot provided suggestions that were adjusted to fit the project’s needs.

3. **Creating the HTML Template:**
   - Developed [templates/researcher_personal_page.template.html](http://_vscodecontentref_/0) including placeholders (`$conference`, `$journal`, `$patents`) that would later be substituted with actual HTML content.
   - Used Bootstrap 5 CDN for responsive design.

4. **Integrating Python Output Into HTML:**
   - Two approaches were suggested:
     - **Dynamic**: Create a Flask application (`app.py`) that renders the template dynamically with Jinja2.
     - **Static**: Create a Python script (`generate_static_page.py`) that reads the template, substitutes the placeholders using Python's `string.Template`, and writes the final HTML page.
   - GitHub Copilot assisted in generating both approaches.

5. **Testing and Running the Application:**
   - For the Flask approach, run:
     ```bash
     python app.py
     ```
     Then visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
   - For the static approach, run:
     ```bash
     python generate_static_page.py
     ```
     Then open the generated `researcher_personal_page.html` in any browser.

## Deploying the Application Locally

To deploy the application locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. **Create and activate python venv**
  Ensure you have Python installed
    ```bash
    python3 -m venv env
    ```

    ```bash
    source env/bin/activate
    ```

3. **Install Dependencies:**
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application:**
   If you are using the Flask approach, start the Flask server:
   ```bash
   python app.py
   ```
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

5. **Generate a Static HTML Page:**
   If you prefer the static approach, generate the HTML page:
   ```bash
   python generate_static_page.py
   ```
   Open the generated `researcher_personal_page.html` in any browser to view the application.

## Conclusion

This project demonstrates how to create a dynamic researcher profile page that integrates BibTeX data with a web interface using Python and Flask. The development process was streamlined using GitHub Copilot to generate boilerplate code and guide through the implementation of parsing functions, HTML templating, and web integration.

Happy coding!