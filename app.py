"""
Create a Python Flask application for a researcher's profile page. The app should:
- Import Flask, os, bibtexparser, and a function called generate_researcher_personal_page from a separate module.
- Define utility functions to parse a BibTeX file (located at "bib_files/own-bib.bib") and filter entries for conference papers (ENTRYTYPE "inproceedings"), journal articles (ENTRYTYPE "article"), and patents (ENTRYTYPE "misc").
- Generate HTML lists from these entries.
- Include a route ("/") that calls a function generate_researcher_personal_page to generate a static HTML page, then renders a template file "index.html" by passing in the generated publication data.
- Run the app in debug mode when executed.
Output the complete Python file.
"""

from flask import Flask, render_template
import os
from generate_static_page import generate_researcher_personal_page
from logic_processing import generate_full_publications_html

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    generate_researcher_personal_page()
    return render_template("index.html", **publications)

if __name__ == "__main__":
    app.run(debug=True)   