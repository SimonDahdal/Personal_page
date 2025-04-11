"""
Create a Python script that generates a static HTML page from a template. The script should:
- Import os, the Template class from string, and bibtexparser.
- Define utility functions to parse a BibTeX file (located at "bib_files/own-bib.bib"), and filter for conference papers (ENTRYTYPE "inproceedings"), journal articles (ENTRYTYPE "article"), and patents (ENTRYTYPE "misc").
- Create a function generate_html_list that converts a list of publication entries into an HTML <ul> list.
- Create a function generate_full_publications_html that returns a dictionary with HTML for "conference", "journal", and "patents".
- Read the HTML template from "jinja_templates/reasercher_personal_page.template.html", substitute the placeholders ($conference, $journal, $patents) using string.Template, and write the final HTML output to "templates/reasercher_personal_page.html".
- Include a main function that performs the above operation when the script is run.
Output the complete Python file.
"""

import os
from jinja2 import Environment, FileSystemLoader

from logic_processing import parse_bib_file, get_conference_papers, get_journal_articles, get_patents, generate_html_list, generate_full_publications_html

# add a function that recreate the researcher_personal_page.html file
def generate_researcher_personal_page():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    
    env = Environment(loader=FileSystemLoader(os.path.join(current_dir, "jinja_templates")))
    template = env.get_template("reasercher_personal_page.template.html")
    final_html = template.render(
        conference=publications["conference"],
        journal=publications["journal"],
        patents=publications["patents"]
    )
    
    with open(os.path.join(current_dir, "./", "index.html"), "w", encoding="utf-8") as f:
        f.write(final_html)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    
    env = Environment(loader=FileSystemLoader(os.path.join(current_dir, "jinja_templates")))
    template = env.get_template("reasercher_personal_page.template.html")
    final_html = template.render(
        conference=publications["conference"],
        journal=publications["journal"],
        patents=publications["patents"]
    )
    
    with open(os.path.join(current_dir, "./", "index.html"), "w", encoding="utf-8") as f:
        f.write(final_html)


if __name__ == "__main__":
    main()