# Karakterutvikling og Grafer 📊  

Dette programmet analyserer karakterdata lagret i en Excel-fil og visualiserer dem ved hjelp av grafer.  
Formålet er å kartlegge forskjeller i prestasjon basert på ulike kategorier, som år, arbeidskrav eller tema.  
I dette eksemplet brukes en **dummy-fil** hvor karakterene er delt inn i to hovedtemaer: **grunnleggende** og **avansert**.  

---

## 📌 Funksjonalitet  

Programmet er utviklet i henhold til oppgavetekstens innholdskrav og tilfredsstiller følgende:  

- **📂 Arrays** – Lagrede karakterer fordelt på to hovedtemaer (grunnleggende/avansert).  
- **🧮 Vektoriserte beregninger** – Beregning av gjennomsnitt og medianverdier i arrays.  
- **⚖️ If/else-tester** – If/else-tester for stryk, som må telles separat.  
- **🔄 For/while-løkker** – For-løkke for å sjekke toppkarakterer, som må telles separat.  
- **📥 Lese data fra fil** – Leser karakterer fra en Excel-fil.  
- **📤 Skrive data til fil** – Skriver statistikk (deskriptiv og signifikanstest) til dokument med plot.  
- **📊 Plotting** – Plotter de to kategoriene og henter informasjon fra forskjellige kolonner basert på brukerinput.  
- **🔧 Egendefinerte funksjoner** – Utfører signifikanstest med vurdering opp mot alfanivå.  

---

## 🚀 Plan for Videre Utvikling  
- Implementere **GUI** (Tkinter eller lignende) for valg av graf-type, statistikk og format på output-fil.  
- Åpne for sammenligning av **flere enn to kategorier**, noe som krever mer avanserte brukervalg og en annen type statistikk.  

---

## 🛠️ Teknologier og Biblioteker  
- **Python**  
- **Pandas** (databehandling)  
- **Matplotlib**
