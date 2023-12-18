from PIL import Image, ImageFilter, ImageOps

def apply_instagram_filter(image):
    filtered_image = image.filter(ImageFilter.GaussianBlur(radius=10))
    return filtered_image

def main():
    # Spør brukeren om filstien til bildet
    filename = input("Skriv inn filstien til bildet: ")
    original_image = Image.open(filename)

    # Vis originalbildet
    original_image.show()

    # Sjekk om brukeren ønsker å bruke et filter
    bruk_filter = input("Vil du legge til et Instagram-filter? (ja/nei): ")

    if bruk_filter.lower() == "ja":
        # Anvend filteret
        filtered_image = apply_instagram_filter(original_image)

        # Vis bildet med filteret
        filtered_image.show()

    # spør om man vil ha et svart hvit bilde
    svart_hvit = input("Vil du gjøre bildet svart hvit? (ja/nei): ")

    if svart_hvit.lower() == "ja":
        # gjør bildet svart hvitt
        grayscale_image = original_image.convert('L')
        grayscale_image.show()

    # spør om den skal rotere
    rotere = input('Vil du rotere dette bildet? (ja/nei): ')

    if rotere.lower() == "ja":
        # Viser bildet før rotasjon
        rotated_image = original_image.rotate(angle=90, expand=True, fillcolor="white")
        rotated_image.show()

    # spør om man vil beskjære bildet
    beskjere = input("Vil du beskjære bildet? (ja/nei): ")

    if beskjere.lower() == "ja":
        # gir bildet et navn
   
        # åpner bildet
        img = Image.open(filename)
        # beskjærer bildet
        img_cropped = img.crop(box=(20, 20, 200, 200))
        # viser bildet
        img_cropped.show()

    # spør om du vil endre størrelsen på bildet
    størrelse = input("Vil du gjøre bildet større?(ja/nei): ")  

    if størrelse.lower() == "ja":
        # gir navn til bildet
     
        # endrer størrelsen slik at det er tilpasset instagram
        img = Image.open(filename)
        print(img.width, img.height)
        img_resized = img.resize((int(img.width*2), int(img.height*2)))
        print(img_resized.width, img_resized.height)
        # viser bildet forstørret
        img_resized.show()

størrelse = input("Vil du sette in en bilderamme?(ja/nei): ")  

if størrelse.lower() == "ja":
    
  img1 = Image.open("frosk.png")
img2 = ImageOps.fit(img1, (760,760))
ramme = Image.open("bilde.png")
polar = ramme.convert("RGB")
polar.paste(img2,(64,64))
polar.show()

if __name__ == "__main__":
    main()