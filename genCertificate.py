from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Configurazioni
template_path = 'certificatoIPPOG2025.png' #attestato_template.png'  # Percorso del template
font_path = 'Arial.ttf'  # Percorso del font (assicurati di avere questo file o cambialo con uno disponibile)
font_size = 30  # Dimensione del testo
output_dir = 'attestati2025'  # Cartella dove salvare gli attestati
csv_path = 'partecipanti.csv'  # Percorso del file CSV con i nomi

# Crea la cartella di output se non esiste
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Carica la lista dei partecipanti
df = pd.read_csv(csv_path)
df.info()

# Carica il font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Font non trovato. Assicurati che {font_path} esista.")
    exit()

# Cicla su ogni nome e crea l'attestato
for index, row in df.iterrows():
    nome = row['Nome']
    
    # Apri il template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Calcola la posizione del testo per centrarlo
    bbox = draw.textbbox((0, 0), nome, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    img_width, img_height = img.size
    x = (img_width - text_width) / 1.5
    y = img_height / 2.3  # Puoi aggiustare questa coordinata per la posizione verticale
    
    # Aggiungi il nome all'immagine
    draw.text((x, y), nome, fill="black", font=font)
    
    # Salva l'attestato
    output_path = os.path.join(output_dir, f'attestato_{nome}.png')
    img.save(output_path)
    print(f'Attestato creato per {nome}')

print("Tutti gli attestati sono stati generati.")
