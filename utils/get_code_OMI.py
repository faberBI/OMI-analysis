def extract_code_from_filename(row):
    """
    Estrae il codice prima di .kml dal percorso del file e il valore dopo 'OMI' dalla colonna 'Name'.
    """
    file_path = row['Fonte']
    filename = os.path.basename(file_path)  # Ottiene il nome del file
    code = os.path.splitext(filename)[0]  # Rimuove l'estensione .kml

    text = row['Name']
    match = re.search(r"OMI\s*(.*)", text)  # Cerca tutto ciò che viene dopo 'OMI'

    return code, match.group(1) if match else None
