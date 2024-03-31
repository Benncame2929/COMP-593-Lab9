from tkinter import Tk, ttk
from tkinter import messagebox

from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2)

info_frame = ttk.LabelFrame(root, text="Info")
info_frame.grid(row=1, column=0, sticky="N", padx=(10, 5), pady=(5, 10))

stats_frame = ttk.LabelFrame(root, text="Stats")
stats_frame.grid(row=1, column=1, sticky="N", padx=(5, 10), pady=(5, 10))

# Populate the user input frame with widgets
input_lbl = ttk.Label(input_frame, text="Pokemon Name:")
input_lbl.grid(row=0, column=0, padx=(10, 5), pady=10)

input_ent = ttk.Entry(input_frame)
input_ent.grid(row=0, column=1, padx=5, pady=10)

# Function to get and display Pokemon information
def get_info():
    poke_name = input_ent.get().strip().lower()
    if not poke_name:
        messagebox.showerror("Error", "Please enter a Pokemon name.")
        return

    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        # Update info labels
        height_val["text"] = f"{poke_info['height']} dm"
        weight_val["text"] = f"{poke_info['weight']} hg"
        types = [t["type"]["name"] for t in poke_info["types"]]
        type_val["text"] = ', '.join(types).title()

        # Update stats bars
        for i, stat in enumerate(poke_info["stats"]):
            stat_bars[i]["value"] = stat["base_stat"]
            stat_labels[i]["text"] = stat["stat"]["name"].replace('-', ' ').title() + ":"
    else:
        messagebox.showerror("Error", "Could not fetch information for the selected Pokemon. Please ma")

# Populate the info frame
height_lbl = ttk.Label(info_frame, text="Height:")
weight_lbl = ttk.Label(info_frame, text="Weight:")
type_lbl = ttk.Label(info_frame, text="Type:")
height_val = ttk.Label(info_frame, width=20)
weight_val = ttk.Label(info_frame, width=20)
type_val = ttk.Label(info_frame, width=20)

height_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
weight_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
type_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=(5, 10))
height_val.grid(row=0, column=1, sticky="W", padx=(5, 10), pady=(10, 5))
weight_val.grid(row=1, column=1, sticky="W", padx=(5, 10), pady=5)
type_val.grid(row=2, column=1, sticky="W", padx=(5, 10), pady=(5, 10))

# Populate the stats frame with labels and progress bars for each stat
MAX_STAT = 255
BAR_LENGTH = 200
stat_names = ["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]
stat_bars = []
stat_labels = []

for i, stat_name in enumerate(stat_names):
    lbl = ttk.Label(stats_frame, text=f"{stat_name}:")
    lbl.grid(row=i, column=0, sticky="E", padx=(10, 5), pady=(5, 5))
    bar = ttk.Progressbar(stats_frame, maximum=MAX_STAT, length=BAR_LENGTH)
    bar.grid(row=i, column=1, padx=(5, 10), pady=(5, 5))
    stat_bars.append(bar)
    stat_labels.append(lbl)

# Add button to fetch Pokemon information
input_btn = ttk.Button(input_frame, text="Get Info", command=get_info)
input_btn.grid(row=0, column=2, padx=(5, 10), pady=10)

# Run the main window loop
root.mainloop()
