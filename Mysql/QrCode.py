import qrcode

try:
    # Exemplo de dados do pagamento PIX
    pix_data = {
        "chave": "example@chavepix.com",  # Chave PIX do destinatário (email, CPF, CNPJ, etc)
        "valor": "10.00",  # Valor do pagamento
        "nome": "Nome do Recebedor",  # Nome do recebedor
        "cidade": "São Paulo",  # Cidade do recebedor
    }

    # Payload do PIX (BR Code) - formato simplificado para este exemplo
    br_code = (
        "00020126580014BR.GOV.BCB.PIX0114{chave}52040000530398654041{valor}5802BR5913{nome}"
        "6009{cidade}62070503***"
    ).format(
        chave = pix_data["chave"],
        valor = pix_data["valor"],
        nome = pix_data["nome"],
        cidade = pix_data["cidade"]
    )

    # Criação do QR Code
    qr = qrcode.QRCode(
        version = 1,  # Tamanho do QR Code
        error_correction = qrcode.constants.ERROR_CORRECT_L,  # Correção de erro
        box_size = 10,  # Tamanho das caixas
        border = 4,  # Tamanho da borda
    )

    qr.add_data(br_code)
    qr.make(fit=True)

    # Gerar a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')

    # Salvar a imagem do QR Code
    img.save("pagamento.png")

    print("QR Code do PIX gerado com sucesso!")

except ValueError as err:
    print(f"Erro ao gerar QR Code\n\n{err}\n")

finally:
    print("\nQR Code gerado com sucesso!\n")