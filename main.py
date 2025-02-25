
import pandas as pd
import matplotlib.pyplot as plt
from spire.doc import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.stats import ttest_rel




def sig():
    ttest = ttest_rel(grade_df[f'{kategori1}'], grade_df[f'{kategori2}'])
    degrees_freedom = (grade_df.shape[0] - 1)
    content_paragraph2030 = section.AddParagraph()
    content_paragraph2030.AppendText("En t-test ble kjørt for å sjekke forskjeller mellomgruppene")
    content_paragraph2030.AppendText(
        f"T testen er tohalet og basert på parrete verdier (paired sample):\n p= {ttest[1]}, df = {degrees_freedom}")
    if 0.05 < ttest[1]:
        content_paragraph2030.AppendText("\nVed alfanivå 0.05 er det ingen signifikant forskjeller.")
    else:
        content_paragraph2030.AppendText("\nVed alfanivå 0.05 er det en signifikant forskjell mellom de to gruppene.")


print(
    "Velkommen til den automatiske rapporten for karakter endring.\nProgrammet skriver automatisk raport med deskriptiv statistikk til to grupper/kategorier av karakterer (f.eks to forskjellige år, arbeidskrav eller kategori av vanskelighet).\nEt boxplot blir så generert basert på karakterene.\nDeretter kjøres en paret t-test for å se etter signifikante forskjeller.\nTil sist lagres rapporten i et word-kompatibelt format.")

input("Trykk en tast for å velge excel fil. ")
root = Tk()
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

if not len(filename) < 4:
    filename = askopenfilename()
else:
    pass

root.withdraw()
Tk().quit()

kategori1 = input("Hva er tittelen på første karakter kategori? Bruk ordrett tittel fra kolonnens første celle. ")
kategori2 = input("Hva er tittelen på andre karakter kategori? Bruk ordrett tittel fra kolonnens første celle. ")

print(filename)

document = Document()

section = document.AddSection()
section.PageSetup.Margins.All = 72
title = input("Hvilket år gjelder rapporten for.")
grade_df = pd.read_excel(f'{filename}', usecols='A, B')

while kategori1 not in grade_df.columns:
    kategori1 = input(
        f"Gjenta tittelen på første karakter kategori. {kategori1} er ikke riktig. Bruk ordrett tittel fra kolonnens tittel celle. ")

while kategori2 not in grade_df.columns:
    kategori2 = input(
        f"Gjenta tittelen på andre karakter kategori. {kategori2} er ikke riktig. Bruk ordrett tittel fra kolonnens tittel celle. ")

titleParagraph = section.AddParagraph()
titleParagraph.AppendText(f"Rapport for år {title} - {kategori1} og {kategori2}")
titleParagraph = titleParagraph.ApplyStyle(BuiltinStyle.Heading1)

content_paragraph2023 = section.AddParagraph()
content_paragraph2023.AppendText("\n" + f"Karakter er lagret i: {filename}" + "\n")

if 1 in grade_df[f'{kategori1}'].unique():
    print(f"Stryk registrert i kategorien {kategori1}")
    stryk_kat1 = True
    stryk_kat1_count = grade_df[f'{kategori1}'].value_counts().get("1")
    print("Antall stryk:", stryk_kat1_count)
else:
    stryk_kat1_count = 0
    print(f"Ingen stryk i kategori {kategori1}")
    pass
count6 = 0
for cell in grade_df[f'{kategori1}']:
    if cell == 6:
        count6 += 1
print(count6)

if 1 in grade_df[f'{kategori2}'].unique():
    print(f"Stryk registrert i kategorien {kategori2}")
    stryk_kat2 = True
    stryk_kat2_count = grade_df[f'{kategori2}'].value_counts().get("1")
    print("Antall stryk:", stryk_kat2_count)
else:
    stryk_kat2_count = 0
    print(f"Ingen stryk kategorien {kategori2}")
    pass
count6k2 = 0
for cell in grade_df[f'{kategori2}']:
    if cell == 6:
        count6k2 += 1
print(count6k2)

if stryk_kat1_count > 0:
    content_paragraph2026 = section.AddParagraph()
    content_paragraph2026.AppendText(
        "\nDet var totalt " + str(stryk_kat1_count) + f" som ikke besto oppgaver i {kategori1}.")
else:
    pass

content_paragraph2024 = section.AddParagraph()
content_paragraph2024.AppendText(f"\nGjennomsnitt karakter for {kategori1} er: " + str(
    grade_df[f'{kategori1}'].mean()) + "\n" + "Standardavvik er " + str(grade_df[f'{kategori1}'].std()) + ".")
content_paragraph2024.AppendText("\nDet var totalt " + str(count6) + " som fikk toppkarakter.")

content_paragraph2027 = section.AddParagraph()
content_paragraph2027.AppendText(f"\nGjennomsnitt karakter {kategori2} er: " + str(
    grade_df[f'{kategori2}'].mean()) + "\n" + "Standardavvik er " + str(grade_df['Avansert'].std()) + ".")
content_paragraph2027.AppendText("\nDet var totalt " + str(count6k2) + " som fikk toppkarakter.")

if stryk_kat2_count > 0:
    content_paragraph2027.AppendText(
        "\nDet var totalt " + str(stryk_kat2_count) + f" som ikke besto oppgaver i {kategori2}.")
else:
    pass

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
boxplot2024 = grade_df[[f'{kategori1}', f'{kategori2}']].plot(kind='box', title='2024 Karakterer')
plt.savefig(f'{title} -karakterer.png')

content_paragraph2029 = section.AddParagraph()
image2023 = content_paragraph2029.AppendPicture(f'{title} -karakterer.png')
image2023.Width = 200
image2023.Height = 200
image2023.TextWrappingStyle = TextWrappingStyle.Inline

sig()
document.SaveToFile(f"Output/Karakterer for år {title} -{kategori1} og {kategori2} .docx", FileFormat.Docx2019)
