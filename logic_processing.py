"""
Create a Python module for processing a BibTeX file. The module should:
- Import bibtexparser.
- Define a function parse_bib_file that opens and parses a given BibTeX file ("bib_files/own-bib.bib"), returning the entries.
- Define a function get_conference_papers that filters entries with ENTRYTYPE equal to "inproceedings".
- Define a function get_journal_articles that filters entries with ENTRYTYPE equal to "article".
- Define a function get_patents that filters entries for patents (for this example, check for ENTRYTYPE "patent").
- Define a function generate_html_list that converts a list of entries into an HTML unordered list (<ul>) with each item detailing the title, publication venue, and year.
- Define a function generate_full_publications_html that uses the above functions to return a dictionary with keys "conference", "journal", and "patents", each value being the corresponding HTML list.
- Optionally, include example usage (e.g. in a main block) that prints out the generated HTML lists.
Output the complete Python file.
"""

import bibtexparser

def parse_bib_file(bib_path):
    """Load and parse the bib file."""
    with open(bib_path, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def get_conference_papers(entries):
    """Filter entries for conference papers (INPROCEEDINGS)."""
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'inproceedings']

def get_journal_articles(entries):
    """Filter entries for journal articles."""
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'article']

def get_patents(entries):
    """Filter entries for patents."""
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'misc']

def generate_html_list(entries):
    """Generate an HTML list from a list of bib entries."""
    list_items = []
    for entry in entries:
        authors = entry.get('author', 'No authors')
        entry_type = entry.get('ENTRYTYPE', '').lower()
        if entry_type == 'inproceedings':
            list_items.append(
                f"<li>{entry.get('title','No title')} - {authors} - {entry.get('booktitle','Conference')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'article':
            list_items.append(
                f"<li>{entry.get('title','No title')} - {authors} - {entry.get('journal','Journal')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'misc':
            list_items.append(
                f"<li>{entry.get('title','No title')} - {authors} - {entry.get('number','Patent number')} {entry.get('year','')}</li>"
            )
    return "<ul>\n" + "\n".join(list_items) + "\n</ul>"

def generate_full_publications_html(bib_path):
    """Return a dictionary with HTML for each section of published works."""
    entries = parse_bib_file(bib_path)
    conference_html = generate_html_list(get_conference_papers(entries))
    journal_html = generate_html_list(get_journal_articles(entries))
    patents_html = generate_html_list(get_patents(entries))
    return {
        "conference": conference_html,
        "journal": journal_html,
        "patents": patents_html
    }

# Example usage:
if __name__ == "__main__":
    bib_path = "./bib_files/own-bib.bib"
    publications = generate_full_publications_html(bib_path)
    
    # print("Conference Papers:")
    # print(publications["conference"])
    
    # print("\nJournal Articles:")
    # print(publications["journal"])
    
    print("\nPatents:")
    print(publications["patents"])