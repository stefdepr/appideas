import csv

ingeschreven_leden_ok_pas = {}

with open('inschrijvingen zoo Antwerpem.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    index_ok_pas = header.index("Ik ben in het bezit van een ok-pass")
    index_voornaam = header.index("Voornaam")
    index_achternaam = header.index("Achternaam")
    with open('ok_pas_zoo.csv', 'a') as file:
        header_inclusion = []
        header_inclusion.append(header[index_achternaam])
        header_inclusion.append(header[index_voornaam])
        writer = csv.writer(file)
        writer.writerow(header_inclusion)

    for row in reader:

        if row[index_ok_pas] != 'false':
            print('traakt hier')

            list_to_write_csv = []
            list_to_write_csv.append(row[index_voornaam])
            list_to_write_csv.append(row[index_achternaam])

            print(list_to_write_csv)

            with open('ok_pas_zoo.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(list_to_write_csv)
