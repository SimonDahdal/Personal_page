from flask import Flask, render_template
import os
import bibtexparser
from generate_static_page import generate_researcher_personal_page

app = Flask(__name__, template_folder='templates')

def parse_bib_file(bib_path):
    with open(bib_path, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def get_conference_papers(entries):
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'inproceedings']

def get_journal_articles(entries):
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'article']

def get_patents(entries):
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'misc']

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
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('number','Patent number')} {entry.get('year','')}</li>"
            )
    return "<ul>\n" + "\n".join(list_items) + "\n</ul>"

def generate_full_publications_html(bib_path):
    entries = parse_bib_file(bib_path)
    conference_html = generate_html_list(get_conference_papers(entries))
    journal_html = generate_html_list(get_journal_articles(entries))
    patents_html = generate_html_list(get_patents(entries))
    return {"conference": conference_html, "journal": journal_html, "patents": patents_html}

@app.route("/")
def index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bib_path = os.path.join(current_dir, "bib_files", "own-bib.bib")
    publications = generate_full_publications_html(bib_path)
    generate_researcher_personal_page()
    return render_template("reasercher_personal_page.html", **publications)

if __name__ == "__main__":
    app.run(debug=True)   