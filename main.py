import numpy as np
import matplotlib.pyplot as plt

def calculate_pmf(image):
    # Renkli bir görüntüyü gri tonlamaya çevir (Opsiyonel)
    grayscale_image = np.mean(image, axis=-1)

    # Histogramı oluştur
    histogram, bin_edges = np.histogram(grayscale_image.flatten(), bins=256, range=[0, 256])

    # Olasılık kütle fonksiyonunu hesapla
    pmf = histogram / np.sum(histogram)

    return bin_edges[:-1], pmf

def plot_pmf(bin_edges, pmf, title='Olasılık Kütle Fonksiyonu (PMF)'):
    plt.bar(bin_edges, pmf, width=1.0, color='gray', edgecolor='black')
    plt.title(title)
    plt.xlabel('Pixel Değeri')
    plt.ylabel('Olasılık')
    plt.show()

def add_images(images):
    # İki fotoğrafı sırayla topla
    result_image = images[0]
    for image in images[1:]:
        result_image = np.add(result_image, image)

    return result_image

def display_menu(menu):
    options = list(menu.keys())
    options.sort()
    for entry in options:
        print(f"{entry}. {menu[entry]}")

def main():
    image_paths = [
        "C:\\Users\\Batuhan\\Downloads\\5.1.09.tiff",
        "C:\\Users\\Batuhan\\Downloads\\5.1.10.tiff",
        "C:\\Users\\Batuhan\\Downloads\\5.1.11.tiff",
        "C:\\Users\\Batuhan\\Downloads\\5.1.12.tiff",
        "C:\\Users\\Batuhan\\Downloads\\5.1.13.tiff",
        "C:\\Users\\Batuhan\\Downloads\\5.1.14.tiff",
    ]

    images = [plt.imread(image_path) for image_path in image_paths]

    menu = {
        '1': "Her fotoğrafın PMF değerini hesapla ve göster",
        '2': "İlk 3 fotoğrafı topla, PMF değerini hesapla ve göster",
        '3': "İlk 6 fotoğrafı topla, PMF değerini hesapla ve göster",
        '4': "Exit"
    }

    while True:
        display_menu(menu)
        selection = input("Please Select: ")

        if selection == '1':
            for i, image in enumerate(images, start=1):
                bin_edges, pmf = calculate_pmf(image)
                plot_pmf(bin_edges, pmf, f"Fotoğraf {i} PMF")
        elif selection == '2':
            combined_image = add_images(images[:3])
            bin_edges, pmf = calculate_pmf(combined_image)
            plot_pmf(bin_edges, pmf, "İlk 3 Fotoğrafın Toplamı PMF")
        elif selection == '3':
            combined_image = add_images(images[:6])
            bin_edges, pmf = calculate_pmf(combined_image)
            plot_pmf(bin_edges, pmf, "İlk 6 Fotoğrafın Toplamı PMF")
        elif selection == '4':
            break
        else:
            print("Geçersiz Seçenek!")

if __name__ == "__main__":
    main()
