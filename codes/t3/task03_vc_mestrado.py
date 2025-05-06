# Célula para coletar coordenadas dos 4 cantos do campo
import cv2
import numpy as np

# Carregando a imagem do campo de futebol
soccer_img = cv2.imread('../img/task03/soccer.jpg')
soccer_img_rgb = cv2.cvtColor(soccer_img, cv2.COLOR_BGR2RGB)

# Lista para armazenar as coordenadas
positions = []

# Função para coletar coordenadas usando cliques
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Usar a cópia da imagem para desenhar os círculos
        cv2.circle(img_display, (x, y), 5, (0, 0, 255), -1)
        positions.append([x, y])
        print(f"Ponto {len(positions)} adicionado: ({x}, {y})")
        cv2.imshow("Selecione os 4 cantos", img_display)
        
        # Quando tivermos 4 pontos, fechar automaticamente
        if len(positions) == 4:
            print("\nCoordenadas coletadas:")
            for i, pos in enumerate(positions):
                print(f"Ponto {i+1}: {pos}")

# Criando uma cópia da imagem para visualização
img_display = soccer_img.copy()

print("Clique nos 4 cantos do campo na seguinte ordem:")
print("1. Canto superior esquerdo")
print("2. Canto superior direito")
print("3. Canto inferior direito")
print("4. Canto inferior esquerdo")
print("\nA janela fechará automaticamente após selecionar os 4 pontos.")

cv2.imshow("Selecione os 4 cantos", img_display)
cv2.setMouseCallback("Selecione os 4 cantos", click_event)

# Esperar até que 4 pontos sejam selecionados ou o usuário pressione ESC
while len(positions) < 4:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC
        break

cv2.destroyAllWindows()

# Imprimindo o código para você copiar os valores
if len(positions) == 4:
    print("\nCopie estas coordenadas para seu código:")
    print("positions = [")
    for pos in positions:
        print(f"    {pos},")
    print("]")
else:
    print(f"Você selecionou apenas {len(positions)} pontos. São necessários exatamente 4 pontos.")