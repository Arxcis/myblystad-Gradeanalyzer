# Gradeanalyzer
Et program som analyserer to sett med karakterer ved å generere et boksplott, utføre en t-test, vise beskrivende statistikk og sammenfatte resultatene i et Word-dokument. Programmet er utviklet som et verktøy for emneevaluering og ble laget som en semesteroppgave i et grunnleggende Python-kurs ved USN.
Her er en GitHub-vennlig README-fil i Markdown-format for prosjektet ditt:


# 📊 Karakteranalyse og Automatisert Rapportgenerering  

Dette Python-programmet analyserer karakterdata fra en Excel-fil, genererer statistikk og visualiseringer, utfører en t-test for å undersøke forskjeller mellom to kategorier og lagrer resultatene i en Word-rapport.  

---

## 🚀 Funksjonalitet  

- **📥 Filvalg via GUI** – Brukeren velger en Excel-fil med karakterdata.  
- **📊 Deskriptiv statistikk** – Beregner gjennomsnitt, standardavvik og antall toppkarakterer.  
- **⚖️ Signifikanstest (t-test)** – Utfører en paret t-test for å sjekke om forskjellene mellom kategoriene er signifikante.  
- **📊 Data-visualisering** – Genererer et boxplot av karakterfordelingen.  
- **📤 Automatisert rapportgenerering** – Skriver analyseresultatene til et Word-dokument.  

---

## 🛠️ Teknologier og Biblioteker  

- **Python**  
- **pandas** – Databehandling  
- **matplotlib** – Plotting og visualisering  
- **SciPy** – Statistiske analyser (t-test)  
- **spire.doc** – Generering av Word-rapport  
- **tkinter** – GUI for filvalg  

---

## 🔧 Installasjon  

1. **Klon prosjektet**  
   ```bash
   git clone https://github.com/mblystad/Gradeanalyzer.git
   cd Gradeanalyzer
   ```
2. **Installer nødvendige biblioteker**  
   ```bash
   pip install pandas matplotlib scipy spire.doc tk
   ```
3. **Kjør programmet**  
   ```bash
   python main.py
   ```

---

## 📖 Brukerveiledning  

1. Start programmet, og velg en Excel-fil med karakterdata.  
2. Angi de eksakte kolonnenavnene for de to kategoriene som skal sammenlignes.  
3. Programmet beregner gjennomsnitt, standardavvik, teller stryk og toppkarakterer.  
4. En t-test utføres for å undersøke om forskjellen mellom gruppene er signifikant.  
5. Et boxplot genereres og lagres.  
6. En Word-rapport opprettes automatisk med alle analyseresultatene.  

---

## 🎯 Plan for Videre Utvikling  

- **📊 Flere sammenligningskategorier** – Utvide funksjonaliteten for å analysere mer enn to kategorier samtidig.  
- **🖥️ Forbedret GUI** – Implementere et mer brukervennlig grensesnitt med Tkinter.  
- **📈 Ekstra statistiske analyser** – Legge til ANOVA eller andre relevante tester.  

---

## 📜 Lisens  

Dette prosjektet er utviklet som en semesteroppgave ved USN og er ment for læringsformål.  

---

### ✉️ Kontakt  

Dersom du har spørsmål eller forslag til forbedringer, ta gjerne kontakt!  
