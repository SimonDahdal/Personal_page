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
    return [entry for entry in entries if entry.get('ENTRYTYPE','').lower() == 'patent']

def generate_html_list(entries):
    """Generate an HTML list from a list of bib entries."""
    list_items = []
    for entry in entries:
        entry_type = entry.get('ENTRYTYPE','').lower()
        if entry_type == 'inproceedings':
            # For conference papers, display title, conference name (booktitle) and year
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('booktitle','Conference')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'article':
            # For journal articles, display title, journal name and year
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('journal','Journal')} {entry.get('year','')}</li>"
            )
        elif entry_type == 'misc':
            # For patents, display title, patent number and year
            list_items.append(
                f"<li>{entry.get('title','No title')} - {entry.get('number','Patent number')} {entry.get('year','')}</li>"
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
    
    print("Conference Papers:")
    print(publications["conference"])
    
    print("\nJournal Articles:")
    print(publications["journal"])
    
    print("\nPatents:")
    print(publications["patents"])