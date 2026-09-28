from rich.console import Console

console = Console()

def print_sandwich(bread="White", meat="Ham", cheese="Cheddar", sauce="Mayo", toasted=False, is_cut=False):
    # --- 1. HEX COLOR DEFINITIONS ---
    COLORS = {
        "bread_fresh": "#F5DEB3", 
        "bread_toast": "#5D2906",  # Darker brown for better "toasted" contrast
        "ham": "#FFB6C1",          
        "turkey": "#FFF8DC",       
        "beef": "#600000",         # Deep maroon (will trigger white text)
        "cheddar": "#FFA500",      
        "swiss": "#FFFFE0",        
        "mayo": "#FFFFFF",         
        "mustard": "#FFDB58",      
        "ketchup": "#D32F2F",      
        "none": "#000000"        
    }

    # --- 2. CONTRAST HELPER ---
    def get_text_color(hex_color):
        """Returns 'white' or 'black' based on background brightness."""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        # YIQ formula for perceived brightness
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "white" if brightness < 128 else "black"

    # --- 3. LOGIC & ASSEMBLY ---
    b_color = COLORS["bread_toast"] if toasted else COLORS["bread_fresh"]
    
    gap = "  " if is_cut else ""
    width = 40

    def get_layer_text(text, bg_hex, w=width, italic=False):
        fg = get_text_color(bg_hex)
        style = f"{fg} on {bg_hex}"
        if italic: style = f"italic {style}"
        
        display_text = text.center(w)
        if is_cut:
            half = w // 2
            left = display_text[:half]
            right = display_text[half:]
            return f"[{style}]{left}[/]{gap}[{style}]{right}[/]"
        return f"[{style}]{display_text}[/]"

    # --- 4. PRINTING ---
    # Top Bread
    console.print(get_layer_text(bread, b_color))
    
    # Meat Layer
    m_hex = COLORS.get(meat.lower(), "#BEBEBE")
    console.print("  " + get_layer_text(meat, m_hex, width - 4))
    
    # Cheese Layer
    c_hex = COLORS.get(cheese.lower(), "#F4D03F")
    console.print("  " + get_layer_text(cheese, c_hex, width - 4))
    
    # Sauce Layer
    s_hex = COLORS.get(sauce.lower(), "#000000")
    if sauce.lower() != "none":
        console.print(get_layer_text(f"~ {sauce} ~", s_hex, italic=True))
    
    # Bottom Bread
    console.print(get_layer_text(bread, b_color))
    print()


def random_sandwich():
    import random

    bread = random.choice(['white', 'wheat', 'sourdough', 'rye'])
    meat = random.choice(['beef', 'turkey', 'ham', 'salami', 'bologna'])
    cheese = random.choice(['swiss', 'american', 'cheddar'])
    sauce = random.choice(['mustard', 'ketchup', 'mayo'])
    toasted = random.choice([True, False])
    is_cut = random.choice([True, False])

    print(f"{bread=}\n{meat=}\n{cheese=}\n{sauce=}\n{toasted=}\n{is_cut=}")


if __name__ == '__main__':
    random_sandwich()
