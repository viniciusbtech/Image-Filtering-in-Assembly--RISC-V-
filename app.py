from PIL import Image
import numpy as np

def aplicar_filtro_sobel(imagem):
    filtro_sobel = np.array([[-1, -2, -1],
                              [ 0,  0,  0],
                              [ 1,  2,  1]])
    
    imagem_cinza = imagem.convert('L')
    matriz_cinza = np.array(imagem_cinza)
    
    altura, largura = matriz_cinza.shape
    imagem_filtrada = np.zeros((altura, largura))

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):

            regiao = matriz_cinza[i-1:i+2, j-1:j+2]
            valor_filtrado = np.sum(regiao * filtro_sobel)
            imagem_filtrada[i, j] = valor_filtrado

    imagem_filtrada = np.clip(imagem_filtrada, 0, 255)
    imagem_filtrada = imagem_filtrada.astype(np.uint8)

    return Image.fromarray(imagem_filtrada)

def main():
    caminho_imagem_entrada = '4.jpg'
    caminho_imagem_saida = 'imagem_filtradapython.jpg'
    
    imagem = Image.open(caminho_imagem_entrada)
    
    imagem_filtrada = aplicar_filtro_sobel(imagem)
    
    imagem_filtrada.save(caminho_imagem_saida)
    print(f"Imagem filtrada salva em: {caminho_imagem_saida}")

if __name__ == "__main__":
    main()