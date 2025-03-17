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
from string import Template
import bibtexparser

def parse_bib_file(bib_path):
    with open(bib_path, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def get_conference_papers(entries):
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'inproceedings']

def get_journal_articles(entries):
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'article']

def get_patents(entries):
    patents = [entry for entry in entries if entry.get('ENTRYTYPE', '').lower() == 'misc']
    if not patents:
        print("Warning: Entry type 'patent' not standard. Not considered.")
    return patents

def generate_html_list(entries):
    list_items = []
    for entry in entries:
        entry_type = entry.get('ENTRYTYPE','').lower()
        if entry_type == 'inproceedings':
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('booktitle','Conference')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'article':
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('journal','Journal')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'misc':
            authors = entry.get('author', 'Unknown Authors')
            list_items.append(
                f"<li>{entry.get('title','No title')} by {authors} - {entry.get('number','Patent number')} {entry.get('year','')}</li>"
            )
    return "<ul>\n" + "\n".join(list_items) + "\n</ul>"

def generate_full_publications_html(bib_path):
    entries = parse_bib_file(bib_path)
    conference_html = generate_html_list(get_conference_papers(entries))
    journal_html = generate_html_list(get_journal_articles(entries))
    patents_html = generate_html_list(get_patents(entries))
    return {"conference": conference_html, "journal": journal_html, "patents": patents_html}

# add a function that recreate the researcher_personal_page.html file
def generate_researcher_personal_page():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    
    with open(os.path.join(current_dir, "jinja_templates", "reasercher_personal_page.template.html"), "r", encoding="utf-8") as f:
        template_content = f.read()
    
    template = Template(template_content)
    final_html = template.substitute(publications)
    
    with open(os.path.join(current_dir, "templates", "reasercher_personal_page.html"), "w", encoding="utf-8") as f:
        f.write(final_html)


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    
    with open(os.path.join(current_dir, "jinja_templates", "reasercher_personal_page.template.html"), "r", encoding="utf-8") as f:
        template_content = f.read()
    
    template = Template(template_content)
    final_html = template.substitute(publications)
    
    with open(os.path.join(current_dir, "templates", "reasercher_personal_page.html"), "w", encoding="utf-8") as f:
        f.write(final_html)


if __name__ == "__main__":
    main()